
"""
Test script for the EAIS API.
"""
import sys
import os

# Add the src folder to the path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

def test_api_import():
    """Test if we can import the API server."""
    try:
        from enhanced_enterprise_architecture_intelligence_system_e_eais.api.server import app
        print("[SUCCESS] API server imported successfully")
        return True
    except Exception as e:
        print(f"[FAILURE] Error importing API server: {e}")
        return False

def test_orchestrator_import():
    """Test if we can import the orchestrator."""
    try:
        from enhanced_enterprise_architecture_intelligence_system_e_eais.core.orchestrator import EAISOrchestrator
        print("[SUCCESS] Orchestrator imported successfully")
        return True
    except Exception as e:
        print(f"[FAILURE] Error importing orchestrator: {e}")
        return False

def main():
    """Run API tests."""
    print("Testing EAIS API components...")
    print("=" * 40)
    
    tests = [
        test_orchestrator_import,
        test_api_import
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("Done: All tests passed!")
        return 0
    else:
        print("Fail: Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())