
"""
Global orchestrator for the Enhanced Enterprise Architecture Intelligence System (EAIS).
"""
from typing import Dict, Any, List, Optional
import os
from crewai import Crew, Task, Process
from enhanced_enterprise_architecture_intelligence_system_e_eais.agents.architecture_agent import ArchitectureAgent
from enhanced_enterprise_architecture_intelligence_system_e_eais.agents.compliance_agent import ComplianceAgent
from enhanced_enterprise_architecture_intelligence_system_e_eais.agents.business_agent import BusinessAgent


class EAISOrchestrator:
    """Global orchestrator that coordinates all EAIS services and manages information flow."""
    
    def __init__(self):
        """Initialize the orchestrator with all required agents."""
        self.architecture_agent = ArchitectureAgent().get_agent()
        self.compliance_agent = ComplianceAgent().get_agent()
        self.business_agent = BusinessAgent().get_agent()
        self.results = {}
    
    def execute_workflow(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the complete EAIS workflow using CrewAI.
        
        Args:
            inputs: Input parameters for the workflow
            
        Returns:
            Dict containing results from all agents
        """
        project_name = inputs.get('project_info', {}).get('name') if isinstance(inputs.get('project_info'), dict) else inputs.get('project_name', 'Untitled Project')
        
        # Define Tasks
        architecture_task = Task(
            description=(
                f"Design a comprehensive enterprise architecture for the project: {project_name}. "
                f"Business Objectives: {inputs.get('business_objectives')}. "
                f"Technical Requirements: {inputs.get('technical_requirements')}. "
                "Focus on scalability, performance, and modern patterns."
            ),
            expected_output="A detailed architecture design document including component breakdown and technology stack.",
            agent=self.architecture_agent
        )
        
        compliance_task = Task(
            description=(
                f"Assess the proposed architecture against the following compliance requirements: {inputs.get('compliance_requirements')}. "
                f"Regulatory Frameworks: {inputs.get('regulatory_frameworks')}. "
                "Identify gaps and provide implementation guidance for security controls."
            ),
            expected_output="A compliance assessment report with mapping to regulatory frameworks and required security controls.",
            agent=self.compliance_agent,
            context=[architecture_task]
        )
        
        business_task = Task(
            description=(
                "Perform a business impact analysis and TCO modeling for the designed architecture. "
                "Calculate projected ROI and identify cost optimization opportunities. "
                "Consider the project scale and timeline provided in the requirements."
            ),
            expected_output="A business impact analysis report including 5-year TCO projections and ROI calculation.",
            agent=self.business_agent,
            context=[architecture_task, compliance_task]
        )
        
        # Create Crew
        eais_crew = Crew(
            agents=[self.architecture_agent, self.compliance_agent, self.business_agent],
            tasks=[architecture_task, compliance_task, business_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute Workflow
        print("Running EAIS Crew...")
        result = eais_crew.kickoff()
        
        # Process results (CrewAI 0.28+ returns a CrewOutput object)
        self.results = {
            "raw_result": str(result),
            "architecture_result": architecture_task.output.raw if architecture_task.output else "No output",
            "compliance_result": compliance_task.output.raw if compliance_task.output else "No output",
            "business_result": business_task.output.raw if business_task.output else "No output",
            "summary": "EAIS workflow completed successfully using CrewAI"
        }
        
        print("EAIS workflow execution completed.")
        return self.results


# Example usage
if __name__ == "__main__":
    # Ensure API key is set or handled
    if not os.environ.get("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY not found in environment.")
        
    orchestrator = EAISOrchestrator()
    
    # Example inputs
    inputs = {
        "project_info": {"name": "Test Project"},
        "business_objectives": ["Reduce operational costs by 20%", "Improve system scalability"],
        "technical_requirements": ["High availability", "Microsecond latency", "Cloud-native deployment"],
        "compliance_requirements": ["GDPR", "SOC2", "PCI-DSS"],
        "regulatory_frameworks": ["GDPR", "SOC2"]
    }
    
    # Execute the workflow
    results = orchestrator.execute_workflow(inputs)
    print("Final results summary:", results["summary"])
