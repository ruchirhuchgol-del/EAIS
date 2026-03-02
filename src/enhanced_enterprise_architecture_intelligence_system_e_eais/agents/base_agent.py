
"""
Base agent class for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from crewai import Agent


class BaseEaisAgent(ABC):
    """Abstract base class for all EAIS agents."""
    
    def __init__(self, name: str, role: str, goal: str, backstory: str):
        """
        Initialize the base agent.
        
        Args:
            name: Name of the agent
            role: Role of the agent
            goal: Goal of the agent
            backstory: Backstory of the agent
        """
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.agent_instance: Optional[Agent] = None
    
    @abstractmethod
    def create_agent(self) -> Agent:
        """
        Create and configure the crewAI agent instance.
        
        Returns:
            Agent: Configured crewAI agent
        """
        pass
    
    def get_agent(self) -> Agent:
        """
        Get the agent instance, creating it if necessary.
        
        Returns:
            Agent: The agent instance
        """
        if self.agent_instance is None:
            self.agent_instance = self.create_agent()
        return self.agent_instance
    
    def __str__(self) -> str:
        """String representation of the agent."""
        return f"{self.name} ({self.role})"