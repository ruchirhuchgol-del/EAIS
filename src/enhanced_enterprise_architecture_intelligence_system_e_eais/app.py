
"""
Main application entry point for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
import os
import sys
from typing import Dict, Any

from .core.orchestrator import EAISOrchestrator


def main():
    """Main application entry point."""
    print("Starting Enhanced Enterprise Architecture Intelligence System (EAIS)...")
    
    # Example inputs - in a real application, these would come from user input or API
    inputs = {
        'business_objectives': 'Reduce operational costs by 20% while improving system scalability',
        'technical_requirements': 'High availability, microsecond latency, cloud-native deployment',
        'compliance_requirements': 'GDPR, SOC2, PCI-DSS'
    }
    
    try:
        # Run the EAIS system using orchestrator
        orchestrator = EAISOrchestrator()
        result = orchestrator.execute_workflow(inputs=inputs)
        print("EAIS execution completed successfully.")
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error running EAIS: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()