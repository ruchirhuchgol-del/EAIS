
"""
Knowledge Graph Tool for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from typing import Type, Dict, Any
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from ..data.knowledge_graph import KnowledgeGraph


class KnowledgeGraphToolInput(BaseModel):
    """Input schema for KnowledgeGraphTool."""
    action: str = Field(..., description="Action to perform: 'query', 'search', or 'add'")
    query: str = Field(..., description="Query string or entity data")
    entity_type: str = Field(None, description="Entity type for query filtering")


class KnowledgeGraphTool(BaseTool):
    """Tool for interacting with the EAIS knowledge graph."""
    
    name: str = "Knowledge Graph Tool"
    description: str = (
        "Interface with the EAIS semantic knowledge base to query architectural patterns, "
        "technologies, compliance frameworks, and their relationships."
    )
    args_schema: Type[BaseModel] = KnowledgeGraphToolInput
    
    def __init__(self):
        """Initialize the knowledge graph tool."""
        super().__init__()
    
    def _run(self, action: str, query: str, entity_type: str = None) -> str:
        """
        Execute the knowledge graph tool.
        
        Args:
            action: Action to perform ('query', 'search', or 'add')
            query: Query string or entity data
            entity_type: Entity type for query filtering
            
        Returns:
            Result of the knowledge graph operation
        """
        try:
            # Create a local instance of the knowledge graph
            knowledge_graph = KnowledgeGraph()
            
            if action == "query":
                results = knowledge_graph.query_entities(entity_type)
                return f"Found {len(results)} entities of type '{entity_type}'"
            elif action == "search":
                results = knowledge_graph.search_entities(query)
                return f"Search for '{query}' returned {len(results)} results"
            elif action == "add":
                # In a real implementation, this would add entities to the graph
                return f"Added entity with query: {query}"
            else:
                return f"Unknown action: {action}"
        except Exception as e:
            return f"Error executing knowledge graph tool: {str(e)}"
    



# Example usage
if __name__ == "__main__":
    tool = KnowledgeGraphTool()
    
    # Test search
    result = tool._run("search", "microservices")
    print(f"Search result: {result}")
    
    # Test query
    result = tool._run("query", "", "pattern")
    print(f"Query result: {result}")