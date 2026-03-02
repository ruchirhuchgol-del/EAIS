# Enhanced Enterprise Architecture Intelligence System (EAIS)

An AI-powered platform that transforms product requirements into production-ready, enterprise-grade system architectures with comprehensive artifacts and industry-grade web interfaces.

## Overview

EAIS reduces architecture design time from weeks to minutes while ensuring compliance, security, and business alignment across global organizations. The system now features multiple user interfaces including a modern Streamlit web application for enhanced user experience.

## Features

- **Multi-Cloud Architecture Design**: Generate vendor-agnostic and cloud-specific architectures
- **Automated Artifact Generation**: Create production-ready IaC, API specs, CI/CD pipelines
- **Compliance Automation**: Map designs to 50+ regulatory frameworks with automated evidence
- **Business Impact Optimization**: TCO modeling, risk assessment, and sustainability scoring
- **Knowledge Management**: Enterprise knowledge graph with NLP querying
- **Industry-Grade UI**: Modern Streamlit interface with executive dashboards and real-time analytics
- **Multi-Interface Support**: Choose from Streamlit UI, Flask API, React frontend, or CLI
- **Role-Based Access Control**: Secure authentication with administrator, architect, analyst, and viewer roles

## User Interfaces

### 🚀 Streamlit UI (Recommended)
Modern, industry-grade web interface with:
- Executive dashboards with real-time metrics
- Interactive architecture generation
- Comprehensive compliance assessment
- Business impact analysis and TCO modeling
- Knowledge graph visualization
- Advanced reporting capabilities
- Role-based access control

### 🌐 Next.js Integration Portal
Enterprise-grade platform featuring:
- Next.js 15+ with Tailwind CSS and Shadcn UI
- Prisma ORM with SQLite (PostgreSQL compatible)
- Unified AI orchestration (proxied to Python backend)
- Comprehensive user management and session control
- Professional executive reporting and artifact storage

### 🔧 Flask API
Scalable backend interface:
- RESTful endpoints for architecture generation
- Single source of truth for AI agent logic
- High-performance orchestrator gateway

### 💻 Command Line Interface
Direct CLI access for:
- Automated scripting
- Batch processing
- CI/CD integration

## Project Structure
https://github.com/ruchirhuchgol-del/EAIS.git

```
src/enhanced_enterprise_architecture_intelligence_system_e_eais/
├── agents/              # Specialist AI agents
├── api/                 # REST API interface
├── config/              # Configuration management
├── core/                # Core orchestrator
├── data/                # Data layer components
├── tools/               # Custom tools
├── ui_streamlit/        # Modern Streamlit web interface
├── utils/               # Utility functions
├── app.py              # Main application entry point
├── init.py             # System initialization
└── __init__.py         # Package initialization
```

## Quick Start

### Option 1: Streamlit UI (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Start Streamlit application (uses port fallback strategy)
python run_streamlit_app.py
```

Access the application at: **http://localhost:8503** (or first available port: 8501, 8502, 8503)

**Demo Credentials:**
- **Administrator**: admin@eais.com / eais_admin_2024 (Full system access)
- **Enterprise Architect**: architect@eais.com / architect_2024 (Architecture, compliance, reports, dashboard)
- **Business Analyst**: analyst@eais.com / analyst_2024 (Business analysis, reports, dashboard)
- **Viewer**: viewer@eais.com / viewer_2024 (Reports and dashboards - read-only)

### Option 2: Docker Compose (All Services)

```bash
# Start all services with Docker
docker-compose up --build
```

**Access Points:**
- **Streamlit UI**: http://localhost:8503
- **Next.js Portal**: http://localhost:3000
- **Flask API**: http://localhost:8000

## Demo Video

The project includes a comprehensive demo video: **EAIS_DEMO.mp4**.

Due to its large size (150MB), it is managed via **Git LFS**. 

> [!NOTE]
> GitHub's web interface may not preview the video directly. To view it, please **download** the file from the GitHub UI or clone the repository with [Git LFS](https://git-lfs.github.com/) installed.

### Option 3: Easy Startup Scripts

**Windows:**
```cmd
start_eais.bat
```

**Linux/Mac:**
```bash
./start_eais.sh
```

Choose your preferred interface when prompted.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd EAIS_v2
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Run the application:**
   ```bash
   python run_streamlit_app.py
   ```

## Streamlit UI Features

### 🏠 Executive Dashboard
- Real-time KPIs and metrics
- Architecture analytics
- Compliance overview
- Financial performance indicators
- System health monitoring

### 🏢 Architecture Generator
- Interactive requirement forms
- AI-powered architecture generation
- Real-time progress tracking
- Comprehensive result visualization
- Artifact generation and download

### 🛡️ Compliance & Security
- Framework assessment tools
- Security analysis dashboard
- Evidence generation automation
- Compliance reporting

### 💼 Business Analysis
- TCO modeling and calculation
- ROI analysis and projections
- Cost optimization recommendations
- Business impact assessment

### 🧠 Knowledge Graph
- Semantic search capabilities
- Visual knowledge exploration
- Architecture pattern library
- Best practices repository

### 📈 Reports & Analytics
- Executive report generation
- Custom analytics dashboards
- Data export capabilities
- Automated reporting

### ⚙️ Settings
- User profile management
- System configuration
- Notification preferences
- Security settings

## User Roles & Permissions

- **Administrator**: Full system access and user management (all permissions)
- **Enterprise Architect**: Architecture design, compliance assessment, reports, and dashboard access
- **Business Analyst**: Business impact analysis, reports, and dashboard access
- **Viewer**: Read-only access to reports and dashboards

## API Usage

Start the server and send a POST request to `/architecture` with your requirements:

```json
{
  "business_objectives": ["reduce costs", "improve scalability"],
  "technical_requirements": ["high availability", "microsecond latency"],
  "compliance_requirements": ["GDPR", "SOC2"]
}
```

## Architecture

EAIS follows a multi-agent architecture where specialized agents handle different aspects of enterprise architecture design:

1. **Global Architecture Orchestrator**: Coordinates all services
2. **Specialist Agents**: Handle specific domains (architecture, compliance, business)
3. **Custom Tools**: Provide specialized capabilities (knowledge graph, artifact generation)
4. **Data Layer**: Knowledge graph engine and secure artifact vault

## Documentation

- [README.md](README.md) - Main project overview and usage instructions
- [PROFESSIONAL_USAGE_GUIDE.md](PROFESSIONAL_USAGE_GUIDE.md) - Detailed guide on daily usage scenarios and time-saving benefits
- [ERRORS_AND_SOLUTIONS.md](ERRORS_AND_SOLUTIONS.md) - Detailed documentation of errors encountered during development and their solutions
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Technical implementation details
- [STREAMLIT_IMPLEMENTATION_SUMMARY.md](STREAMLIT_IMPLEMENTATION_SUMMARY.md) - Streamlit UI implementation details
- [COMPLETION_SUMMARY.md](COMPLETION_SUMMARY.md) - Project completion summary
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Detailed project structure documentation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the terms specified in the LICENSE file.