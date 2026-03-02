
"""
Business impact agent for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from typing import List
from crewai import Agent, LLM
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from .base_agent import BaseEaisAgent


class BusinessAgent(BaseEaisAgent):
    """Specialized agent for business impact analysis and TCO modeling."""
    
    def __init__(self):
        """Initialize the business impact agent."""
        super().__init__(
            name="Business Impact and TCO Analyst",
            role="Perform comprehensive business impact analysis for enterprise architectures",
            goal="Translate technical architectural decisions into business value metrics",
            backstory=(
                "You are a seasoned business analyst and financial modeler with deep expertise "
                "in technology investments and enterprise architecture economics. You've built "
                "TCO models for billion-dollar IT transformations and have a proven track record "
                "of helping C-level executives understand the business implications of architectural "
                "decisions."
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
                SerperDevTool()
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