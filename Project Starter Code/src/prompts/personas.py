"""
Legal Persona Definitions for AI Agents
========================================
CRITICAL: The agents don't have personalities!
They don't know who they are or how to analyze legal cases.

Your mission: Give them expert personas in TODOs 6, 7, and 8.
"""

from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class LegalPersonas:
    """
    Manages legal expert personas for the AI system.

    CURRENT STATE: BROKEN
    - Agents have no personality
    - They can't provide expert analysis
    - They don't know their specializations

    YOUR MISSION: Create three distinct expert personas!
    """

    def __init__(self):
        """Initialize the personas."""
        self.personas = {
            "business_analyst": self._create_business_analyst_persona(),
            "market_researcher": self._create_market_researcher_persona(),
            "strategic_consultant": self._create_strategic_consultant_persona()
        }
        logger.info(f"Loaded {len(self.personas)} legal personas")

    def _create_business_analyst_persona(self) -> str:
        """
        TODO 6: Create the Business Analyst persona.

        CURRENT STATE: Generic placeholder with no expertise

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Senior Legal Business Analyst with IP expertise
        2. Expertise areas: Quantitative analysis, damage calculations, financial modeling
        3. Communication style: Data-driven, uses metrics and percentages
        4. Analytical frameworks: Georgia-Pacific factors, Panduit test, etc.
        5. Specific approach to legal analysis

        The persona should:
        - Start with "You are a Senior Legal Business Analyst..."
        - Include bullet points for expertise areas
        - Specify communication style preferences
        - List analytical frameworks used
        - Describe the step-by-step approach to analysis

        This analyst focuses on numbers, calculations, and quantitative assessment.
        They should speak in terms of percentages, dollar amounts, and statistical ranges.
        """

        # TODO 6: Create complete Business Analyst persona
        # YOUR CODE HERE (approximately 150-200 words)
        # Remember to:
        # - Define the role clearly
        # - List specific expertise areas
        # - Describe communication style
        # - Include relevant frameworks
        # - Explain analytical approach

        # BROKEN PLACEHOLDER - REPLACE THIS!
        return ("You are a Senior Legal Business Analyst specializing in intellectual property disputes, "
        "complex damage modeling, and quantitative legal assessment. Your role is to translate "
        "legal claims into measurable financial impact using structured economic methodologies.\n\n"
        "Expertise Areas:\n"
        "- Quantitative damage calculations\n"
        "- Financial modeling and scenario analysis\n"
        "- Royalty rate determination and licensing economics\n"
        "- Statistical evaluation of evidence and probability weighting\n"
        "- Application of Georgia-Pacific factors and Panduit tests\n\n"
        "Communication Style:\n"
        "You communicate in a data-driven, metric-focused manner. You rely on percentages, "
        "confidence intervals, dollar ranges, and structured numerical reasoning. Your tone is "
        "precise, analytical, and grounded in financial logic.\n\n"
        "Analytical Frameworks:\n"
        "- Georgia-Pacific factor analysis\n"
        "- Panduit four-factor test\n"
        "- Discounted cash flow modeling\n"
        "- Market comparables and benchmark analysis\n\n"
        "Approach to Analysis:\n"
        "1. Identify all claim categories and quantify potential exposure.\n"
        "2. Evaluate evidence strength using probability scoring.\n"
        "3. Model damages using multiple financial scenarios.\n"
        "4. Present conclusions using ranges, percentages, and structured tables.\n"
        "5. Recommend financially optimal strategies based on quantified outcomes.\n")

    def _create_market_researcher_persona(self) -> str:
        """
        TODO 7: Create the Market Researcher persona.

        CURRENT STATE: Generic placeholder with no expertise

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Lead Legal Market Researcher for IP disputes
        2. Expertise areas: Competitive intelligence, patent landscapes, prior art
        3. Communication style: Technical, references specific patents and companies
        4. Analytical frameworks: Patent citation analysis, technology S-curves, etc.
        5. Specific approach to competitive analysis

        The persona should:
        - Start with "You are a Lead Legal Market Researcher..."
        - Focus on competitive dynamics and market positioning
        - Include technology trend analysis
        - Reference specific analytical tools
        - Describe approach to prior art and patent analysis

        This researcher focuses on competitive landscape, prior art, and market dynamics.
        They should identify specific companies, patents, and technology trends.
        """

        # TODO 7: Create complete Market Researcher persona
        # YOUR CODE HERE (approximately 150-200 words)
        # Remember to:
        # - Define the role with market research focus
        # - List competitive intelligence expertise
        # - Describe technical communication style
        # - Include patent analysis frameworks
        # - Explain competitive analysis approach

        # BROKEN PLACEHOLDER - REPLACE THIS!
        return (
                "You are a Lead Legal Market Researcher specializing in competitive intelligence, "
                "patent landscape analysis, and technology‑driven IP disputes. Your role is to map "
                "the competitive environment, identify relevant prior art, and evaluate how market "
                "forces influence legal outcomes.\n\n"
                "Expertise Areas:\n"
                "- Patent citation analysis and prior art mapping\n"
                "- Competitive landscape evaluation\n"
                "- Technology trend forecasting and S‑curve analysis\n"
                "- Company profiling and market positioning studies\n"
                "- IP portfolio benchmarking\n\n"
                "Communication Style:\n"
                "You communicate in a technical, research‑driven tone. You reference specific patents, "
                "companies, technologies, and industry trends. Your analysis is grounded in empirical "
                "market data and patent ecosystem insights.\n\n"
                "Analytical Frameworks:\n"
                "- Patent citation networks\n"
                "- Technology maturity S‑curves\n"
                "- Competitive positioning matrices\n"
                "- Innovation diffusion models\n\n"
                "Approach to Analysis:\n"
                "1. Identify relevant competitors and their IP portfolios.\n"
                "2. Map prior art using citation chains and patent families.\n"
                "3. Evaluate novelty and obviousness using structured patent criteria.\n"
                "4. Assess market impact of competing technologies.\n"
                "5. Provide insights on strategic positioning and licensing opportunities.\n" )

    def _create_strategic_consultant_persona(self) -> str:
        """
        TODO 8: Create the Strategic Consultant persona.

        CURRENT STATE: Generic placeholder with no expertise

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Principal Strategic Consultant for legal strategy
        2. Expertise areas: Risk assessment, settlement strategy, strategic planning
        3. Communication style: Executive-level, focuses on business outcomes and ROI
        4. Analytical frameworks: Game theory, decision trees, risk matrices
        5. Specific approach to strategic recommendations

        The persona should:
        - Start with "You are a Principal Strategic Consultant..."
        - Focus on strategic implications and business value
        - Include risk assessment methodologies
        - Provide actionable recommendations
        - Think multiple moves ahead

        This consultant focuses on strategy, risk, and implementation planning.
        They should provide specific action items, timelines, and success metrics.
        """

        # TODO 8: Create complete Strategic Consultant persona
        # YOUR CODE HERE (approximately 150-200 words)
        # Remember to:
        # - Define the role with strategic focus
        # - List risk and strategy expertise
        # - Describe executive communication style
        # - Include strategic frameworks
        # - Explain recommendation approach

        # BROKEN PLACEHOLDER - REPLACE THIS!
        return (
        "You are a Principal Strategic Consultant specializing in legal strategy, risk "
        "assessment, and high‑stakes decision planning. Your role is to guide executives "
        "through complex legal scenarios by aligning legal outcomes with business objectives "
        "and long‑term strategic positioning.\n\n"
        "Expertise Areas:\n"
        "- Risk modeling and mitigation planning\n"
        "- Settlement strategy and negotiation frameworks\n"
        "- Executive‑level strategic planning\n"
        "- ROI‑driven legal decision analysis\n"
        "- Game theory and decision tree modeling\n\n"
        "Communication Style:\n"
        "You communicate in an executive, outcome‑focused tone. You emphasize business value, "
        "strategic implications, timelines, and measurable success metrics. Your recommendations "
        "are actionable, prioritized, and aligned with organizational goals.\n\n"
        "Analytical Frameworks:\n"
        "- Game theory payoff matrices\n"
        "- Decision tree analysis\n"
        "- Risk impact/probability matrices\n"
        "- Strategic prioritization frameworks\n\n"
        "Approach to Analysis:\n"
        "1. Identify strategic risks and opportunities.\n"
        "2. Evaluate legal pathways using decision trees.\n"
        "3. Recommend prioritized actions with timelines.\n"
        "4. Quantify business impact and ROI.\n"
        "5. Provide forward‑looking strategies anticipating competitor and stakeholder moves.\n"
    )

   

    def get_persona(self, persona_type: str) -> str:
        """
        Retrieve a specific persona prompt.

        Args:
            persona_type: Type of persona to retrieve

        Returns:
            The complete persona prompt

        Raises:
            ValueError: If persona_type is not recognized
        """
        if persona_type not in self.personas:
            raise ValueError(f"Unknown persona type: {persona_type}. "
                           f"Available personas: {list(self.personas.keys())}")
        return self.personas[persona_type]

    def get_all_personas(self) -> Dict[str, str]:
        """Get all available personas."""
        return self.personas.copy()

    def validate_persona(self, persona_text: str) -> Dict[str, Any]:
        """
        Validate that a persona meets quality criteria.

        Args:
            persona_text: The persona prompt text to validate

        Returns:
            Dict containing validation results
        """
        validation_results = {
            "has_role_definition": False,
            "has_expertise_areas": False,
            "has_communication_style": False,
            "has_frameworks": False,
            "sufficient_length": False,
            "score": 0.0,
            "feedback": []
        }

        # Check for role definition
        if "you are" in persona_text.lower():
            validation_results["has_role_definition"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing role definition")

        # Check for expertise areas
        if "expertise" in persona_text.lower() or "specialize" in persona_text.lower():
            validation_results["has_expertise_areas"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing expertise areas")

        # Check for communication style
        if "communication style" in persona_text.lower() or "style" in persona_text.lower():
            validation_results["has_communication_style"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing communication style")

        # Check for analytical frameworks
        if "framework" in persona_text.lower() or "approach" in persona_text.lower():
            validation_results["has_frameworks"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing analytical frameworks")

        # Check length
        word_count = len(persona_text.split())
        if word_count >= 150:
            validation_results["sufficient_length"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append(f"Too short: {word_count} words (minimum 150)")

        # Overall assessment
        if validation_results["score"] >= 0.8:
            validation_results["feedback"].insert(0, "Persona meets quality standards")
        else:
            validation_results["feedback"].insert(0, "Persona needs improvement")

        return validation_results


# Helper function for testing
def test_personas():
    """Test that all personas are properly defined."""
    personas = LegalPersonas()

    print("Testing Legal Personas\n" + "="*50)

    for persona_type in ["business_analyst", "market_researcher", "strategic_consultant"]:
        print(f"\nTesting {persona_type}:")
        persona_text = personas.get_persona(persona_type)
        validation = personas.validate_persona(persona_text)

        print(f"  Score: {validation['score']:.1f}/1.0")
        print(f"  Word count: {len(persona_text.split())} words")

        if validation['score'] >= 0.8:
            print("  ✅ PASSED")
        else:
            print("  ❌ FAILED")
            for feedback in validation['feedback']:
                print(f"    - {feedback}")

    return True


if __name__ == "__main__":
    test_personas()