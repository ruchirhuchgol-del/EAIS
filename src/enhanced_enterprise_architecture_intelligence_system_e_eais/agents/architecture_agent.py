
"""
Architecture agent for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from typing import List
from crewai import Agent, LLM
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, ArxivPaperTool

from .base_agent import BaseEaisAgent


class ArchitectureAgent(BaseEaisAgent):
    """Specialized agent for enterprise architecture design and pattern recommendation."""
    
    def __init__(self):
        """Initialize the architecture agent."""
        super().__init__(
            name="Enterprise Architecture Specialist",
            role="Design comprehensive, enterprise-grade system architectures",
            goal="Transform business requirements into production-ready technical solutions",
            backstory=(
                "You are a seasoned enterprise architect with 15+ years of experience "
                "designing large-scale systems for Fortune 500 companies. You've successfully led "
                "digital transformations across industries and have deep expertise in microservices, "
                "cloud-native architectures, and distributed systems."
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
                ArxivPaperTool()
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