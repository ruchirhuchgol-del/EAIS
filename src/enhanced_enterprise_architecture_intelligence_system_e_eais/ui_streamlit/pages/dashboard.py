"""
Executive Dashboard page for EAIS Streamlit application.

This module provides a comprehensive executive dashboard with real-time metrics,
architecture analytics, compliance status, and business performance indicators.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from typing import Dict, List, Any
import time

# Changed from relative import to absolute import
from src.enhanced_enterprise_architecture_intelligence_system_e_eais.ui_streamlit.utils import helpers, visualization, auth

@auth.require_permission('dashboard')
def render_dashboard_page():
    """Render the executive dashboard page"""
    
    # Apply custom styling
    visualization.style_metric_containers()
    
    st.title("🏠 Executive Dashboard")
    st.markdown("**Real-time enterprise architecture intelligence and performance metrics**")
    st.markdown("---")
    
    # Quick refresh button
    col1, col2, col3 = st.columns([6, 1, 1])
    with col2:
        if st.button("🔄 Refresh", help="Refresh dashboard data"):
            st.rerun()
    
    with col3:
        auto_refresh = st.checkbox("Auto-refresh", help="Auto-refresh every 30 seconds")
    
    if auto_refresh:
        time.sleep(30)
        st.rerun()
    
    # Key Performance Indicators
    render_kpi_section()
    
    st.markdown("---")
    
    # Main dashboard content in tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Architecture Analytics", 
        "🛡️ Compliance Overview", 
        "💰 Financial Metrics", 
        "⚡ System Performance"
    ])
    
    with tab1:
        render_architecture_analytics()
    
    with tab2:
        render_compliance_overview()
    
    with tab3:
        render_financial_metrics()
    
    with tab4:
        render_system_performance()

def render_kpi_section():
    """Render key performance indicators section"""
    st.subheader("📊 Key Performance Indicators")
    
    # First row of KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🏗️ Architectures Delivered",
            value="127",
            delta="↗️ 12 this month",
            help="Total number of enterprise architectures generated and delivered"
        )
    
    with col2:
        st.metric(
            label="🛡️ Avg Compliance Score",
            value="94.2%",
            delta="↗️ +2.1%",
            help="Average compliance score across all frameworks"
        )
    
    with col3:
        st.metric(
            label="💰 Total TCO Savings",
            value="$2.4M",
            delta="↗️ +$340K",
            help="Total cost savings identified through architecture optimization"
        )
    
    with col4:
        st.metric(
            label="⚡ Avg Generation Time",
            value="3.2 min",
            delta="↘️ -0.8 min",
            help="Average time to generate complete architecture solution"
        )
    
    # Second row of KPIs  
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.metric(
            label="🎯 Active Projects",
            value="45",
            delta="↗️ +8",
            help="Number of active architecture projects"
        )
    
    with col6:
        st.metric(
            label="🔧 System Uptime",
            value="99.94%",
            delta="↗️ +0.02%",
            help="EAIS system availability and uptime"
        )
    
    with col7:
        st.metric(
            label="👥 Active Users",
            value="284",
            delta="↗️ +23",
            help="Number of active users in the last 30 days"
        )
    
    with col8:
        st.metric(
            label="📈 ROI Achievement",
            value="18.7%",
            delta="↗️ +3.2%",
            help="Average ROI achieved through EAIS implementations"
        )

def render_architecture_analytics():
    """Render architecture analytics section"""
    col1, col2 = st.columns(2)
    
    with col1:
        # Architecture projects timeline
        charts = visualization.create_executive_dashboard_charts()
        st.plotly_chart(charts['projects_timeline'], use_container_width=True)
        
        # Architecture quality radar
        quality_radar = visualization.create_architecture_quality_radar()
        st.plotly_chart(quality_radar, use_container_width=True)
    
    with col2:
        # Technology stack distribution
        stack_chart = visualization.create_technology_stack_sunburst()
        st.plotly_chart(stack_chart, use_container_width=True)
        
        # Recent architecture activities
        st.subheader("📋 Recent Activities")
        activities = [
            {"time": "2 hours ago", "action": "Generated e-commerce architecture", "user": "Alice Chen"},
            {"time": "4 hours ago", "action": "Completed compliance review", "user": "Bob Smith"},
            {"time": "6 hours ago", "action": "Published financial analysis", "user": "Carol Johnson"},
            {"time": "8 hours ago", "action": "Updated knowledge graph", "user": "David Wilson"},
            {"time": "1 day ago", "action": "Created architecture report", "user": "Eva Martinez"}
        ]
        
        for activity in activities:
            st.markdown(f"""
            <div style="padding: 0.5rem; margin: 0.5rem 0; border-left: 3px solid #2E86AB; background-color: #f8f9fa;">
                <strong>{activity['action']}</strong><br>
                <small>👤 {activity['user']} • ⏰ {activity['time']}</small>
            </div>
            """, unsafe_allow_html=True)

def render_compliance_overview():
    """Render compliance overview section"""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Compliance scores by framework
        charts = visualization.create_executive_dashboard_charts()
        st.plotly_chart(charts['compliance_scores'], use_container_width=True)
        
        # Compliance heatmap
        frameworks_data = helpers.generate_compliance_framework_data()
        heatmap = visualization.create_compliance_heatmap(frameworks_data)
        st.plotly_chart(heatmap, use_container_width=True)
    
    with col2:
        st.subheader("🛡️ Compliance Status")
        
        # Framework status cards
        for framework in frameworks_data:
            status_color = "success" if framework['status'] == 'Compliant' else "warning"
            
            st.markdown(f"""
            <div style="
                background: white;
                padding: 1rem;
                border-radius: 0.5rem;
                border-left: 4px solid {'#28a745' if status_color == 'success' else '#ffc107'};
                margin-bottom: 1rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                <h5 style="margin: 0; color: #333;">{framework['name']}</h5>
                <p style="margin: 0.5rem 0; color: #666; font-size: 0.9rem;">{framework['category']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: bold; color: {'#28a745' if status_color == 'success' else '#ffc107'};">
                        {framework['status']}
                    </span>
                    <span style="font-size: 1.2rem; font-weight: bold;">
                        {framework['coverage']:.1f}%
                    </span>
                </div>
                <div style="margin-top: 0.5rem; font-size: 0.8rem; color: #888;">
                    {framework['controls_implemented']}/{framework['controls_total']} controls implemented
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Compliance trends
        st.subheader("📈 Compliance Trends")
        trend_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Score': [89.2, 91.5, 92.8, 93.4, 94.1, 94.2]
        })
        
        fig_trend = px.line(trend_data, x='Month', y='Score', 
                           title="6-Month Compliance Score Trend",
                           line_shape='spline')
        fig_trend.update_traces(line_color=visualization.EAIS_COLORS['primary'])
        fig_trend.update_layout(height=200, template="plotly_white")
        st.plotly_chart(fig_trend, use_container_width=True)

def render_financial_metrics():
    """Render financial metrics section"""
    col1, col2 = st.columns(2)
    
    with col1:
        # TCO breakdown
        charts = visualization.create_executive_dashboard_charts()
        st.plotly_chart(charts['tco_breakdown'], use_container_width=True)
        
        # ROI projection
        st.plotly_chart(charts['roi_projection'], use_container_width=True)
    
    with col2:
        # Cost optimization opportunities
        optimization_chart = visualization.create_cost_optimization_chart()
        st.plotly_chart(optimization_chart, use_container_width=True)
        
        # Financial summary
        st.subheader("💰 Financial Summary")
        
        tco_data = helpers.generate_tco_analysis_data()
        
        summary_metrics = [
            ("Initial Investment", helpers.format_currency(tco_data['initial_investment'])),
            ("Annual OpEx", helpers.format_currency(sum(tco_data['annual_operating_costs'].values()))),
            ("Annual Savings", helpers.format_currency(sum(tco_data['cost_savings'].values()))),
            ("Net ROI (5-year)", f"{tco_data['projected_roi']['year_5']:.1f}%"),
            ("Payback Period", f"{tco_data['payback_period_months']} months")
        ]
        
        for label, value in summary_metrics:
            st.markdown(f"""
            <div style="
                display: flex;
                justify-content: space-between;
                padding: 0.5rem 0;
                border-bottom: 1px solid #eee;
            ">
                <span style="color: #666;">{label}</span>
                <span style="font-weight: bold; color: #333;">{value}</span>
            </div>
            """, unsafe_allow_html=True)

def render_system_performance():
    """Render system performance section"""
    col1, col2 = st.columns(2)
    
    with col1:
        # Performance metrics
        perf_charts = visualization.create_performance_metrics_dashboard()
        st.plotly_chart(perf_charts['response_time'], use_container_width=True)
        
        # Risk assessment matrix
        risk_matrix = visualization.create_risk_matrix()
        st.plotly_chart(risk_matrix, use_container_width=True)
    
    with col2:
        # System throughput gauge
        st.plotly_chart(perf_charts['throughput'], use_container_width=True)
        
        # System health indicators
        st.subheader("🔧 System Health")
        
        health_indicators = [
            {"component": "AI Agent Cluster", "status": "Healthy", "uptime": "99.97%", "load": "67%"},
            {"component": "Knowledge Graph", "status": "Healthy", "uptime": "99.94%", "load": "45%"},
            {"component": "API Gateway", "status": "Healthy", "uptime": "99.99%", "load": "72%"},
            {"component": "Database Cluster", "status": "Warning", "uptime": "99.85%", "load": "89%"},
            {"component": "Cache Layer", "status": "Healthy", "uptime": "99.92%", "load": "34%"}
        ]
        
        for indicator in health_indicators:
            status_color = "#28a745" if indicator["status"] == "Healthy" else "#ffc107"
            
            st.markdown(f"""
            <div style="
                background: white;
                padding: 0.8rem;
                border-radius: 0.3rem;
                border-left: 4px solid {status_color};
                margin-bottom: 0.5rem;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong>{indicator['component']}</strong>
                    <span style="
                        background: {status_color};
                        color: white;
                        padding: 0.2rem 0.5rem;
                        border-radius: 0.2rem;
                        font-size: 0.7rem;
                        font-weight: bold;
                    ">{indicator['status']}</span>
                </div>
                <div style="margin-top: 0.3rem; font-size: 0.8rem; color: #666;">
                    Uptime: {indicator['uptime']} • Load: {indicator['load']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Alert notifications
        st.subheader("🚨 Active Alerts")
        
        alerts = [
            {"level": "warning", "message": "Database cluster at 89% capacity", "time": "5 min ago"},
            {"level": "info", "message": "Scheduled maintenance in 2 hours", "time": "1 hour ago"}
        ]
        
        for alert in alerts:
            alert_color = {"warning": "#ffc107", "error": "#dc3545", "info": "#17a2b8"}.get(alert["level"], "#6c757d")
            
            st.markdown(f"""
            <div style="
                background: {alert_color}20;
                padding: 0.8rem;
                border-radius: 0.3rem;
                border-left: 4px solid {alert_color};
                margin-bottom: 0.5rem;
            ">
                <div style="font-weight: 500; color: #333;">{alert['message']}</div>
                <div style="font-size: 0.8rem; color: #666; margin-top: 0.3rem;">
                    ⏰ {alert['time']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# Add real-time data refresh capability
if 'dashboard_last_refresh' not in st.session_state:
    st.session_state.dashboard_last_refresh = datetime.now()

def get_refresh_status():
    """Get dashboard refresh status"""
    last_refresh = st.session_state.dashboard_last_refresh
    time_diff = datetime.now() - last_refresh
    
    if time_diff < timedelta(minutes=5):
        return "🟢 Data is current"
    elif time_diff < timedelta(minutes=15):
        return "🟡 Data may be stale"
    else:
        return "🔴 Data is outdated"