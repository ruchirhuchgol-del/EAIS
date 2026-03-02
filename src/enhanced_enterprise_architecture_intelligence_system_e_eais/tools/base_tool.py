
"""
Base tool class for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from abc import ABC, abstractmethod
from typing import Dict, Any
from crewai.tools import BaseTool


class BaseEaisTool(ABC):
    """Abstract base class for all EAIS custom tools."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize the base tool.
        
        Args:
            name: Name of the tool
            description: Description of the tool
        """
        self.name = name
        self.description = description
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool with the provided parameters.
        
        Args:
            **kwargs: Tool-specific parameters
            
        Returns:
            Result of tool execution
        """
        pass


class EaisCrewAITool(BaseTool, BaseEaisTool):
    """Base class for EAIS tools that integrate with crewAI."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize the crewAI tool.
        
        Args:
            name: Name of the tool
            description: Description of the tool
        """
        BaseTool.__init__(self)
        BaseEaisTool.__init__(self, name, description)
    
    @abstractmethod
    def _run(self, **kwargs) -> Any:
        """
        Execute the tool with the provided parameters (crewAI interface).
        
        Args:
            **kwargs: Tool-specific parameters
            
        Returns:
            Result of tool execution
        """
        pass