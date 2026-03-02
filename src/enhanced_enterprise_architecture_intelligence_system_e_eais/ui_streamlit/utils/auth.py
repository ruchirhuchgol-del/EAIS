"""
Authentication utilities for EAIS Streamlit application.
"""

import streamlit as st
import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
import yaml

class AuthenticationManager:
    """Manages user authentication and authorization for EAIS"""
    
    def __init__(self):
        """Initialize authentication manager"""
        self.users_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'users.yaml')
        self.load_users()
    
    def load_users(self):
        """Load user credentials from configuration"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r') as f:
                    self.users = yaml.safe_load(f)
            else:
                # Create default users if file doesn't exist
                self.users = self.get_default_users()
                self.save_users()
        except Exception as e:
            st.warning(f"Could not load users: {e}. Using defaults.")
            self.users = self.get_default_users()
    
    def get_default_users(self) -> Dict:
        """Get default user configuration"""
        return {
            'credentials': {
                'admin@eais.com': {
                    'email': 'admin@eais.com',
                    'name': 'EAIS Administrator',
                    'password': self.hash_password('eais_admin_2024'),
                    'role': 'administrator',
                    'permissions': ['all'],
                    'created_at': datetime.now().isoformat()
                },
                'architect@eais.com': {
                    'email': 'architect@eais.com', 
                    'name': 'Enterprise Architect',
                    'password': self.hash_password('architect_2024'),
                    'role': 'architect',
                    'permissions': ['architecture', 'compliance', 'reports'],
                    'created_at': datetime.now().isoformat()
                },
                'analyst@eais.com': {
                    'email': 'analyst@eais.com',
                    'name': 'Business Analyst',
                    'password': self.hash_password('analyst_2024'),
                    'role': 'analyst',
                    'permissions': ['business_analysis', 'reports'],
                    'created_at': datetime.now().isoformat()
                },
                'viewer@eais.com': {
                    'email': 'viewer@eais.com',
                    'name': 'Viewer',
                    'password': self.hash_password('viewer_2024'),
                    'role': 'viewer',
                    'permissions': ['reports'],
                    'created_at': datetime.now().isoformat()
                }
            },
            'roles': {
                'administrator': {
                    'name': 'Administrator',
                    'description': 'Full system access and user management',
                    'permissions': ['all']
                },
                'architect': {
                    'name': 'Enterprise Architect',
                    'description': 'Architecture design and compliance assessment',
                    'permissions': ['architecture', 'compliance', 'knowledge_graph', 'reports']
                },
                'analyst': {
                    'name': 'Business Analyst',
                    'description': 'Business impact analysis and reporting',
                    'permissions': ['business_analysis', 'reports', 'knowledge_graph']
                },
                'viewer': {
                    'name': 'Viewer',
                    'description': 'Read-only access to reports and dashboards',
                    'permissions': ['reports', 'dashboard']
                }
            }
        }
    
    def save_users(self):
        """Save users to configuration file"""
        try:
            os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
            with open(self.users_file, 'w') as f:
                yaml.dump(self.users, f, default_flow_style=False)
        except Exception as e:
            st.error(f"Could not save users: {e}")
    
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, stored_password: str, provided_password: str) -> bool:
        """Verify password against stored hash"""
        return hmac.compare_digest(stored_password, self.hash_password(provided_password))
    
    def authenticate(self, email: str, password: str) -> Tuple[bool, Optional[Dict]]:
        """Authenticate user credentials"""
        if email in self.users['credentials']:
            user = self.users['credentials'][email]
            if self.verify_password(user['password'], password):
                return True, user
        return False, None
    
    def check_permission(self, user_role: str, required_permission: str) -> bool:
        """Check if user has required permission"""
        if user_role not in self.users['roles']:
            return False
        
        user_permissions = self.users['roles'][user_role]['permissions']
        return 'all' in user_permissions or required_permission in user_permissions
    
    def get_user_info(self, email: str) -> Optional[Dict]:
        """Get user information by email"""
        return self.users['credentials'].get(email)

# Global authentication manager instance
auth_manager = AuthenticationManager()

def render_login_page() -> bool:
    """Render login page and handle authentication"""
    st.markdown("""
    <div style="max-width: 400px; margin: 0 auto; padding: 2rem;">
        <h2 style="text-align: center; color: #2E86AB;">🏗️ EAIS Authentication</h2>
        <p style="text-align: center; color: #666;">
            Enter your credentials to access the Enterprise Architecture Intelligence System
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        with st.form("login_form"):
            st.subheader("Login to EAIS")
            
            email = st.text_input("📧 Email", placeholder="user@company.com")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
            
            col_login, col_demo = st.columns(2)
            
            with col_login:
                login_submitted = st.form_submit_button("🚀 Login", use_container_width=True)
            
            with col_demo:
                demo_submitted = st.form_submit_button("🎯 Demo Login", use_container_width=True)
            
            if login_submitted:
                if email and password:
                    success, user = auth_manager.authenticate(email, password)
                    if success and user is not None:
                        st.session_state.authenticated = True
                        st.session_state.username = user['name']
                        st.session_state.user_email = user['email']
                        st.session_state.user_role = user['role']
                        # Get permissions from the role definition, not from the user credentials
                        role_permissions = auth_manager.users['roles'][user['role']]['permissions']
                        st.session_state.user_permissions = role_permissions
                        st.success(f"Welcome, {user['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials. Please try again.")
                else:
                    st.warning("⚠️ Please enter both email and password.")
            
            if demo_submitted:
                # Demo login with architect credentials
                st.session_state.authenticated = True
                st.session_state.username = "Demo Enterprise Architect"
                st.session_state.user_email = "architect@eais.com"
                st.session_state.user_role = "architect"
                st.session_state.user_permissions = ["architecture", "compliance", "reports"]
                st.success("🎯 Demo mode activated!")
                st.rerun()
        
        # Display demo credentials
        with st.expander("🔍 Demo Credentials", expanded=False):
            st.markdown("""
            **Available Demo Accounts:**
            
            🔑 **Administrator**
            - Email: `admin@eais.com`
            - Password: `eais_admin_2024`
            - Access: Full system access
            
            🏗️ **Enterprise Architect**
            - Email: `architect@eais.com`
            - Password: `architect_2024`
            - Access: Architecture, Compliance, Reports
            
            💼 **Business Analyst**
            - Email: `analyst@eais.com`
            - Password: `analyst_2024`
            - Access: Business Analysis, Reports
            
            👁️ **Viewer**
            - Email: `viewer@eais.com`
            - Password: `viewer_2024`
            - Access: Reports and Dashboards (Read-only)
            """)
        
        # System information
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.8rem;">
            <p>🔒 Secure Authentication • 🛡️ Role-Based Access Control</p>
            <p>EAIS v1.0.0 - Enterprise Architecture Intelligence System</p>
        </div>
        """, unsafe_allow_html=True)
    
    return False

def require_permission(permission: str):
    """Decorator to require specific permission for page access"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not st.session_state.get('authenticated', False):
                st.error("🔐 Authentication required")
                return
            
            user_role = st.session_state.get('user_role')
            if user_role is None or not auth_manager.check_permission(user_role, permission):
                st.error(f"🚫 Access denied. Required permission: {permission}")
                st.info(f"Your role '{user_role}' does not have access to this feature.")
                return
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def get_current_user() -> Optional[Dict]:
    """Get current authenticated user information"""
    if st.session_state.get('authenticated', False):
        return {
            'name': st.session_state.get('username'),
            'email': st.session_state.get('user_email'),
            'role': st.session_state.get('user_role'),
            'permissions': st.session_state.get('user_permissions', [])
        }
    return None

def has_permission(permission: str) -> bool:
    """Check if current user has specific permission"""
    if not st.session_state.get('authenticated', False):
        return False
    
    user_role = st.session_state.get('user_role')
    if user_role is None:
        return False
        
    return auth_manager.check_permission(user_role, permission)

# Global authentication manager instance
auth_manager = AuthenticationManager()
