
"""
Compliance agent for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from typing import List
from crewai import Agent, LLM
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, FileReadTool, OCRTool

from .base_agent import BaseEaisAgent


class ComplianceAgent(BaseEaisAgent):
    """Specialized agent for compliance and security architecture."""
    
    def __init__(self):
        """Initialize the compliance agent."""
        super().__init__(
            name="Compliance and Security Architect",
            role="Ensure enterprise architectures meet all regulatory requirements",
            goal="Generate implementation guidance and security controls for regulatory compliance",
            backstory=(
                "You are a compliance expert and security architect who has guided organizations "
                "through complex regulatory landscapes for over a decade. You've worked with legal "
                "teams, auditors, and regulators across multiple jurisdictions and have deep knowledge "
                "of privacy laws, financial regulations, and industry standards."
            )
        )
    
    def create_agent(self) -> Agent:
        """
        Create and configure the crewAI agent instance.
        
        Returns:
            Agent: Configured crewAI agent
        """
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            tools=[
                ScrapeWebsiteTool(),
                SerperDevTool(),
                FileReadTool(),
                OCRTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )