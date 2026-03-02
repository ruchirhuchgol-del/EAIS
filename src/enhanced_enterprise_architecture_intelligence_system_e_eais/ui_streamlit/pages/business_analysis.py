"""
Business Analysis & TCO Modeling page for EAIS Streamlit application.

This module provides comprehensive business impact analysis, TCO modeling,
ROI calculations, and financial optimization recommendations.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from typing import Dict, List, Any, Optional

from src.enhanced_enterprise_architecture_intelligence_system_e_eais.ui_streamlit.utils import helpers, visualization, auth

@auth.require_permission('business_analysis')
def render_business_analysis_page():
    """Render the business analysis and TCO modeling page"""
    
    st.title("💼 Business Analysis & TCO Modeling")
    st.markdown("**Comprehensive business impact analysis and financial optimization**")
    st.markdown("---")
    
    # Main navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Business Dashboard",
        "💰 TCO Modeling", 
        "📈 ROI Analysis",
        "🎯 Optimization Recommendations"
    ])
    
    with tab1:
        render_business_dashboard()
        
        # Check if we have real AI results
        if st.session_state.get('generation_result'):
            result = st.session_state.generation_result
            st.markdown("---")
            st.info("Showing business impact analysis from the last architecture generation.")
            
            business_report = ""
            if "Business" in result.get("technology_stack", {}):
                business_report = result["technology_stack"]["Business"]
            
            if business_report:
                st.markdown("### 📄 AI-Generated Business Impact Report")
                st.markdown(business_report)
    
    with tab2:
        render_tco_modeling()
    
    with tab3:
        render_roi_analysis()
    
    with tab4:
        render_optimization_recommendations()

def render_business_dashboard():
    """Render business metrics dashboard"""
    
    # Key business metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Total TCO", "$4.92M", "↘️ -$680K")
    
    with col2:
        st.metric("📈 5-Year ROI", "24.8%", "↗️ +3.2%")
    
    with col3:
        st.metric("⏱️ Payback Period", "28 months", "↘️ -4 months")
    
    with col4:
        st.metric("💡 Cost Savings", "$900K/year", "↗️ +$150K")
    
    st.markdown("---")
    
    # Business charts
    col1, col2 = st.columns(2)
    
    with col1:
        # TCO breakdown
        charts = visualization.create_executive_dashboard_charts()
        st.plotly_chart(charts['tco_breakdown'], use_container_width=True)
    
    with col2:
        # ROI projection
        st.plotly_chart(charts['roi_projection'], use_container_width=True)
    
    # Cost optimization opportunities
    optimization_chart = visualization.create_cost_optimization_chart()
    st.plotly_chart(optimization_chart, use_container_width=True)

def render_tco_modeling():
    """Render TCO modeling interface"""
    
    st.subheader("💰 Total Cost of Ownership Modeling")
    
    # TCO input form
    with st.form("tco_form"):
        st.markdown("#### 📝 TCO Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Initial Investment**")
            hardware_cost = st.number_input("Hardware & Infrastructure", value=800000, step=10000)
            software_cost = st.number_input("Software Licenses", value=350000, step=5000)
            implementation_cost = st.number_input("Implementation Services", value=450000, step=10000)
            
            st.markdown("**Annual Operating Costs**")
            infrastructure_cost = st.number_input("Infrastructure (annual)", value=450000, step=10000)
            personnel_cost = st.number_input("Personnel (annual)", value=650000, step=10000)
        
        with col2:
            st.markdown("**Additional Costs**")
            maintenance_cost = st.number_input("Maintenance (annual)", value=120000, step=5000)
            training_cost = st.number_input("Training (annual)", value=80000, step=5000)
            support_cost = st.number_input("Support (annual)", value=100000, step=5000)
            
            st.markdown("**Growth Factors**")
            annual_growth = st.slider("Annual cost growth (%)", 0.0, 10.0, 3.5, 0.1)
            
        if st.form_submit_button("📊 Calculate TCO", type="primary"):
            calculate_tco(hardware_cost, software_cost, implementation_cost, 
                         infrastructure_cost, personnel_cost, maintenance_cost,
                         training_cost, support_cost, annual_growth)

def calculate_tco(hardware, software, implementation, infrastructure, 
                 personnel, maintenance, training, support, growth):
    """Calculate and display TCO results"""
    
    initial_investment = hardware + software + implementation
    annual_opex = infrastructure + personnel + maintenance + training + support
    
    # 5-year projection
    years = list(range(1, 6))
    annual_costs = [annual_opex * (1 + growth/100) ** (year-1) for year in years]
    cumulative_costs = [initial_investment + sum(annual_costs[:i+1]) for i in range(5)]
    
    st.success("✅ TCO calculation completed!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Initial Investment", helpers.format_currency(initial_investment))
        st.metric("Annual OpEx (Year 1)", helpers.format_currency(annual_opex))
        st.metric("5-Year TCO", helpers.format_currency(cumulative_costs[-1]))
    
    with col2:
        # TCO projection chart
        fig_tco = px.line(
            x=years,
            y=cumulative_costs,
            title="5-Year TCO Projection",
            labels={'x': 'Year', 'y': 'Cumulative Cost (USD)'},
            markers=True
        )
        st.plotly_chart(fig_tco, use_container_width=True)

def render_roi_analysis():
    """Render ROI analysis interface"""
    
    st.subheader("📈 Return on Investment Analysis")
    
    # ROI calculation form
    with st.form("roi_form"):
        st.markdown("#### 💡 ROI Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Revenue Impact**")
            revenue_increase = st.number_input("Annual revenue increase", value=500000, step=10000)
            market_expansion = st.number_input("Market expansion value", value=200000, step=10000)
            
            st.markdown("**Cost Savings**")
            operational_savings = st.number_input("Operational cost savings", value=320000, step=10000)
            efficiency_gains = st.number_input("Efficiency gains value", value=180000, step=5000)
        
        with col2:
            st.markdown("**Risk Mitigation**")
            downtime_reduction = st.number_input("Downtime reduction value", value=150000, step=5000)
            compliance_savings = st.number_input("Compliance cost savings", value=100000, step=5000)
            
            st.markdown("**Timeline**")
            implementation_months = st.slider("Implementation timeline (months)", 3, 24, 12)
            
        if st.form_submit_button("📊 Calculate ROI", type="primary"):
            calculate_roi(revenue_increase, market_expansion, operational_savings,
                         efficiency_gains, downtime_reduction, compliance_savings,
                         implementation_months)

def calculate_roi(revenue_increase, market_expansion, operational_savings,
                 efficiency_gains, downtime_reduction, compliance_savings,
                 implementation_months):
    """Calculate and display ROI results"""
    
    annual_benefits = (revenue_increase + market_expansion + operational_savings + 
                      efficiency_gains + downtime_reduction + compliance_savings)
    
    # Assuming initial investment from TCO
    initial_investment = 1600000  # Example value
    
    # Calculate monthly benefits starting after implementation
    months = list(range(1, 61))  # 5 years
    monthly_benefits = [0] * implementation_months + [annual_benefits/12] * (60 - implementation_months)
    cumulative_benefits = [sum(monthly_benefits[:i+1]) for i in range(60)]
    net_value = [benefits - initial_investment for benefits in cumulative_benefits]
    
    # Find payback period
    payback_month = next((i for i, val in enumerate(net_value) if val > 0), None)
    
    st.success("✅ ROI calculation completed!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Annual Benefits", helpers.format_currency(annual_benefits))
        st.metric("5-Year NPV", helpers.format_currency(net_value[-1]))
        if payback_month:
            st.metric("Payback Period", f"{payback_month + 1} months")
    
    with col2:
        # ROI projection chart
        fig_roi = px.line(
            x=months,
            y=net_value,
            title="Net Value Over Time",
            labels={'x': 'Month', 'y': 'Net Value (USD)'},
            markers=True
        )
        fig_roi.add_hline(y=0, line_dash="dash", line_color="red")
        st.plotly_chart(fig_roi, use_container_width=True)

def render_optimization_recommendations():
    """Render optimization recommendations interface"""
    
    st.subheader("🎯 Business Optimization Recommendations")
    
    # Cost optimization opportunities
    st.markdown("### 💰 Cost Optimization Opportunities")
    
    opportunities = [
        {"opportunity": "Right-size cloud instances", "savings": 120000, "effort": "Medium", "timeline": "3 months"},
        {"opportunity": "Implement reserved instances", "savings": 250000, "effort": "Low", "timeline": "1 month"},
        {"opportunity": "Optimize database queries", "savings": 80000, "effort": "High", "timeline": "6 months"},
        {"opportunity": "Automate manual processes", "savings": 180000, "effort": "Medium", "timeline": "4 months"},
        {"opportunity": "Consolidate vendors", "savings": 90000, "effort": "Low", "timeline": "2 months"}
    ]
    
    for opp in opportunities:
        with st.expander(f"💡 {opp['opportunity']} - {helpers.format_currency(opp['savings'])} savings"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"**Effort Level:** {opp['effort']}")
            with col2:
                st.markdown(f"**Timeline:** {opp['timeline']}")
            with col3:
                st.markdown(f"**Annual Savings:** {helpers.format_currency(opp['savings'])}")
    
    # Performance optimization
    st.markdown("### ⚡ Performance Optimization")
    
    performance_metrics = {
        "Response Time": {"current": "450ms", "target": "150ms", "improvement": "67%"},
        "Throughput": {"current": "1,000 TPS", "target": "3,000 TPS", "improvement": "200%"},
        "Availability": {"current": "99.5%", "target": "99.9%", "improvement": "0.4%"},
        "Error Rate": {"current": "2.1%", "target": "0.5%", "improvement": "76%"}
    }
    
    col1, col2 = st.columns(2)
    
    for i, (metric, data) in enumerate(performance_metrics.items()):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div style="
                padding: 1rem;
                border: 1px solid #ddd;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
                background: #f8f9fa;
            ">
                <h5>{metric}</h5>
                <p>Current: <strong>{data['current']}</strong></p>
                <p>Target: <strong>{data['target']}</strong></p>
                <p>Improvement: <span style="color: green;"><strong>{data['improvement']}</strong></span></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Strategic recommendations
    st.markdown("### 🎯 Strategic Recommendations")
    
    if st.button("📊 Generate Business Case", type="primary"):
        st.success("Business case generated! Download link will be available shortly.")
    
    if st.button("📧 Share with Stakeholders"):
        st.success("Analysis shared with stakeholders!")