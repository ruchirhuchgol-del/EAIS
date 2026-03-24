🏛️ Enhanced Enterprise Architecture Intelligence System (EAIS)
Transform Product Requirements into Production-Grade Architectures in Minutes.

An AI-powered platform leveraging Multi-Agent Orchestration to bridge the gap between business vision and technical implementation.

PythonStreamlitDockerLicenseGitHub Stars

🎯 Demo Video • 🚀 Quick Start • 🤖 Architecture • 📚 Documentation

📝 The Problem vs. The Solution
Traditional Enterprise Architecture	EAIS Approach
🐢 Weeks of manual design and diagramming	⚡ Minutes of AI generation based on requirements
🧩 Siloed tools for diagramming, compliance, and code	🌐 Unified Platform generating diagrams, IaC, and reports
📉 Human error in regulatory compliance checks	🛡️ Automated Compliance mapped to 50+ global frameworks
🙈 Static documents that rot over time	🧠 Living Knowledge Graph with NLP querying
✨ Core Capabilities
🤖 Agentic Orchestration: A team of specialist AI agents (Architect, Compliance Officer, Business Analyst) collaborates to generate holistic designs.
🌐 Multi-Cloud Agility: Generates vendor-agnostic designs or specific blueprints for AWS, Azure, and GCP.
⚙️ Production-Ready Artifacts: Don't just get a diagram—get Terraform scripts, Kubernetes manifests, CI/CD pipelines, and OpenAPI specs instantly.
📊 Business Impact Modeling: Automated TCO calculation, ROI projection, and sustainability scoring.
🔐 Enterprise-Grade Security: RBAC implementation with granular permissions for Admins, Architects, and Analysts.
🖥️ User Interfaces
EAIS provides a flexible multi-interface experience to suit different user needs:

Interface	Tech Stack	Best For
✨ Streamlit UI (Recommended)	Streamlit, Plotly	Interactive exploration, Executive Dashboards, Rapid Prototyping
🌐 Integration Portal	Next.js 15, Tailwind, Prisma	Enterprise deployment, User Management, Scalable Web App
🔌 Headless API	Flask, REST	CI/CD Integration, Custom Frontends, Batch Processing
💻 CLI	Python, Rich	Scripting, Automation Pipelines, Local Development
🚀 Quick Start
Get the system up and running in under 5 minutes.

Prerequisites
Python 3.9+
OpenAI API Key
Method 1: Docker Compose (All Services) 🐳
The easiest way to spin up the complete ecosystem (Streamlit + Next.js + Flask).

docker-compose up --build
Streamlit UI: http://localhost:8503
Next.js Portal: http://localhost:3000
Flask API: http://localhost:8000
Method 2: Native Python (Streamlit) 🐍
bash

# 1. Clone the repository
git clone https://github.com/ruchirhuchgol-del/EAIS.git
cd EAIS

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your OpenAI Key
export OPENAI_API_KEY="your-key-here"

# 4. Run the application
python run_streamlit_app.py
🔐 Default Login Credentials (Click to expand)
🤖 AI Architecture
EAIS leverages a Multi-Agent System (MAS) where specialized agents handle specific domains under the coordination of a Global Orchestrator.

graph TD
    User[User Input / Requirements] --> Orchestrator[Global Architecture Orchestrator]
    
    subgraph "AI Agent Swarm"
        Orchestrator --> ArchAgent[Architecture Agent]
        Orchestrator --> CompAgent[Compliance Agent]
        Orchestrator --> BizAgent[Business Agent]
    end
    
    subgraph "Core Tools & Memory"
        ArchAgent --> KG[Knowledge Graph Engine]
        CompAgent --> RegDB[Regulatory Framework DB]
        BizAgent --> TCO[TCO Calculator]
    end
    
    ArchAgent & CompAgent & BizAgent --> ArtifactGen[Artifact Generation Engine]
    
    ArtifactGen --> Output[Production-Ready Artifacts]
    
    Output --> |IaC / Diagrams| User


    The Agent Swarm
Global Orchestrator: The "manager" agent that decomposes user requirements and routes tasks to specialists.
Architecture Agent: Designs system topologies, selects tech stacks, and ensures scalability.
Compliance Agent: Maps designs against GDPR, SOC2, HIPAA, etc., generating audit trails automatically.
Business Agent: Calculates Total Cost of Ownership (TCO) and aligns tech decisions with business KPIs.
📸 Feature Showcase
Executive Dashboard: Real-time KPIs, compliance health, and cost metrics at a glance.
Interactive Architecture Generation: Input natural language requirements (e.g., "Highly scalable e-commerce platform for black friday traffic").
Knowledge Graph Visualization: visually explore relationships between system components and regulatory controls.
Automated Artifact Export: Download generated Terraform files, CI/CD pipelines, and PDF reports with one click.
📽️ Demo Video
The project includes a comprehensive demo video (EAIS_DEMO.mp4 - 150MB).

Note: Due to file size, this is managed via Git LFS.
Download the video directly from the repository to see the system in action.

📂 Project Structure
The repository is organized for modularity and scalability:
text

src/enhanced_enterprise_architecture_intelligence_system_e_eais/
├── 🤖 agents/              # Specialist AI Agent Definitions
├── 🌐 api/                 # Flask REST API Endpoints
├── ⚙️ core/                # Orchestrator & Main Logic
├── 🧠 data/                # Knowledge Graph & Data Models
├── 🎨 ui_streamlit/        # Streamlit Frontend Code
├── 🛠️ tools/               # Custom Tools (e.g., Artifact Generators)
└── 📄 app.py               # Main Application Entry Point
📖 Deep Dive: Documentation Index
🤝 Contributing
We welcome contributions to enhance the intelligence and capabilities of EAIS.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
