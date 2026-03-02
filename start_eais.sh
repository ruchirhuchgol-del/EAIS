

# EAIS Startup Script (Unix/Linux/Mac)

# Check if we're running in Windows Subsystem for Linux
if grep -qE "(Microsoft|WSL)" /proc/version &> /dev/null ; then
    echo "Running in Windows Subsystem for Linux (WSL)"
    IS_WSL=true
else
    IS_WSL=false
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python3; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if pip is installed
if ! command_exists pip3; then
    echo "Error: pip3 is not installed or not in PATH"
    exit 1
fi

# Check if uv is installed, if not install it
if ! command_exists uv; then
    echo "Installing uv for dependency management..."
    pip3 install uv
fi

# Install project dependencies
echo "Installing project dependencies..."
uv sync

# Check if environment variables are set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Warning: OPENAI_API_KEY environment variable is not set"
    echo "Please set it before running the application:"
    echo "  export OPENAI_API_KEY='your-api-key-here'"
fi

# Start the application
echo "Starting EAIS application..."
echo "Backend API will be available at http://localhost:8000"
echo "Frontend UI will be available at http://localhost:5173"

# Run the application
uv run python src/enhanced_enterprise_architecture_intelligence_system_e_eais/app.py