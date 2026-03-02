
import sys
from .core.orchestrator import EAISOrchestrator

# This main file is intended to be a way for your to run your
# system locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the system.
    """
    inputs = {
        'business_objectives': 'sample_value',
        'technical_requirements': 'sample_value',
        'compliance_requirements': 'sample_value'
    }
    orchestrator = EAISOrchestrator()
    return orchestrator.execute_workflow(inputs=inputs)


def train():
    """
    Train functionality - not applicable for orchestrator approach.
    """
    print("Training functionality not applicable for orchestrator approach.")
    print("Use run() instead.")

def replay():
    """
    Replay functionality - not applicable for orchestrator approach.
    """
    print("Replay functionality not applicable for orchestrator approach.")
    print("Use run() instead.")

def test():
    """
    Test the system execution and returns the results.
    """
    inputs = {
        'business_objectives': 'sample_value',
        'technical_requirements': 'sample_value',
        'compliance_requirements': 'sample_value'
    }
    orchestrator = EAISOrchestrator()
    return orchestrator.execute_workflow(inputs=inputs)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
