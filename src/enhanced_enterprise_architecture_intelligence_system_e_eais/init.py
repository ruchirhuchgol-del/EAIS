
"""
System initialization module for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
import os
from typing import Dict, Any


def initialize_system() -> Dict[str, Any]:
    """
    Initialize the EAIS system with default configurations.
    
    Returns:
        Dict[str, Any]: System configuration
    """
    config = {
        "system_name": "Enhanced Enterprise Architecture Intelligence System",
        "version": "1.0.0",
        "debug": os.getenv("EAIS_DEBUG", "False").lower() == "true",
        "log_level": os.getenv("EAIS_LOG_LEVEL", "INFO"),
        "data_directory": os.getenv("EAIS_DATA_DIR", "./data"),
        "output_directory": os.getenv("EAIS_OUTPUT_DIR", "./output"),
    }
    
    # Create necessary directories
    os.makedirs(config["data_directory"], exist_ok=True)
    os.makedirs(config["output_directory"], exist_ok=True)
    
    print(f"EAIS System initialized with config: {config}")
    return config


def validate_environment() -> bool:
    """
    Validate that the system environment is properly configured.
    
    Returns:
        bool: True if environment is valid, False otherwise
    """
    required_vars = ["OPENAI_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Missing required environment variables: {missing_vars}")
        print("Please set these variables in your .env file or environment.")
        return False
    
    return True


if __name__ == "__main__":
    if not validate_environment():
        exit(1)
    
    config = initialize_system()
    print("EAIS system initialization complete.")