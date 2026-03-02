
"""
Knowledge graph engine for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from typing import Dict, List, Any, Optional
import json
import os


class KnowledgeGraph:
    """Enterprise knowledge graph engine for EAIS."""
    
    def __init__(self, storage_path: str = "./data/knowledge_graph.json"):
        """
        Initialize the knowledge graph.
        
        Args:
            storage_path: Path to the knowledge graph storage file
        """
        self.storage_path = storage_path
        self.graph = {}
        self._load_graph()
    
    def _load_graph(self):
        """Load the knowledge graph from storage."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    self.graph = json.load(f)
                print(f"Knowledge graph loaded from {self.storage_path}")
            except Exception as e:
                print(f"Error loading knowledge graph: {e}")
                self.graph = {}
        else:
            print("No existing knowledge graph found, starting with empty graph")
            self.graph = {}
    
    def _save_graph(self):
        """Save the knowledge graph to storage."""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
            
            with open(self.storage_path, 'w') as f:
                json.dump(self.graph, f, indent=2)
            print(f"Knowledge graph saved to {self.storage_path}")
        except Exception as e:
            print(f"Error saving knowledge graph: {e}")
    
    def add_entity(self, entity_id: str, entity_type: str, properties: Dict[str, Any]):
        """
        Add an entity to the knowledge graph.
        
        Args:
            entity_id: Unique identifier for the entity
            entity_type: Type of the entity (e.g., 'technology', 'pattern', 'framework')
            properties: Properties of the entity
        """
        if entity_id not in self.graph:
            self.graph[entity_id] = {
                "type": entity_type,
                "properties": properties,
                "relationships": []
            }
        else:
            # Update existing entity
            self.graph[entity_id]["type"] = entity_type
            self.graph[entity_id]["properties"].update(properties)
        
        self._save_graph()
    
    def add_relationship(self, source_id: str, target_id: str, relationship_type: str, properties: Dict[str, Any] = None):
        """
        Add a relationship between two entities.
        
        Args:
            source_id: ID of the source entity
            target_id: ID of the target entity
            relationship_type: Type of relationship
            properties: Additional properties of the relationship
        """
        if source_id not in self.graph:
            print(f"Warning: Source entity {source_id} not found in graph")
            return
        
        if target_id not in self.graph:
            print(f"Warning: Target entity {target_id} not found in graph")
            return
        
        relationship = {
            "target": target_id,
            "type": relationship_type,
            "properties": properties or {}
        }
        
        # Check if relationship already exists
        existing_relationships = [
            r for r in self.graph[source_id]["relationships"]
            if r["target"] == target_id and r["type"] == relationship_type
        ]
        
        if not existing_relationships:
            self.graph[source_id]["relationships"].append(relationship)
            self._save_graph()
    
    def query_entities(self, entity_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Query entities in the knowledge graph.
        
        Args:
            entity_type: Optional filter by entity type
            
        Returns:
            List of entities matching the criteria
        """
        results = []
        for entity_id, entity_data in self.graph.items():
            if entity_type is None or entity_data["type"] == entity_type:
                result = {"id": entity_id, **entity_data}
                results.append(result)
        return results
    
    def get_entity(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific entity from the knowledge graph.
        
        Args:
            entity_id: ID of the entity to retrieve
            
        Returns:
            Entity data or None if not found
        """
        return self.graph.get(entity_id)
    
    def search_entities(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for entities containing the query string.
        
        Args:
            query: Search query string
            
        Returns:
            List of matching entities
        """
        results = []
        query_lower = query.lower()
        
        for entity_id, entity_data in self.graph.items():
            # Search in entity ID
            if query_lower in entity_id.lower():
                results.append({"id": entity_id, **entity_data})
                continue
            
            # Search in properties
            for key, value in entity_data["properties"].items():
                if isinstance(value, str) and query_lower in value.lower():
                    results.append({"id": entity_id, **entity_data})
                    break
        
        return results


# Example usage
if __name__ == "__main__":
    # Create a knowledge graph instance
    kg = KnowledgeGraph("./data/test_knowledge_graph.json")
    
    # Add some sample entities
    kg.add_entity("aws_lambda", "technology", {
        "name": "AWS Lambda",
        "category": "serverless computing",
        "provider": "Amazon Web Services",
        "description": "Event-driven, serverless computing platform"
    })
    
    kg.add_entity("microservices", "pattern", {
        "name": "Microservices Architecture",
        "category": "architectural pattern",
        "description": "Architectural style that structures an application as a collection of loosely coupled services"
    })
    
    # Add a relationship
    kg.add_relationship("aws_lambda", "microservices", "supports", {
        "compatibility": "high",
        "reason": "AWS Lambda functions can be used as microservices"
    })
    
    # Query entities
    tech_entities = kg.query_entities("technology")
    print(f"Technology entities: {len(tech_entities)}")
    
    # Search entities
    search_results = kg.search_entities("serverless")
    print(f"Search results for 'serverless': {len(search_results)}")