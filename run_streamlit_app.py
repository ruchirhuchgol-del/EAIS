
"""
Streamlit Application Launcher for Enhanced Enterprise Architecture Intelligence System (EAIS)

This script launches the Streamlit application for EAIS, providing an industry-grade
web interface for enterprise architecture intelligence.

Usage:
    python run_streamlit_app.py
    
    or
    
    streamlit run src/enhanced_enterprise_architecture_intelligence_system_e_eais/ui_streamlit/main.py
"""

import os
import sys
import subprocess
import argparse
import socket
from pathlib import Path


def setup_environment():
    """Setup the environment for running the Streamlit application"""
    
    # Get the project root directory
    current_dir = Path(__file__).parent.absolute()
    project_root = current_dir
    
    # Add project root to Python path
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    
    # Set environment variables
    os.environ['PYTHONPATH'] = str(project_root)
    
    print(f"[SUCCESS] Project root: {project_root}")
    print(f"[SUCCESS] Python path configured")
    
    return project_root


def check_dependencies():
    """Check if required dependencies are installed"""
    
    required_packages = [
        'streamlit',
        'plotly',
        'pandas',
        'crewai'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"[OK] {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"[MISSING] {package} is missing")
    
    if missing_packages:
        print(f"\n[ERROR] Missing packages: {', '.join(missing_packages)}")
        print("Please install dependencies using: pip install -r requirements.txt")
        return False
    
    print("[OK] All dependencies are installed")
    return True


def is_port_in_use(port: int) -> bool:
    """Check if a port is already in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("localhost", port))
            return False
        except OSError:
            return True


def find_available_port(start_port: int, max_attempts: int = 3) -> int:
    """Find an available port starting from start_port"""
    for i in range(max_attempts):
        port = start_port + i
        if not is_port_in_use(port):
            return port
    
    # If no port found in the range, return the original port
    return start_port


def run_streamlit_app(project_root: Path, port: int = 8501, host: str = "localhost"):
    """Run the Streamlit application with port fallback strategy"""
    
    # Path to the main Streamlit app
    app_path = project_root / "src" / "enhanced_enterprise_architecture_intelligence_system_e_eais" / "ui_streamlit" / "main.py"
    
    if not app_path.exists():
        print(f"Streamlit app not found at: {app_path}")
        print("Please ensure the Streamlit UI files have been created.")
        return False
    
    # Implement port fallback strategy
    original_port = port
    available_port = find_available_port(port, 3)
    
    if available_port != original_port:
        print(f"[WARNING] Port {original_port} is already in use, falling back to port {available_port}")
        port = available_port
    
    print(f"Starting EAIS Streamlit application...")
    print(f"Application path: {app_path}")
    print(f"Server: http://{host}:{port}")
    print("=" * 60)
    
    # Streamlit command with proper configuration
    cmd = [
        sys.executable, "-m", "streamlit", "run",
        str(app_path),
        "--server.port", str(port),
        "--server.address", host,
        "--server.headless", "false",
        "--browser.gatherUsageStats", "false",
        "--theme.base", "light",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ]
    
    try:
        # Run Streamlit
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to start Streamlit application: {e}")
        print("Please check that all dependencies are installed correctly.")
        return False
    except KeyboardInterrupt:
        print("\nEAIS Streamlit application stopped by user")
        return True
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return False
    
    return True


def validate_environment():
    """Validate the environment and provide helpful error messages"""
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("[ERROR] Python 3.8 or higher is required")
        return False
    
    print(f"[OK] Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check if we're in the right directory
    current_dir = Path(__file__).parent.absolute()
    required_files = [
        "requirements.txt",
        "src/enhanced_enterprise_architecture_intelligence_system_e_eais"
    ]
    
    for file_path in required_files:
        if not (current_dir / file_path).exists():
            print(f"[ERROR] Required file/directory not found: {file_path}")
            print(f"Please ensure you're running this script from the EAIS project root directory")
            return False
    
    print("[OK] Environment validation passed")
    return True


def main():
    """Main function"""
    
    parser = argparse.ArgumentParser(
        description="Launch EAIS Streamlit Application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python run_streamlit_app.py
    python run_streamlit_app.py --port 8080
    python run_streamlit_app.py --host 0.0.0.0 --port 8080
    python run_streamlit_app.py --skip-checks
        """
    )
    
    parser.add_argument(
        "--port", 
        type=int, 
        default=8501,
        help="Port to run the application on (default: 8501)"
    )
    
    parser.add_argument(
        "--host", 
        type=str, 
        default="localhost",
        help="Host to run the application on (default: localhost)"
    )
    
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip dependency and environment checks"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    print("EAIS: Enhanced Enterprise Architecture Intelligence System")
    print("=" * 60)
    print("Starting Streamlit Web Interface...")
    print()
    
    # Validate environment
    if not args.skip_checks:
        if not validate_environment():
            print("\n[ERROR] Environment validation failed")
            sys.exit(1)
        print()
    
    # Setup environment
    project_root = setup_environment()
    print()
    
    # Check dependencies
    if not args.skip_checks:
        if not check_dependencies():
            print("\n[ERROR] Dependency check failed")
            print("Run: pip install -r requirements.txt")
            sys.exit(1)
        print()
    
    # Set debug mode if requested
    if args.debug:
        os.environ['EAIS_DEBUG'] = 'true'
        print("[DEBUG] Debug mode enabled")
        print()
    
    # Display access information
    print("Application Information:")
    print(f"   URL: http://{args.host}:{args.port}")
    print(f"   Project Root: {project_root}")
    print()
    print("Demo Login Credentials:")
    print("   Administrator: admin@eais.com / eais_admin_2024")
    print("   Enterprise Architect: architect@eais.com / architect_2024")
    print("   Business Analyst: analyst@eais.com / analyst_2024")
    print("   Viewer: viewer@eais.com / viewer_2024")
    print()
    print("Press Ctrl+C to stop the application")
    print("=" * 60)
    print()
    
    # Run the application
    success = run_streamlit_app(project_root, args.port, args.host)
    
    if not success:
        print("\n[ERROR] Failed to start EAIS Streamlit application")
        sys.exit(1)


if __name__ == "__main__":
    main()