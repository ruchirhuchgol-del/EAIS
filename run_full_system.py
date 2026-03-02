
"""
Script to run the full EAIS system (backend API + frontend UI).
"""
import subprocess
import sys
import os
import time

def run_backend():
    """Start the backend API server."""
    print("Starting EAIS backend API server...")
    try:
        # Change to the API directory
        api_dir = os.path.join("src", "enhanced_enterprise_architecture_intelligence_system_e_eais", "api")
        os.chdir(api_dir)
        
        # Start the Flask server
        backend_process = subprocess.Popen([
            sys.executable, "server.py"
        ])
        
        print("Backend API server started on http://localhost:8000")
        return backend_process
    except Exception as e:
        print(f"Error starting backend: {e}")
        return None

def run_frontend():
    """Start the frontend UI server."""
    print("Starting EAIS frontend UI server...")
    try:
        # Change to the UI directory
        ui_dir = os.path.join("src", "enhanced_enterprise_architecture_intelligence_system_e_eais", "ui")
        
        # Start the Vite development server
        frontend_process = subprocess.Popen([
            "npm", "run", "dev"
        ], cwd=ui_dir)
        
        print("Frontend UI server started on http://localhost:5173")
        return frontend_process
    except Exception as e:
        print(f"Error starting frontend: {e}")
        return None

def main():
    """Run the full EAIS system."""
    print("Starting Enhanced Enterprise Architecture Intelligence System (EAIS)...")
    
    # Start backend
    backend_process = run_backend()
    if not backend_process:
        print("Failed to start backend server")
        return 1
    
    # Give backend time to start
    time.sleep(3)
    
    # Start frontend
    frontend_process = run_frontend()
    if not frontend_process:
        print("Failed to start frontend server")
        backend_process.terminate()
        return 1
    
    print("\nEAIS system is running!")
    print("Access the application at: http://localhost:5173")
    print("Backend API is available at: http://localhost:8000")
    print("\nPress Ctrl+C to stop both servers")
    
    try:
        # Wait for both processes
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down EAIS system...")
        backend_process.terminate()
        frontend_process.terminate()
        print("EAIS system stopped.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())