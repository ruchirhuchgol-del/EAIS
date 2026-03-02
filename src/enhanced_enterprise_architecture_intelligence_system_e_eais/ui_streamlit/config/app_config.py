"""
Configuration file for EAIS Streamlit application.
"""

import yaml
import os
from typing import Dict, Any

def create_app_config():
    """Create default application configuration"""
    
    config = {
        'app': {
            'name': 'EAIS - Enterprise Architecture Intelligence System',
            'version': '1.0.0',
            'description': 'AI-powered enterprise architecture intelligence platform',
            'author': 'EAIS Development Team',
            'debug': False
        },
        'server': {
            'host': '0.0.0.0',
            'port': 8501,
            'max_upload_size': 200,  # MB
            'enable_cors': True,
            'enable_xsrf_protection': True
        },
        'features': {
            'authentication': True,
            'multi_tenancy': True,
            'audit_logging': True,
            'real_time_metrics': True,
            'auto_refresh': True,
            'export_capabilities': True
        },
        'ui': {
            'theme': 'light',
            'sidebar_width': 300,
            'chart_height': 400,
            'enable_wide_mode': True,
            'show_metrics': True,
            'auto_refresh_interval': 30  # seconds
        },
        'ai': {
            'default_provider': 'openai',
            'model': 'gpt-4o-mini',
            'temperature': 0.7,
            'max_tokens': 4000,
            'timeout': 120,
            'retry_attempts': 3
        },
        'security': {
            'session_timeout': 3600,  # seconds
            'password_policy': 'standard',
            'require_mfa': False,
            'enable_audit_log': True,
            'rate_limiting': True,
            'max_requests_per_minute': 60
        },
        'database': {
            'type': 'json',  # For now, using JSON files
            'path': 'data/',
            'backup_enabled': True,
            'backup_interval': 24  # hours
        },
        'integrations': {
            'slack': {
                'enabled': False,
                'webhook_url': None
            },
            'teams': {
                'enabled': False,
                'webhook_url': None
            },
            'email': {
                'enabled': False,
                'smtp_server': None,
                'smtp_port': 587,
                'username': None,
                'password': None
            }
        },
        'logging': {
            'level': 'INFO',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'file': 'logs/eais.log',
            'max_size': 10,  # MB
            'backup_count': 5
        }
    }
    
    return config

def save_default_config():
    """Save default configuration to file"""
    
    config_dir = os.path.join(
        os.path.dirname(__file__)
    )
    
    os.makedirs(config_dir, exist_ok=True)
    
    config_file = os.path.join(config_dir, 'app_config.yaml')
    
    if not os.path.exists(config_file):
        config = create_app_config()
        
        with open(config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, indent=2)
        
        print(f"✓ Created default configuration: {config_file}")
    else:
        print(f"✓ Configuration file exists: {config_file}")

if __name__ == "__main__":
    save_default_config()