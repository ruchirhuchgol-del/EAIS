
"""
Demo script for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Use relative imports
from src.enhanced_enterprise_architecture_intelligence_system_e_eais.agents.architecture_agent import ArchitectureAgent
from src.enhanced_enterprise_architecture_intelligence_system_e_eais.tools.knowledge_graph_tool import KnowledgeGraphTool
from src.enhanced_enterprise_architecture_intelligence_system_e_eais.data.knowledge_graph import KnowledgeGraph


def test_architecture_agent():
    """Test the architecture agent creation."""
    print("Testing Architecture Agent...")
    try:
        agent = ArchitectureAgent()
        agent_instance = agent.get_agent()
        print(f"✓ Architecture Agent created successfully: {agent_instance.role}")
        return True
    except Exception as e:
        print(f"✗ Error creating Architecture Agent: {e}")
        return False


def test_knowledge_graph_tool():
    """Test the knowledge graph tool."""
    print("Testing Knowledge Graph Tool...")
    try:
        tool = KnowledgeGraphTool()
        print(f"✓ Knowledge Graph Tool created successfully: {tool.name}")
        return True
    except Exception as e:
        print(f"✗ Error creating Knowledge Graph Tool: {e}")
        return False


def test_knowledge_graph():
    """Test the knowledge graph engine."""
    print("Testing Knowledge Graph Engine...")
    try:
        kg = KnowledgeGraph("./data/demo_knowledge_graph.json")
        print("✓ Knowledge Graph Engine created successfully")
        return True
    except Exception as e:
        print(f"✗ Error creating Knowledge Graph Engine: {e}")
        return False


def main():
    """Run all demo tests."""
    print("EAIS Demo Script")
    print("=" * 50)
    
    tests = [
        test_architecture_agent,
        test_knowledge_graph_tool,
        test_knowledge_graph
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Demo Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! EAIS is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())