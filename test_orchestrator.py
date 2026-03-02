
"""Simple test for the orchestrator."""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from enhanced_enterprise_architecture_intelligence_system_e_eais.core.orchestrator import EAISOrchestrator
    
    print("✅ Successfully imported EAISOrchestrator")
    
    # Test orchestrator
    orchestrator = EAISOrchestrator()
    inputs = {
        'business_objectives': 'test objectives', 
        'technical_requirements': 'test requirements', 
        'compliance_requirements': 'test compliance'
    }
    
    result = orchestrator.execute_workflow(inputs)
    print("✅ Orchestrator executed successfully")
    print(f"Result: {result}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()