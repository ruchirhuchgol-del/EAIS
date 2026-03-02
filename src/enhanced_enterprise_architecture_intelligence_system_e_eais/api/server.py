
"""
REST API server for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from flask import Flask, request, jsonify
from typing import Dict, Any
import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Use relative import
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.orchestrator import EAISOrchestrator


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "EAIS API"}), 200


@app.route('/architecture', methods=['POST'])
def generate_architecture():
    """
    Generate enterprise architecture based on requirements.
    
    Expected JSON payload:
    {
        "business_objectives": ["reduce costs", "improve scalability"],
        "technical_requirements": ["high availability", "microsecond latency"],
        "compliance_requirements": ["GDPR", "SOC2"]
    }
    
    Returns:
        JSON response with architecture results
    """
    try:
        # Get the request data
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Validate required fields
        required_fields = ['business_objectives', 'technical_requirements', 'compliance_requirements']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Run the EAIS orchestrator
        orchestrator = EAISOrchestrator()
        result = orchestrator.execute_workflow(inputs=data)
        
        return jsonify({
            "status": "success",
            "result": str(result)
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/architecture/template', methods=['GET'])
def get_template():
    """Get a template for the architecture request."""
    template = {
        "business_objectives": ["Example: reduce operational costs by 20%"],
        "technical_requirements": ["Example: high availability, cloud-native deployment"],
        "compliance_requirements": ["Example: GDPR, SOC2, PCI-DSS"]
    }
    return jsonify(template), 200


def create_app():
    """Create and configure the Flask application."""
    app.config.update(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-secret-key'),
        ENV=os.environ.get('FLASK_ENV', 'development')
    )
    return app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"Starting EAIS API server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)