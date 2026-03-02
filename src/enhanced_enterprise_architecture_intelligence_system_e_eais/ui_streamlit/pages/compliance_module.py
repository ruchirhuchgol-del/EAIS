"""
Compliance & Security Assessment page for EAIS Streamlit application.

This module provides comprehensive compliance framework mapping, security assessment,
regulatory requirement analysis, and automated evidence generation capabilities.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from typing import Dict, List, Any, Optional

from src.enhanced_enterprise_architecture_intelligence_system_e_eais.ui_streamlit.utils import helpers, visualization, auth

@auth.require_permission('compliance')
def render_compliance_page():
    """Render the compliance and security assessment page"""
    
    st.title("🛡️ Compliance & Security Assessment")
    st.markdown("**Comprehensive regulatory compliance mapping and security analysis**")
    st.markdown("---")
    
    # Main navigation tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Compliance Dashboard",
        "🔍 Framework Assessment", 
        "🛡️ Security Analysis",
        "📋 Evidence Generator",
        "📈 Compliance Reporting"
    ])
    
    with tab1:
        render_compliance_dashboard()
    
    with tab2:
        render_framework_assessment()
    
    with tab3:
        render_security_analysis()
    
    with tab4:
        render_evidence_generator()
    
    with tab5:
        render_compliance_reporting()

def render_compliance_dashboard():
    """Render compliance overview dashboard"""
    
    # Key compliance metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Overall Compliance", "94.2%", "↗️ +2.1%")
    
    with col2:
        st.metric("🏆 Frameworks Assessed", "12", "↗️ +3")
    
    with col3:
        st.metric("⚠️ Open Issues", "8", "↘️ -5")
    
    with col4:
        st.metric("📅 Next Audit", "45 days", "📊 SOC2")
    
    st.markdown("---")
    
    # Compliance charts
    frameworks_data = helpers.generate_compliance_framework_data()
    heatmap = visualization.create_compliance_heatmap(frameworks_data)
    st.plotly_chart(heatmap, use_container_width=True)

def render_framework_assessment():
    """Render detailed framework assessment interface"""
    
    st.subheader("🔍 Compliance Framework Assessment")
    
    # Check if we have real AI results
    if st.session_state.get('generation_result'):
        result = st.session_state.generation_result
        st.info("Showing compliance results from the last architecture generation.")
        
        # Display the AI-generated compliance report
        compliance_report = ""
        # The AI result might be in tech_stack or we can look at the raw result
        if "Compliance" in result.get("technology_stack", {}):
            compliance_report = result["technology_stack"]["Compliance"]
        
        if compliance_report:
            st.markdown("### 📄 AI-Generated Compliance Report")
            st.markdown(compliance_report)
            st.markdown("---")

    selected_frameworks = st.multiselect(
        "Select frameworks to assess (Manual Mode)",
        ["GDPR", "SOC2 Type II", "PCI-DSS", "ISO 27001", "HIPAA"],
        default=["GDPR", "SOC2 Type II"]
    )
    
    if st.button("🚀 Start Manual Assessment", type="primary"):
        if selected_frameworks:
            st.success(f"Assessment started for {len(selected_frameworks)} framework(s)")
        else:
            st.error("Please select at least one framework")

def render_security_analysis():
    """Render security analysis interface"""
    
    st.subheader("🛡️ Security Analysis & Assessment")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🛡️ Security Score", "92.8", "↗️ +3.2")
    
    with col2:
        st.metric("🔍 Vulnerabilities", "12", "↘️ -8")
    
    with col3:
        st.metric("🔐 Security Controls", "156/162", "↗️ +6")
    
    with col4:
        st.metric("📊 Risk Level", "Low", "↘️ Improved")
    
    # Risk matrix
    risk_matrix = visualization.create_risk_matrix()
    st.plotly_chart(risk_matrix, use_container_width=True)

def render_evidence_generator():
    """Render compliance evidence generator interface"""
    
    st.subheader("📋 Compliance Evidence Generator")
    
    with st.form("evidence_form"):
        evidence_framework = st.selectbox(
            "Select compliance framework",
            ["GDPR", "SOC2 Type II", "PCI-DSS", "ISO 27001", "HIPAA"]
        )
        
        evidence_type = st.multiselect(
            "Evidence types to generate",
            ["Policy Documents", "Technical Controls", "Audit Logs", "Training Records"],
            default=["Policy Documents", "Technical Controls"]
        )
        
        if st.form_submit_button("🚀 Generate Evidence", type="primary"):
            st.success(f"Evidence generation started for {evidence_framework}")

def render_compliance_reporting():
    """Render compliance reporting interface"""
    
    st.subheader("📈 Compliance Reporting")
    
    report_type = st.selectbox(
        "Report Type",
        ["Executive Summary", "Detailed Assessment", "Gap Analysis", "Remediation Plan"]
    )
    
    if st.button("📊 Generate Report", type="primary"):
        st.success(f"Generating {report_type} report...")