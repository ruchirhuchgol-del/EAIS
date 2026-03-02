"""
Visualization utilities for EAIS Streamlit application.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
from typing import Dict, List, Any, Optional, Tuple
import networkx as nx
from datetime import datetime, timedelta

# EAIS color palette
EAIS_COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'success': '#28a745',
    'warning': '#ffc107',
    'danger': '#dc3545',
    'info': '#17a2b8',
    'light': '#f8f9fa',
    'dark': '#343a40',
    'muted': '#6c757d'
}

EAIS_PALETTE = [
    '#2E86AB', '#A23B72', '#F18F01', '#C73E1D', 
    '#592E83', '#1B998B', '#84DCCF', '#95E1D3'
]

def create_executive_dashboard_charts() -> Dict[str, go.Figure]:
    """Create charts for executive dashboard"""
    charts = {}
    
    # 1. Architecture Projects Over Time
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    projects = np.cumsum(np.random.poisson(8, len(dates)))
    
    fig_projects = go.Figure()
    fig_projects.add_trace(go.Scatter(
        x=dates,
        y=projects,
        mode='lines+markers',
        line=dict(color=EAIS_COLORS['primary'], width=3),
        marker=dict(size=8),
        name='Architecture Projects'
    ))
    fig_projects.update_layout(
        title="Architecture Projects Delivered",
        xaxis_title="Month",
        yaxis_title="Cumulative Projects",
        template="plotly_white",
        height=300
    )
    charts['projects_timeline'] = fig_projects
    
    # 2. Compliance Score Distribution
    frameworks = ['GDPR', 'SOC2', 'PCI-DSS', 'ISO 27001', 'HIPAA', 'NIST', 'FedRAMP']
    scores = [98.5, 95.2, 92.8, 89.4, 96.1, 91.7, 88.9]
    
    fig_compliance = go.Figure(data=[
        go.Bar(
            x=frameworks,
            y=scores,
            marker_color=EAIS_PALETTE,
            text=[f"{score}%" for score in scores],
            textposition='auto',
        )
    ])
    fig_compliance.update_layout(
        title="Compliance Framework Scores",
        xaxis_title="Framework",
        yaxis_title="Compliance Score (%)",
        template="plotly_white",
        height=300,
        yaxis=dict(range=[80, 100])
    )
    charts['compliance_scores'] = fig_compliance
    
    # 3. TCO Analysis Donut Chart
    tco_categories = ['Infrastructure', 'Personnel', 'Licenses', 'Maintenance', 'Training']
    tco_values = [450000, 650000, 180000, 120000, 80000]
    
    fig_tco = go.Figure(data=[go.Pie(
        labels=tco_categories,
        values=tco_values,
        hole=0.5,
        marker_colors=EAIS_PALETTE,
        textinfo='label+percent',
        textfont_size=12
    )])
    fig_tco.update_layout(
        title="Total Cost of Ownership Breakdown",
        template="plotly_white",
        height=300,
        annotations=[dict(text='TCO<br>$1.48M', x=0.5, y=0.5, font_size=16, showarrow=False)]
    )
    charts['tco_breakdown'] = fig_tco
    
    # 4. ROI Projection
    years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
    roi_values = [-8.2, 12.4, 18.7, 22.1, 24.8]
    
    fig_roi = go.Figure()
    fig_roi.add_trace(go.Bar(
        x=years,
        y=roi_values,
        marker_color=[EAIS_COLORS['danger'] if x < 0 else EAIS_COLORS['success'] for x in roi_values],
        text=[f"{val}%" for val in roi_values],
        textposition='auto'
    ))
    fig_roi.update_layout(
        title="ROI Projection Over 5 Years",
        xaxis_title="Year",
        yaxis_title="ROI (%)",
        template="plotly_white",
        height=300
    )
    charts['roi_projection'] = fig_roi
    
    return charts

def create_architecture_quality_radar() -> go.Figure:
    """Create radar chart for architecture quality metrics"""
    metrics = ['Security', 'Scalability', 'Performance', 'Maintainability', 
              'Cost Efficiency', 'Compliance', 'Innovation', 'Reliability']
    values = [92.8, 96.2, 89.5, 87.3, 88.7, 94.5, 82.1, 95.8]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Close the polygon
        theta=metrics + [metrics[0]],
        fill='toself',
        fillcolor=f'rgba({int(EAIS_COLORS["primary"][1:3], 16)}, {int(EAIS_COLORS["primary"][3:5], 16)}, {int(EAIS_COLORS["primary"][5:7], 16)}, 0.3)',
        line=dict(color=EAIS_COLORS['primary'], width=2),
        marker=dict(size=8, color=EAIS_COLORS['primary']),
        name='Architecture Quality'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                ticksuffix='%'
            )
        ),
        title="Architecture Quality Assessment",
        template="plotly_white",
        height=400
    )
    
    return fig

def create_compliance_heatmap(frameworks_data: List[Dict]) -> go.Figure:
    """Create compliance heatmap"""
    df = pd.DataFrame(frameworks_data)
    
    # Create matrix data
    categories = df['category'].unique()
    frameworks = df['name'].unique()
    
    z_data = []
    for cat in categories:
        row = []
        for fw in frameworks:
            match = df[(df['category'] == cat) & (df['name'] == fw)]
            if not match.empty:
                row.append(match.iloc[0]['coverage'])
            else:
                row.append(0)
        z_data.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=z_data,
        x=frameworks,
        y=categories,
        colorscale='RdYlGn',
        text=[[f"{val:.1f}%" for val in row] for row in z_data],
        texttemplate="%{text}",
        textfont={"size": 12},
        colorbar=dict(title="Coverage %")
    ))
    
    fig.update_layout(
        title="Compliance Framework Coverage Heatmap",
        xaxis_title="Framework",
        yaxis_title="Category",
        template="plotly_white",
        height=400
    )
    
    return fig

def create_cost_waterfall_chart() -> go.Figure:
    """Create waterfall chart for cost analysis"""
    measures = ['Initial Cost', 'Infrastructure', 'Personnel', 'Licenses', 
               'Savings', 'Optimization', 'Net Cost']
    values = [2500000, 450000, 650000, 180000, -320000, -240000, 0]
    
    # Calculate cumulative values for waterfall
    cumulative = [values[0]]
    for i in range(1, len(values) - 1):
        cumulative.append(cumulative[-1] + values[i])
    cumulative.append(sum(values[:-1]))
    
    fig = go.Figure()
    
    # Add bars
    colors = [EAIS_COLORS['primary']] + [EAIS_COLORS['danger'] if v > 0 else EAIS_COLORS['success'] for v in values[1:-1]] + [EAIS_COLORS['info']]
    
    fig.add_trace(go.Waterfall(
        name="Cost Analysis",
        orientation="v",
        measure=["absolute"] + ["relative"] * (len(measures) - 2) + ["total"],
        x=measures,
        textposition="outside",
        text=[f"${v/1000:.0f}K" for v in values],
        y=values,
        connector={"line": {"color": "rgb(63, 63, 63)"}},
    ))
    
    fig.update_layout(
        title="5-Year TCO Waterfall Analysis",
        template="plotly_white",
        height=400,
        yaxis_title="Cost (USD)"
    )
    
    return fig

def create_architecture_network_graph() -> Dict[str, Any]:
    """Create network graph data for architecture visualization"""
    # Create sample architecture network
    G = nx.Graph()
    
    # Add nodes with categories
    nodes = [
        ('API Gateway', {'category': 'Gateway', 'size': 30}),
        ('Auth Service', {'category': 'Security', 'size': 20}),
        ('User Service', {'category': 'Business', 'size': 25}),
        ('Order Service', {'category': 'Business', 'size': 25}),
        ('Payment Service', {'category': 'Business', 'size': 20}),
        ('Database', {'category': 'Data', 'size': 35}),
        ('Cache', {'category': 'Data', 'size': 15}),
        ('Message Queue', {'category': 'Infrastructure', 'size': 20}),
        ('Load Balancer', {'category': 'Infrastructure', 'size': 25}),
        ('Monitoring', {'category': 'Operations', 'size': 15})
    ]
    
    G.add_nodes_from(nodes)
    
    # Add edges
    edges = [
        ('Load Balancer', 'API Gateway'),
        ('API Gateway', 'Auth Service'),
        ('API Gateway', 'User Service'),
        ('API Gateway', 'Order Service'),
        ('API Gateway', 'Payment Service'),
        ('User Service', 'Database'),
        ('Order Service', 'Database'),
        ('Payment Service', 'Database'),
        ('User Service', 'Cache'),
        ('Order Service', 'Message Queue'),
        ('Payment Service', 'Message Queue'),
        ('Monitoring', 'API Gateway'),
        ('Monitoring', 'Database')
    ]
    
    G.add_edges_from(edges)
    
    # Calculate layout
    pos = nx.spring_layout(G, k=3, iterations=50)
    
    # Prepare data for visualization
    node_data = []
    edge_data = []
    
    category_colors = {
        'Gateway': EAIS_COLORS['primary'],
        'Security': EAIS_COLORS['danger'],
        'Business': EAIS_COLORS['success'],
        'Data': EAIS_COLORS['warning'],
        'Infrastructure': EAIS_COLORS['info'],
        'Operations': EAIS_COLORS['muted']
    }
    
    for node in G.nodes():
        x, y = pos[node]
        node_info = G.nodes[node]
        node_data.append({
            'id': node,
            'x': x,
            'y': y,
            'size': node_info.get('size', 20),
            'color': category_colors.get(node_info.get('category', 'Infrastructure'), EAIS_COLORS['muted']),
            'category': node_info.get('category', 'Infrastructure')
        })
    
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_data.append({
            'x0': x0, 'y0': y0,
            'x1': x1, 'y1': y1,
            'source': edge[0],
            'target': edge[1]
        })
    
    return {'nodes': node_data, 'edges': edge_data}

def create_gantt_chart(timeline_data: List[Dict]) -> go.Figure:
    """Create Gantt chart for project timeline"""
    df = pd.DataFrame(timeline_data)
    
    fig = px.timeline(df, x_start="start", x_end="end", y="task", color="category",
                     title="Architecture Implementation Timeline")
    
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        template="plotly_white",
        height=400,
        xaxis_title="Timeline",
        yaxis_title="Tasks"
    )
    
    return fig

def create_risk_matrix() -> go.Figure:
    """Create risk assessment matrix"""
    risks = [
        {'name': 'Security Breach', 'probability': 0.2, 'impact': 0.9, 'severity': 'High'},
        {'name': 'Performance Issues', 'probability': 0.4, 'impact': 0.6, 'severity': 'Medium'},
        {'name': 'Compliance Failure', 'probability': 0.1, 'impact': 0.8, 'severity': 'High'},
        {'name': 'Budget Overrun', 'probability': 0.3, 'impact': 0.5, 'severity': 'Medium'},
        {'name': 'Vendor Lock-in', 'probability': 0.5, 'impact': 0.4, 'severity': 'Low'},
        {'name': 'Data Loss', 'probability': 0.1, 'impact': 0.9, 'severity': 'High'},
        {'name': 'Integration Issues', 'probability': 0.6, 'impact': 0.3, 'severity': 'Low'},
        {'name': 'Scalability Problems', 'probability': 0.3, 'impact': 0.7, 'severity': 'Medium'}
    ]
    
    df = pd.DataFrame(risks)
    
    color_map = {'Low': EAIS_COLORS['success'], 'Medium': EAIS_COLORS['warning'], 'High': EAIS_COLORS['danger']}
    
    fig = px.scatter(df, x='probability', y='impact', color='severity', 
                    size=[30]*len(df), hover_name='name',
                    color_discrete_map=color_map,
                    title="Risk Assessment Matrix")
    
    fig.update_layout(
        template="plotly_white",
        height=400,
        xaxis_title="Probability",
        yaxis_title="Impact",
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[0, 1])
    )
    
    # Add quadrant lines
    fig.add_hline(y=0.5, line_dash="dash", line_color="gray", opacity=0.5)
    fig.add_vline(x=0.5, line_dash="dash", line_color="gray", opacity=0.5)
    
    return fig

def create_technology_stack_sunburst() -> go.Figure:
    """Create sunburst chart for technology stack"""
    data = {
        'ids': [
            'Infrastructure', 'Infrastructure - Cloud', 'Infrastructure - Container', 'Infrastructure - Network',
            'Backend', 'Backend - API', 'Backend - Database', 'Backend - Cache',
            'Frontend', 'Frontend - Web', 'Frontend - Mobile',
            'Security', 'Security - Auth', 'Security - Encryption', 'Security - Monitoring'
        ],
        'labels': [
            'Infrastructure', 'Cloud (AWS)', 'Containers (K8s)', 'Networking (CDN)',
            'Backend', 'API (REST)', 'Database (PostgreSQL)', 'Cache (Redis)',
            'Frontend', 'Web (React)', 'Mobile (React Native)',
            'Security', 'Auth (OAuth2)', 'Encryption (TLS)', 'Monitoring (Grafana)'
        ],
        'parents': [
            '', 'Infrastructure', 'Infrastructure', 'Infrastructure',
            '', 'Backend', 'Backend', 'Backend',
            '', 'Frontend', 'Frontend',
            '', 'Security', 'Security', 'Security'
        ],
        'values': [
            1, 0.4, 0.3, 0.3,
            1, 0.4, 0.4, 0.2,
            1, 0.7, 0.3,
            1, 0.4, 0.3, 0.3
        ]
    }
    
    fig = go.Figure(go.Sunburst(
        ids=data['ids'],
        labels=data['labels'],
        parents=data['parents'],
        values=data['values'],
        branchvalues="total",
    ))
    
    fig.update_layout(
        title="Technology Stack Architecture",
        template="plotly_white",
        height=500
    )
    
    return fig

def create_performance_metrics_dashboard() -> Dict[str, go.Figure]:
    """Create performance metrics dashboard charts"""
    charts = {}
    
    # Response time trend
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    response_times = np.random.normal(150, 20, 30)
    
    fig_response = go.Figure()
    fig_response.add_trace(go.Scatter(
        x=dates,
        y=response_times,
        mode='lines+markers',
        line=dict(color=EAIS_COLORS['primary']),
        name='Response Time'
    ))
    fig_response.update_layout(
        title="API Response Time Trend",
        xaxis_title="Date",
        yaxis_title="Response Time (ms)",
        template="plotly_white",
        height=300
    )
    charts['response_time'] = fig_response
    
    # Throughput gauge
    fig_throughput = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=87.3,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "System Throughput (%)"},
        delta={'reference': 80},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': EAIS_COLORS['primary']},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig_throughput.update_layout(height=300)
    charts['throughput'] = fig_throughput
    
    return charts

def create_cost_optimization_chart() -> go.Figure:
    """Create cost optimization opportunities chart"""
    opportunities = [
        'Right-sizing instances',
        'Reserved instances',
        'Spot instances',
        'Auto-scaling optimization',
        'Storage optimization',
        'Network optimization',
        'Database optimization'
    ]
    
    savings = [12000, 25000, 8000, 15000, 7000, 5000, 10000]
    effort = [20, 40, 15, 35, 25, 30, 45]  # Effort in hours
    
    fig = go.Figure()
    
    # Create bubble chart
    fig.add_trace(go.Scatter(
        x=effort,
        y=savings,
        mode='markers+text',
        marker=dict(
            size=[(s/1000) for s in savings],  # Scale bubble size
            color=EAIS_PALETTE,
            opacity=0.7,
            line=dict(width=2, color='white')
        ),
        text=opportunities,
        textposition="middle center",
        textfont=dict(size=10),
        name='Optimization Opportunities'
    ))
    
    fig.update_layout(
        title="Cost Optimization Opportunities (Effort vs Savings)",
        xaxis_title="Implementation Effort (Hours)",
        yaxis_title="Annual Savings (USD)",
        template="plotly_white",
        height=400,
        showlegend=False
    )
    
    return fig

def style_metric_containers():
    """Apply custom styling to metric containers"""
    st.markdown("""
    <style>
    div[data-testid="metric-container"] {
        background-color: white;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    div[data-testid="metric-container"] > div {
        width: fit-content;
        margin: auto;
    }
    
    div[data-testid="metric-container"] > div > div[data-testid="metric-delta"] {
        margin-top: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)