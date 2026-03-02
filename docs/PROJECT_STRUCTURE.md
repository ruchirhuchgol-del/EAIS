# EAIS Project Structure

## Overview

The Enterprise Architecture Intelligence System (EAIS) follows a modular, agent-based architecture designed for extensibility and maintainability.

## Directory Structure

```
EAIS/
├── docs/
│   ├── EAIS_integration/      # Next.js Integration Portal
│   └── ...
├── src/
│   └── enhanced_enterprise_architecture_intelligence_system_e_eais/
│       ├── __init__.py        # Package initialization
│       ├── app.py            # Main application entry point
│       ├── init.py           # System initialization
│       ├── agents/           # Specialist AI agents
│       │   ├── __init__.py
│       │   ├── base_agent.py        # Abstract base class
│       │   ├── architecture_agent.py # Core architecture generation
│       │   ├── compliance_agent.py   # Compliance validation
│       │   └── business_agent.py    # Business impact analysis
│       ├── api/              # REST API interface
│       │   ├── __init__.py
│       │   └── server.py            # Flask server implementation
│       ├── config/           # Configuration management
│       │   ├── __init__.py
│       │   ├── agents.yaml          # Agent configurations
│       │   └── tasks.yaml           # Task definitions
│       ├── core/             # Core orchestrator
│       │   ├── __init__.py
│       │   └── orchestrator.py      # Global orchestrator
│       ├── data/             # Data layer components
│       │   ├── __init__.py
│       │   └── knowledge_graph.py   # Knowledge graph engine
│       ├── tools/            # Custom tools
│       │   ├── __init__.py
│       │   ├── base_tool.py         # Abstract base class
│       │   ├── knowledge_graph_tool.py
│       │   ├── artifact_generation_tool.py
│       │   ├── cost_carbon_optimizer.py
│       │   ├── compliance_evidence_automator.py
│       │   ├── architecture_evolution_engine.py
│       │   ├── dependency_mapper.py
│       │   ├── secure_artifact_vault.py
│       │   └── federated_learning_orchestrator.py
│       ├── ui/               # Web user interface
│       │   ├── package.json
│       │   ├── vite.config.js
│       │   ├── index.html
│       │   └── src/
│       │       ├── main.jsx
│       │       ├── App.jsx
│       │       ├── index.css
│       │       └── App.css
│       └── utils/            # Utility functions
│           ├── __init__.py
│           └── logger.py            # Logging utilities
├── tests/                    # Unit and integration tests
│   ├── __init__.py
│   ├── test_architecture_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── test_all_tools.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── test_all_agents.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── test_orchestrator.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_server.py
│   └── run_all_tests.py      # Comprehensive test runner
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── Dockerfile                # Container definition
├── Dockerfile.ui             # UI container definition
├── docker-compose.yml        # Multi-container deployment
├── demo.py                   # Demonstration script
├── test_eais.py              # System tests
├── test_api.py               # API tests
├── run_all_tests.py          # Test runner
├── SYSTEM_REVIEW.md          # System review and enhancement summary
├── ENHANCEMENT_SUMMARY.md    # Enhancement documentation
├── IMPLEMENTATION_SUMMARY.md # Implementation documentation
├── PROJECT_STRUCTURE.md      # Project structure documentation
├── start_eais.sh             # Startup script (Unix)
├── start_eais.bat            # Startup script (Windows)
└── COMPLETION_SUMMARY.txt    # Completion summary
```

## Core Components

### 1. Global Architecture Orchestrator
Located in `src/enhanced_enterprise_architecture_intelligence_system_e_eais/core/orchestrator.py`, this component coordinates all EAIS services and manages the flow of information between agents and tools.

### 2. Specialist Agents
Located in `src/enhanced_enterprise_architecture_intelligence_system_e_eais/agents/`, these are domain-specific AI agents:

- **Architecture Agent**: Generates core architecture designs and recommends patterns
- **Compliance Agent**: Handles regulatory compliance and evidence generation
- **Business Agent**: Performs TCO modeling and business impact analysis

### 3. Custom Tools
Located in `src/enhanced_enterprise_architecture_intelligence_system_e_eais/tools/`, these provide specialized capabilities:

- **Knowledge Graph Tool**: Interfaces with the semantic knowledge base
- **Artifact Generation Tool**: Creates production-ready artifacts (IaC, APIs, etc.)
- **Cost/Carbon Optimizer**: TCO modeling and sustainability analysis
- **Compliance Evidence Automator**: Generates audit-ready compliance artifacts
- **Architecture Evolution Engine**: Continuous optimization and drift detection
- **Dependency Mapper**: System interdependencies visualization
- **Secure Artifact Vault**: Tamper-proof storage with blockchain verification
- **Federated Learning Orchestrator**: Cross-org knowledge sharing

### 4. Data Layer
Located in `src/enhanced_enterprise_architecture_intelligence_system_e_eais/data/`, this contains data management components:

- **Knowledge Graph Engine**: Maintains the enterprise knowledge base

### 5. API Layer
Located in `src/enhanced_enterprise_architecture_intelligence_system_e_eais/api/`, this provides RESTful interfaces for external integration.

### 6. UI Layer
Located in `src/enhanced_enterprise_architecture_intelligence_system_e_eais/ui/`, this provides a modern web interface for interacting with the system.

## Design Principles

1. **Modularity**: Each component is loosely coupled and independently testable
2. **Extensibility**: New agents and tools can be added without modifying core logic
3. **Scalability**: Designed for horizontal scaling with Kubernetes
4. **Security**: Built-in zero-trust principles and compliance validation
5. **Observability**: Comprehensive logging and monitoring capabilities

## Development Guidelines

1. **Code Style**: Follow PEP 8 guidelines
2. **Documentation**: All public methods should have docstrings
3. **Testing**: Maintain >80% code coverage
4. **Dependencies**: Keep requirements.txt updated
5. **Versioning**: Follow semantic versioning

## Deployment Options

1. **Local Development**: Run directly with Python
2. **Containerized**: Use Docker for consistent environments
3. **Kubernetes**: Deploy in production clusters for scalability

## Testing Strategy

1. **Unit Testing**: Individual component testing
2. **Integration Testing**: Component interaction testing
3. **API Testing**: REST endpoint validation
4. **End-to-End Testing**: Complete workflow validation
5. **Performance Testing**: Load and stress testing