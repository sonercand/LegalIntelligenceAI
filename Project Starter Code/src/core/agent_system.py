"""
Legal Intelligence Agent System - Core Agent Implementation
===========================================================
CRITICAL: This module is BROKEN. The agents can't connect to Vertex AI,
generate content, or work together. You need to fix it!

The infrastructure is here, but the intelligence is missing.
"""

import os
import time
import json
import logging
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import asyncio

# Google AI imports
from google import genai
from google.genai import types
import vertexai
from vertexai.generative_models import GenerativeModel

# Internal imports
from ..models.legal_models import (
    LegalScenario,
    AnalysisReport,
    AgentResponse,
    ReportSection,
    TokenUsage
)
from ..prompts.personas import LegalPersonas
from .quality_validator import QualityValidator

logger = logging.getLogger(__name__)



class LegalIntelligenceAgent:
    """
    Main orchestrator for the Legal Intelligence AI System.

    CURRENT STATE: BROKEN
    - Can't connect to Vertex AI
    - Can't generate content
    - Can't chain context between agents

    YOUR MISSION: Fix the TODOs to make this system work!
    """

    def __init__(self, project_id: str, location: str = "us-central1", model_name: str = "gemini-2.5-flash"):
        """Initialize the Legal Intelligence Agent system."""
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self.client = None
        self.initialized = False

        # Components
        self.personas = LegalPersonas()
        self.quality_validator = QualityValidator()

        # Performance tracking
        self.token_usage_history = []
        self.processing_times = []
        self.success_count = 0
        self.total_attempts = 0

        # Configuration
        self.generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 4096,
        }

        logger.info(f"LegalIntelligenceAgent initialized for project {project_id}")

    def initialize_vertex_ai(self) -> bool:
        try:
            logger.info(f"Initializing Vertex AI for project: {self.project_id}")

            # Initialize Vertex AI
            vertexai.init(project=self.project_id, location=self.location)

            # Create model instance
            self.model = GenerativeModel(self.model_name)

            # Test connection
            self.model.generate_content("test")

            # Success
            self.initialized = True
            return True

        except Exception as e:
            logger.error(f"Vertex AI initialization failed: {str(e)}")
            self.initialized = False
            return False      

    def generate_section_content(
        self,
        persona: str,
        section_type: str,
        scenario: LegalScenario,
        previous_sections: List[ReportSection] = None
    ) -> Tuple[str, TokenUsage, float]:
        """
        TODO 2: Generate content for a specific report section.

        CURRENT STATE: Returns dummy content, no actual AI generation

        Requirements:
        1. Build a comprehensive prompt combining persona, scenario, and context
        2. Generate content using self.model with retry logic
        3. Track token usage from response.usage_metadata
        4. Calculate cost based on tokens
        5. Handle errors with exponential backoff

        Args:
            persona: The agent persona text (from personas.py)
            section_type: Type of section (e.g., "liability_assessment")
            scenario: The legal case to analyze
            previous_sections: Previous sections for context chaining

        Returns:
            Tuple of (content, token_usage, cost)

        Hints:
        - Use self._build_prompt() to create the prompt
        - Use self.model.generate_content() with self.generation_config
        - Implement retry with exponential backoff (2^attempt seconds)
        - Extract token counts from response.usage_metadata
        - Use self._calculate_cost() for cost calculation
        """
               # TODO 2: Implement content generation with retry logic
                # YOUR CODE HERE (approximately 25-35 lines)
                # Steps:
                # 1. Set max_retries = 3
                # 2. Loop for retry attempts
                # 3. Try to generate content using self.model.generate_content()
                # 4. Extract text from response
                # 5. Create TokenUsage from response.usage_metadata
                # 6. Calculate cost using self._calculate_cost()
                # 7. Handle exceptions with exponential backoff
                # 8. Return (content, token_usage, cost)
        

  
        if not self.initialized:
            raise RuntimeError("Agent system not initialized. Call initialize_vertex_ai() first.")

        start_time = time.time()
        previous_sections = previous_sections or []
        max_retries = 3
        last_error = None
        # Build the comprehensive prompt
        for attempt in range(max_retries):
            retry_number = attempt
            try:
                prompt = self._build_prompt(persona, section_type, scenario, previous_sections,retry_number=retry_number)
                response = self.model.generate_content(
                    contents=prompt,
                    generation_config=self.generation_config)
                # Extract text
                if hasattr(response, "text"):
                    content = response.text
                elif hasattr(response, "candidates") and response.candidates:
                    content = response.candidates[0].content.parts[0].text
                else:
                    raise ValueError("Model returned no text content.")  
                # Extract usage metadata safely
                usage = getattr(response, "usage_metadata", None)
                if usage:
                    input_tokens = getattr(usage, "prompt_token_count", 0)
                    output_tokens = getattr(usage, "candidates_token_count", 0)
                    total_tokens = getattr(usage, "total_token_count", input_tokens + output_tokens)
                else:
                    input_tokens = output_tokens = total_tokens = 0

                token_usage = TokenUsage(
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    total_tokens=total_tokens
                )

                # Cost calculation
                cost = self._calculate_cost(token_usage) 
                # Metrics
                self.token_usage_history.append(token_usage)
                self.processing_times.append(time.time() - start_time)
                self.total_attempts += 1
                self.success_count += 1

                return content, token_usage, cost
            except Exception as e:
                last_error = e
                logger.error(
                    f"Error generating section '{section_type}' on attempt {attempt+1}: {str(e)}"
                )
                time.sleep(2 ** attempt)  # exponential backoff
        self.total_attempts += 1
        raise RuntimeError(
                    f"Failed to generate section '{section_type}' after {max_retries} attempts. Last error: {last_error}"
                )
 
    

    async def generate_complete_report(self, scenario: LegalScenario) -> AnalysisReport:
        logger.info(f"Starting complete report generation for case: {scenario.case_name}")
        start_time = time.time()

        section_config = [
            ("liability_assessment", "business_analyst"),
            ("damage_calculation", "business_analyst"),
            ("prior_art_analysis", "market_researcher"),
            ("competitive_landscape", "market_researcher"),
            ("risk_assessment", "strategic_consultant"),
            ("strategic_recommendations", "strategic_consultant"),
        ]

        sections: List[ReportSection] = []
        total_cost = 0.0
        total_tokens = 0

        for section_type, persona_key in section_config:

            persona_text = self.personas.get_persona(persona_key)

            content, token_usage, cost = await asyncio.to_thread(
                self.generate_section_content,
                persona_text,
                section_type,
                scenario,
                sections
            )

            validation = self.quality_validator.validate_section(
                content,
                section_type=section_type,
                expected_elements=self._get_expected_elements(section_type)
            )

            quality_score = validation.overall_score

            if quality_score < 0.7:
                logger.warning(f"Quality too low ({quality_score:.2f}) for {section_type}. Retrying...")

                content, token_usage, cost = await asyncio.to_thread(
                    self.generate_section_content,
                    persona_text,
                    section_type,
                    scenario,
                    sections
                )

                validation = self.quality_validator.validate_section(
                    content,
                    section_type=section_type,
                    expected_elements=self._get_expected_elements(section_type)
                )
                quality_score = validation.overall_score

            section_obj = ReportSection(
                type=section_type,
                title=self._get_section_title(section_type),
                content=content,
                agent_type=self._get_agent_type(persona_text),
                quality_score=quality_score,
                tokens_used=token_usage.total_tokens,
                cost=cost,
                timestamp=datetime.now().isoformat()
            )

            sections.append(section_obj)
            total_cost += cost
            total_tokens += token_usage.total_tokens

        executive_summary = self._generate_executive_summary(sections, scenario)

        report = AnalysisReport(
            scenario=scenario,
            sections=sections,
            executive_summary=executive_summary,
            total_cost=total_cost,
            total_tokens=total_tokens,
            processing_time=time.time() - start_time,
            confidence_score=sum(s.quality_score for s in sections) / len(sections),
            timestamp=datetime.now().isoformat(),
            metadata={"section_count": len(sections)}
        )

        return report
        

    def _build_prompt(
        self,
        persona: str,
        section_type: str,
        scenario: LegalScenario,
        previous_sections: List[ReportSection],
        retry_number: int = 0
    ) -> str:
        """Build a comprehensive prompt combining persona, context, and chain-of-thought instructions."""

        # Start with the persona
        prompt = f"{persona}\n\n"
        # Role instructions
        prompt += (
        "ROLE INSTRUCTIONS:\n"
        "You are acting strictly in the role described above. Maintain the persona’s tone, "
        "analytical style, and domain expertise throughout the entire response.\n\n"
        )
        # Retry metadata
        prompt += (
            "RETRY METADATA:\n"
            f"Retry Attempt: {retry_number}\n"
            "If retry_number > 0, improve clarity, structure, completeness, and alignment with the persona’s analytical frameworks.\n\n"
        )
            # Reasoning instructions
        prompt += (
            "REASONING INSTRUCTIONS:\n"
            "You must use step-by-step reasoning to analyze this legal case. Structure your analysis as follows:\n"
            "1. Identify the key legal issues\n"
            "2. Analyze the relevant facts\n"
            "3. Apply legal principles\n"
            "4. Provide your conclusions\n"
            "Think through each step carefully before moving to the next.\n\n"
        )
         # Previous sections context
        prompt += "PREVIOUS ANALYSIS CONTEXT:\n"
        prompt += (
            "Use the following previous sections ONLY as context. Do NOT repeat their content. "
            "Do NOT restate their conclusions. Build upon them and ensure consistency.\n\n"
        )
        if previous_sections:
            for section in previous_sections[-2:]:
                excerpt = section.content[:500]
                prompt += f"{section.title}:\n{excerpt}...\n\n"
            else:
                prompt += "(No previous sections available.)\n\n"
        # Scenario details
        prompt += "CASE DETAILS:\n"
        prompt += f"Case Name: {scenario.case_name}\n"
        prompt += f"Case Type: {scenario.case_type}\n"
        prompt += f"Filing Date: {scenario.filing_date}\n"
        prompt += f"Parties Involved: {', '.join(scenario.parties_involved)}\n"
        prompt += f"Key Issues: {', '.join(scenario.key_issues)}\n"
        prompt += f"Urgency Level: {scenario.urgency_level}\n"
        if scenario.additional_context:
            prompt += f"Additional Context: {scenario.additional_context}\n"

        prompt += "\nComplaint Summary:\n"
        prompt += f"{scenario.complaint_text}\n\n"

        # Section task
        prompt += (
            "SECTION TASK:\n"
            f"Provide a {section_type.replace('_', ' ')} for the case above.\n\n"
        )

        # Section-specific instructions
        prompt += "SECTION-SPECIFIC INSTRUCTIONS:\n"
        prompt += self._get_section_instructions(section_type) + "\n\n"
        # Output format requirements
        prompt += (
        "OUTPUT FORMAT REQUIREMENTS:\n"
        "Your output MUST follow this structure:\n"
        f"SECTION TITLE: {self._get_section_title(section_type)}\n"
        "1. Key Issues\n"
        "2. Fact Analysis\n"
        "3. Legal Principles\n"
        "4. Conclusions\n"
        "Ensure each section is clearly labeled and aligned with the persona’s analytical style.\n"
        )


        return prompt

    def _get_section_instructions(self, section_type: str) -> str:
        """Get specific instructions for each section type."""
        instructions = {
            "liability_assessment": """
Analyze liability by:
- Identifying each potential claim
- Evaluating strength of evidence
- Assessing probability of success (use percentages)
- Citing relevant precedents or legal principles
""",
            "damage_calculation": """
Calculate potential damages by:
- Identifying categories of damages (actual, statutory, punitive)
- Providing specific dollar ranges
- Explaining calculation methodology
- Considering mitigation factors
""",
            "prior_art_analysis": """
Analyze prior art and precedents by:
- Identifying relevant existing patents/IP
- Assessing validity challenges
- Evaluating obviousness arguments
- Determining freedom to operate
""",
            "competitive_landscape": """
Analyze competitive implications by:
- Identifying key competitors affected
- Assessing market position changes
- Evaluating licensing opportunities
- Predicting competitor responses
""",
            "risk_assessment": """
Assess risks by:
- Identifying legal risks (probability and impact)
- Evaluating business risks
- Analyzing reputational risks
- Providing risk mitigation strategies
""",
            "strategic_recommendations": """
Provide strategic recommendations by:
- Outlining 3-5 specific action items
- Prioritizing by impact and urgency
- Estimating resource requirements
- Defining success metrics
"""
        }
        return instructions.get(section_type, "Provide comprehensive analysis for this section.")

    def _get_expected_elements(self, section_type: str) -> List[str]:
        """Get expected elements for quality validation."""
        elements_map = {
            "liability_assessment": ["claims", "evidence", "probability", "precedent"],
            "damage_calculation": ["damages", "calculation", "amount", "methodology"],
            "prior_art_analysis": ["patents", "prior art", "validity", "obviousness"],
            "competitive_landscape": ["competitors", "market", "position", "licensing"],
            "risk_assessment": ["risks", "probability", "impact", "mitigation"],
            "strategic_recommendations": ["recommendations", "action", "timeline", "resources"]
        }
        return elements_map.get(section_type, ["analysis", "assessment", "conclusion"])

    def _get_section_title(self, section_type: str) -> str:
        """Get formatted title for section."""
        titles = {
            "liability_assessment": "Liability Assessment",
            "damage_calculation": "Damage Calculation",
            "prior_art_analysis": "Prior Art Analysis",
            "competitive_landscape": "Competitive Landscape",
            "risk_assessment": "Risk Assessment",
            "strategic_recommendations": "Strategic Recommendations"
        }
        return titles.get(section_type, section_type.replace("_", " ").title())

    def _get_agent_type(self, persona: str) -> str:
        """Determine agent type from persona text."""
        if "Business Analyst" in persona:
            return "business_analyst"
        elif "Market Research" in persona:
            return "market_researcher"
        elif "Strategic" in persona:
            return "strategic_consultant"
        else:
            return "unknown"

    def _generate_executive_summary(self, sections: List[ReportSection], scenario: LegalScenario) -> str:
        """Generate executive summary from all sections."""
        summary = f"EXECUTIVE SUMMARY - {scenario.case_name}\n"
        summary += "=" * 50 + "\n\n"

        # Extract key points from each section
        for section in sections:
            # Get first substantive paragraph
            paragraphs = [p.strip() for p in section.content.split('\n\n') if len(p.strip()) > 50]
            if paragraphs:
                summary += f"{section.title}:\n"
                summary += f"{paragraphs[0][:200]}...\n\n"

        # Add overall assessment
        avg_quality = sum(s.quality_score for s in sections) / len(sections) if sections else 0
        summary += f"Overall Confidence: {avg_quality:.1%}\n"
        summary += f"Key Issues Identified: {len(scenario.key_issues)}\n"
        summary += f"Urgency Level: {scenario.urgency_level}\n"

        return summary

    def _calculate_cost(self, token_usage: TokenUsage) -> float:
        """Calculate cost based on token usage."""
        # Example pricing (adjust based on actual Vertex AI pricing)
        # Gemini pricing as of 2024: ~$0.00025 per 1K input tokens, ~$0.00125 per 1K output tokens
        #uptaded for 2026 August pricing for GEMINI 2.5 flash
        input_cost = (token_usage.input_tokens / 1000) * 0.00030
        output_cost = (token_usage.output_tokens / 1000) * 0.00250 
        return input_cost + output_cost

    # Metric tracking methods

    def get_token_usage_stats(self) -> Dict[str, Any]:
        """Get token usage statistics."""
        if not self.token_usage_history:
            return {"error": "No usage data available"}

        total_input = sum(u.input_tokens for u in self.token_usage_history)
        total_output = sum(u.output_tokens for u in self.token_usage_history)
        total_tokens = sum(u.total_tokens for u in self.token_usage_history)

        return {
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "total_tokens": total_tokens,
            "average_per_request": total_tokens / len(self.token_usage_history) if self.token_usage_history else 0,
            "request_count": len(self.token_usage_history)
        }

    def get_avg_processing_time(self) -> float:
        """Get average processing time."""
        if not self.processing_times:
            return 0.0
        return sum(self.processing_times) / len(self.processing_times)

    def get_success_rate(self) -> float:
        """Get success rate of generations."""
        if self.total_attempts == 0:
            return 0.0
        return self.success_count / self.total_attempts