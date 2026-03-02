
"""
Main Streamlit Application for Enhanced Enterprise Architecture Intelligence System (EAIS)

This application provides an industry-grade web interface for enterprise architecture
intelligence, featuring executive dashboards, architecture generation, compliance
assessment, business impact analysis, and comprehensive reporting capabilities.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import sys
import os
from datetime import datetime, timedelta
import json
import time
from typing import Dict, Any, List, Optional

# Configure page settings
st.set_page_config(
    page_title="EAIS - Enterprise Architecture Intelligence System",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/eais/documentation',
        'Report a bug': 'https://github.com/eais/issues',
        'About': """
        # Enhanced Enterprise Architecture Intelligence System (EAIS)
        
        **Version:** 1.0.0
        
        An AI-powered platform that transforms product requirements into production-ready,
        enterprise-grade system architectures with comprehensive artifacts and modern web interface.
        
        **Features:**
        - Multi-Cloud Architecture Design
        - Automated Artifact Generation
        - Compliance Automation
        - Business Impact Optimization
        - Knowledge Management
        
        **Built with:** CrewAI, Streamlit, OpenAI GPT-4
        """
    }
)

# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import EAIS components
try:
    from src.enhanced_enterprise_architecture_intelligence_system_e_eais.core.orchestrator import EAISOrchestrator
    from src.enhanced_enterprise_architecture_intelligence_system_e_eais.data.knowledge_graph import KnowledgeGraph
except ImportError as e:
    st.error(f"Failed to import EAIS components: {e}")
    st.stop()

# Import page modules
from src.enhanced_enterprise_architecture_intelligence_system_e_eais.ui_streamlit.pages import (
    dashboard,
    architecture_generator,
    compliance_module,
    business_analysis,
    knowledge_graph_ui,
    reporting_module,
    settings
)
from src.enhanced_enterprise_architecture_intelligence_system_e_eais.ui_streamlit.utils import auth, helpers, visualization

class EAISStreamlitApp:
    """Main EAIS Streamlit Application Class"""
    
    def __init__(self):
        """Initialize the EAIS Streamlit application"""
        self.initialize_session_state()
        self.load_configuration()
    
    def initialize_session_state(self):
        """Initialize Streamlit session state variables"""
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'user_role' not in st.session_state:
            st.session_state.user_role = None
        if 'current_project' not in st.session_state:
            st.session_state.current_project = None
        if 'eais_crew' not in st.session_state:
            st.session_state.eais_crew = None
        if 'last_analysis_result' not in st.session_state:
            st.session_state.last_analysis_result = None
        if 'knowledge_graph' not in st.session_state:
            st.session_state.knowledge_graph = KnowledgeGraph()
    
    def load_configuration(self):
        """Load application configuration"""
        try:
            # Load app configuration
            config_path = os.path.join(os.path.dirname(__file__), 'config', 'app_config.yaml')
            if os.path.exists(config_path):
                import yaml
                with open(config_path, 'r') as f:
                    self.config = yaml.safe_load(f)
            else:
                self.config = self.get_default_config()
        except Exception as e:
            st.warning(f"Could not load configuration: {e}. Using defaults.")
            self.config = self.get_default_config()
    
    def get_default_config(self) -> Dict[str, Any]:
        """Get default application configuration"""
        return {
            'app': {
                'name': 'EAIS - Enterprise Architecture Intelligence System',
                'version': '1.0.0',
                'description': 'AI-powered enterprise architecture intelligence platform'
            },
            'features': {
                'authentication': True,
                'multi_tenancy': True,
                'audit_logging': True,
                'real_time_metrics': True
            },
            'ui': {
                'theme': 'corporate',
                'sidebar_width': 300,
                'chart_height': 400
            }
        }
    
    def render_header(self):
        """Render application header with branding and user info"""
        col1, col2, col3 = st.columns([2, 3, 2])
        
        with col1:
            st.image("https://via.placeholder.com/150x50/2E86AB/FFFFFF?text=EAIS", width=150)
        
        with col2:
            st.title("🏗️ Enterprise Architecture Intelligence System")
            st.caption("Transform requirements into production-ready architectures in minutes")
        
        with col3:
            if st.session_state.authenticated:
                st.success(f"👤 Welcome, {st.session_state.get('username', 'User')}")
                st.caption(f"Role: {st.session_state.user_role}")
                if st.button("🚪 Logout", key="logout_btn"):
                    self.logout()
            else:
                st.info("Please authenticate to access full features")
    
    def render_sidebar_navigation(self) -> str:
        """Render sidebar navigation menu"""
        with st.sidebar:
            st.image("https://via.placeholder.com/200x80/2E86AB/FFFFFF?text=EAIS+Logo", width=200)
            st.markdown("---")
            
            # Main navigation
            selected = option_menu(
                menu_title="Navigation",
                options=[
                    "🏠 Dashboard",
                    "🏗️ Architecture Generator", 
                    "🛡️ Compliance & Security",
                    "💼 Business Analysis",
                    "🧠 Knowledge Graph",
                    "📊 Reports & Analytics",
                    "⚙️ Settings"
                ],
                icons=[
                    "speedometer2",
                    "diagram-3",
                    "shield-check",
                    "graph-up",
                    "share",
                    "bar-chart",
                    "gear"
                ],
                menu_icon="list",
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "#2E86AB", "font-size": "18px"},
                    "nav-link": {
                        "font-size": "14px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee"
                    },
                    "nav-link-selected": {"background-color": "#2E86AB"},
                }
            )
            
            st.markdown("---")
            
            # Quick Stats
            self.render_sidebar_stats()
            
            # System Status
            self.render_system_status()
            
        return selected
    
    def render_sidebar_stats(self):
        """Render quick statistics in sidebar"""
        st.subheader("📈 Quick Stats")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Architectures", "127", "↗️ 12")
        with col2:
            st.metric("Compliance", "98.5%", "↗️ 2.1%")
        
        col3, col4 = st.columns(2)
        with col3:
            st.metric("TCO Saved", "$2.4M", "↗️ $340K")
        with col4:
            st.metric("Projects", "45", "↗️ 8")
    
    def render_system_status(self):
        """Render system status in sidebar"""
        st.subheader("🔧 System Status")
        
        # Mock system health data
        status_items = [
            ("AI Agents", "✅ Online", "success"),
            ("Knowledge Graph", "✅ Healthy", "success"),
            ("API Services", "✅ Running", "success"),
            ("Compliance DB", "⚠️ Syncing", "warning")
        ]
        
        for service, status, level in status_items:
            if level == "success":
                st.success(f"{service}: {status}")
            elif level == "warning":
                st.warning(f"{service}: {status}")
            else:
                st.error(f"{service}: {status}")
    
    def authenticate_user(self):
        """Handle user authentication"""
        if not st.session_state.authenticated:
            return auth.render_login_page()
        return True
    
    def logout(self):
        """Handle user logout"""
        st.session_state.authenticated = False
        st.session_state.user_role = None
        st.session_state.username = None
        st.session_state.current_project = None
        st.rerun()
    
    def render_main_content(self, selected_page: str):
        """Render main content based on selected page"""
        try:
            if selected_page == "🏠 Dashboard":
                dashboard.render_dashboard_page()
            elif selected_page == "🏗️ Architecture Generator":
                architecture_generator.render_architecture_generator_page()
            elif selected_page == "🛡️ Compliance & Security":
                compliance_module.render_compliance_page()
            elif selected_page == "💼 Business Analysis":
                business_analysis.render_business_analysis_page()
            elif selected_page == "🧠 Knowledge Graph":
                knowledge_graph_ui.render_knowledge_graph_page()
            elif selected_page == "📊 Reports & Analytics":
                reporting_module.render_reporting_page()
            elif selected_page == "⚙️ Settings":
                settings.render_settings_page()
            else:
                st.error(f"Unknown page: {selected_page}")
        except Exception as e:
            st.error(f"Error rendering page {selected_page}: {e}")
            st.exception(e)
    
    def render_footer(self):
        """Render application footer"""
        st.markdown("---")
        col1, col2, col3 = st.columns([2, 1, 2])
        
        with col1:
            st.caption("© 2024 EAIS - Enterprise Architecture Intelligence System")
        
        with col2:
            st.caption("v1.0.0")
        
        with col3:
            st.caption("Powered by CrewAI & OpenAI GPT-4")
    
    def run(self):
        """Main application entry point"""
        try:
            # Authentication check
            if not self.authenticate_user():
                return
            
            # Render header
            self.render_header()
            
            # Render navigation and get selected page
            selected_page = self.render_sidebar_navigation()
            
            # Render main content
            self.render_main_content(selected_page)
            
            # Render footer
            self.render_footer()
            
        except Exception as e:
            st.error(f"Application error: {e}")
            st.exception(e)

def main():
    """Main function to run the Streamlit application"""
    try:
        # Custom CSS for enhanced styling
        st.markdown("""
        <style>
        .main > div {
            padding-top: 1rem;
        }
        .stMetric {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 0.375rem;
            padding: 1rem;
        }
        .element-container div[data-testid="metric-container"] {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            padding: 1rem;
            border-radius: 0.375rem;
            box-shadow: 0 0.125rem 0.25rem rgba(0,0,0,0.075);
        }
        .stAlert {
            border-radius: 0.375rem;
        }
        .stButton > button {
            border-radius: 0.375rem;
            border: 1px solid #2E86AB;
            background-color: #2E86AB;
            color: white;
        }
        .stButton > button:hover {
            background-color: #1a5490;
            border-color: #1a5490;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Initialize and run the application
        app = EAISStreamlitApp()
        app.run()
        
    except Exception as e:
        st.error(f"Failed to start EAIS application: {e}")
        st.exception(e)

if __name__ == "__main__":
    main()