"""
Helper utilities for EAIS Streamlit application.
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import yaml
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import base64
from io import BytesIO
import plotly.graph_objects as go
import plotly.express as px

def load_css(file_path: str):
    """Load custom CSS from file"""
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found: {file_path}")

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format currency amount with proper formatting"""
    if currency == "USD":
        return f"${amount:,.2f}"
    elif currency == "EUR":
        return f"€{amount:,.2f}"
    elif currency == "GBP":
        return f"£{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"

def format_percentage(value: float, decimals: int = 1) -> str:
    """Format percentage with proper display"""
    return f"{value:.{decimals}f}%"

def format_large_number(num: float) -> str:
    """Format large numbers with appropriate suffixes"""
    if num >= 1_000_000_000:
        return f"{num/1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num/1_000:.1f}K"
    else:
        return f"{num:.0f}"

def create_download_link(data: bytes, filename: str, link_text: str) -> str:
    """Create a download link for data"""
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/octet-stream;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

def export_to_excel(dataframes: Dict[str, pd.DataFrame], filename: str = "eais_export.xlsx"):
    """Export multiple dataframes to Excel with different sheets"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        for sheet_name, df in dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    output.seek(0)
    return output.getvalue()

def create_metric_card(title: str, value: str, delta: str = None, help_text: str = None):
    """Create a styled metric card"""
    delta_html = ""
    if delta:
        delta_color = "green" if delta.startswith("↗") else "red" if delta.startswith("↘") else "blue"
        delta_html = f'<div style="color: {delta_color}; font-size: 0.8rem; margin-top: 5px;">{delta}</div>'
    
    help_html = ""
    if help_text:
        help_html = f'<div style="color: #666; font-size: 0.7rem; margin-top: 5px;">{help_text}</div>'
    
    card_html = f"""
    <div style="
        background: white;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    ">
        <div style="color: #666; font-size: 0.8rem; font-weight: 500;">{title}</div>
        <div style="color: #333; font-size: 1.8rem; font-weight: bold; margin: 0.5rem 0;">{value}</div>
        {delta_html}
        {help_html}
    </div>
    """
    return card_html

def create_status_badge(status: str, color: str = None) -> str:
    """Create a colored status badge"""
    colors = {
        'success': '#28a745',
        'warning': '#ffc107',
        'error': '#dc3545',
        'info': '#17a2b8',
        'primary': '#007bff'
    }
    
    if color is None:
        if status.lower() in ['active', 'online', 'healthy', 'completed', 'approved']:
            color = colors['success']
        elif status.lower() in ['warning', 'pending', 'in_progress']:
            color = colors['warning']
        elif status.lower() in ['error', 'failed', 'offline', 'rejected']:
            color = colors['error']
        else:
            color = colors['info']
    elif color in colors:
        color = colors[color]
    
    badge_html = f"""
    <span style="
        background-color: {color};
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
    ">{status}</span>
    """
    return badge_html

def create_progress_bar(percentage: float, color: str = "#2E86AB", height: str = "20px") -> str:
    """Create a custom progress bar"""
    progress_html = f"""
    <div style="
        background-color: #e9ecef;
        border-radius: 10px;
        height: {height};
        overflow: hidden;
    ">
        <div style="
            background-color: {color};
            height: 100%;
            width: {percentage}%;
            border-radius: 10px;
            transition: width 0.3s ease;
        "></div>
    </div>
    <div style="text-align: center; margin-top: 5px; font-size: 0.8rem; color: #666;">
        {percentage:.1f}%
    </div>
    """
    return progress_html

def generate_sample_architecture_data() -> Dict[str, Any]:
    """Generate sample architecture data for demonstrations"""
    return {
        'architecture_id': f"ARCH_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'timestamp': datetime.now().isoformat(),
        'business_objectives': [
            "Reduce operational costs by 20%",
            "Improve system scalability",
            "Enhance security posture",
            "Enable multi-cloud deployment"
        ],
        'technical_requirements': [
            "High availability (99.9% uptime)",
            "Microsecond latency",
            "Cloud-native deployment",
            "Microservices architecture",
            "Container orchestration"
        ],
        'compliance_requirements': [
            "GDPR", "SOC2", "PCI-DSS", "ISO 27001"
        ],
        'estimated_tco': {
            'year_1': 850000,
            'year_2': 920000,
            'year_3': 980000,
            'year_4': 1050000,
            'year_5': 1120000,
            'total': 4920000
        },
        'compliance_score': 94.5,
        'security_score': 92.8,
        'scalability_score': 96.2,
        'cost_optimization_score': 88.7
    }

def generate_compliance_framework_data() -> List[Dict[str, Any]]:
    """Generate sample compliance framework data"""
    frameworks = [
        {
            'name': 'GDPR',
            'category': 'Data Protection',
            'coverage': 98.5,
            'status': 'Compliant',
            'controls_implemented': 47,
            'controls_total': 48,
            'last_assessment': '2024-01-15'
        },
        {
            'name': 'SOC2 Type II',
            'category': 'Security',
            'coverage': 95.2,
            'status': 'Compliant',
            'controls_implemented': 78,
            'controls_total': 82,
            'last_assessment': '2024-01-10'
        },
        {
            'name': 'PCI-DSS',
            'category': 'Payment Security',
            'coverage': 92.8,
            'status': 'Compliant',
            'controls_implemented': 334,
            'controls_total': 360,
            'last_assessment': '2024-01-08'
        },
        {
            'name': 'ISO 27001',
            'category': 'Information Security',
            'coverage': 89.4,
            'status': 'In Progress',
            'controls_implemented': 98,
            'controls_total': 114,
            'last_assessment': '2024-01-12'
        },
        {
            'name': 'HIPAA',
            'category': 'Healthcare',
            'coverage': 96.1,
            'status': 'Compliant',
            'controls_implemented': 67,
            'controls_total': 69,
            'last_assessment': '2024-01-14'
        }
    ]
    return frameworks

def generate_tco_analysis_data() -> Dict[str, Any]:
    """Generate sample TCO analysis data"""
    return {
        'initial_investment': 2500000,
        'annual_operating_costs': {
            'infrastructure': 450000,
            'licenses': 180000,
            'personnel': 650000,
            'maintenance': 120000,
            'training': 80000
        },
        'cost_savings': {
            'operational_efficiency': 320000,
            'reduced_downtime': 180000,
            'automation': 240000,
            'cloud_optimization': 160000
        },
        'risk_mitigation_value': 850000,
        'projected_roi': {
            'year_1': -8.2,
            'year_2': 12.4,
            'year_3': 18.7,
            'year_4': 22.1,
            'year_5': 24.8
        },
        'payback_period_months': 28
    }

def validate_json_input(json_string: str) -> Tuple[bool, Any, str]:
    """Validate JSON input and return parsed data"""
    try:
        data = json.loads(json_string)
        return True, data, "Valid JSON"
    except json.JSONDecodeError as e:
        return False, None, f"Invalid JSON: {str(e)}"

def validate_yaml_input(yaml_string: str) -> Tuple[bool, Any, str]:
    """Validate YAML input and return parsed data"""
    try:
        data = yaml.safe_load(yaml_string)
        return True, data, "Valid YAML"
    except yaml.YAMLError as e:
        return False, None, f"Invalid YAML: {str(e)}"

def create_timeline_data(events: List[Dict[str, str]]) -> pd.DataFrame:
    """Create timeline data for Gantt charts"""
    df = pd.DataFrame(events)
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])
    df['duration'] = (df['end'] - df['start']).dt.days
    return df

def calculate_business_metrics(data: Dict[str, Any]) -> Dict[str, float]:
    """Calculate various business metrics from input data"""
    metrics = {}
    
    # Calculate ROI
    if 'investment' in data and 'annual_savings' in data:
        metrics['roi'] = (data['annual_savings'] / data['investment']) * 100
    
    # Calculate payback period
    if 'investment' in data and 'monthly_savings' in data:
        metrics['payback_months'] = data['investment'] / data['monthly_savings']
    
    # Calculate efficiency gain
    if 'current_cost' in data and 'projected_cost' in data:
        metrics['efficiency_gain'] = ((data['current_cost'] - data['projected_cost']) / data['current_cost']) * 100
    
    return metrics

def format_architecture_summary(result: str) -> Dict[str, str]:
    """Format architecture analysis result into structured sections"""
    sections = {
        'executive_summary': '',
        'technical_architecture': '',
        'compliance_analysis': '',
        'business_impact': '',
        'recommendations': ''
    }
    
    # Basic parsing of result text
    lines = result.split('\n')
    current_section = 'executive_summary'
    
    for line in lines:
        line_lower = line.lower().strip()
        if 'technical' in line_lower and 'architecture' in line_lower:
            current_section = 'technical_architecture'
        elif 'compliance' in line_lower:
            current_section = 'compliance_analysis'
        elif 'business' in line_lower and 'impact' in line_lower:
            current_section = 'business_impact'
        elif 'recommendation' in line_lower:
            current_section = 'recommendations'
        else:
            sections[current_section] += line + '\n'
    
    return sections

def create_architecture_diagram_placeholder() -> str:
    """Create a placeholder for architecture diagrams"""
    return """
    ```mermaid
    graph TB
        A[User Interface] --> B[API Gateway]
        B --> C[Microservices Layer]
        C --> D[Business Logic]
        C --> E[Data Access Layer]
        D --> F[External Services]
        E --> G[Database Cluster]
        E --> H[Cache Layer]
        
        I[Monitoring] --> A
        I --> B
        I --> C
        
        J[Security Layer] --> A
        J --> B
        J --> C
    ```
    """

class DataProcessor:
    """Data processing utilities for EAIS"""
    
    @staticmethod
    def aggregate_metrics(data: List[Dict[str, Any]], group_by: str, metric: str) -> pd.DataFrame:
        """Aggregate metrics by grouping field"""
        df = pd.DataFrame(data)
        return df.groupby(group_by)[metric].agg(['mean', 'sum', 'count']).reset_index()
    
    @staticmethod
    def calculate_trend(values: List[float], periods: int = 5) -> str:
        """Calculate trend direction from values"""
        if len(values) < 2:
            return "stable"
        
        recent_avg = np.mean(values[-periods:]) if len(values) >= periods else np.mean(values)
        older_avg = np.mean(values[:-periods]) if len(values) >= periods else np.mean(values[:-1])
        
        if recent_avg > older_avg * 1.05:
            return "increasing"
        elif recent_avg < older_avg * 0.95:
            return "decreasing"
        else:
            return "stable"
    
    @staticmethod
    def detect_anomalies(data: List[float], threshold: float = 2.0) -> List[int]:
        """Detect anomalies in data using z-score"""
        if len(data) < 3:
            return []
        
        mean = np.mean(data)
        std = np.std(data)
        z_scores = [(x - mean) / std for x in data]
        
        return [i for i, z in enumerate(z_scores) if abs(z) > threshold]