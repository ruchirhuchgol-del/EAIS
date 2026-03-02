// User Types
export type UserRole = 'admin' | 'architect' | 'analyst' | 'viewer';

export interface User {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  avatar?: string;
  department?: string;
  isActive: boolean;
  lastLoginAt?: Date;
  createdAt: Date;
  updatedAt: Date;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}

// Architecture Types
export type ArchitectureType = 
  | 'microservices' 
  | 'monolithic' 
  | 'serverless' 
  | 'event-driven' 
  | 'layered' 
  | 'hexagonal'
  | 'cqrs'
  | 'hybrid';

export type ArchitectureStatus = 'draft' | 'generating' | 'completed' | 'failed';

export interface ArchitectureComponent {
  id: string;
  name: string;
  type: string;
  description: string;
  technology?: string;
  connections: string[];
}

export interface ArchitectureDiagram {
  id: string;
  name: string;
  type: 'context' | 'container' | 'component' | 'sequence' | 'deployment';
  url?: string;
  content?: string;
}

export interface ArchitecturePattern {
  id: string;
  name: string;
  description: string;
  applicability: string;
}

export interface Architecture {
  id: string;
  userId: string;
  name: string;
  description: string;
  type: ArchitectureType;
  status: ArchitectureStatus;
  businessRequirements?: string;
  technicalRequirements?: string;
  constraints?: string;
  overview?: string;
  components?: ArchitectureComponent[];
  diagrams?: ArchitectureDiagram[];
  patterns?: ArchitecturePattern[];
  recommendations?: string;
  complexityScore?: number;
  estimatedCost?: number;
  riskLevel?: 'low' | 'medium' | 'high' | 'critical';
  createdAt: Date;
  updatedAt: Date;
}

// Compliance Types
export type ComplianceFramework = 'GDPR' | 'SOC2' | 'HIPAA' | 'PCI-DSS' | 'ISO27001';

export interface ComplianceFinding {
  id: string;
  category: string;
  requirement: string;
  status: 'compliant' | 'non-compliant' | 'partial' | 'not-applicable';
  score: number;
  evidence?: string;
  recommendations?: string;
}

export interface ComplianceReport {
  id: string;
  userId: string;
  name: string;
  framework: ComplianceFramework;
  targetSystem: string;
  scopeDetails?: string;
  overallScore?: number;
  status: 'pending' | 'in_progress' | 'completed';
  findings?: ComplianceFinding[];
  recommendations?: string;
  governanceScore?: number;
  dataProtectionScore?: number;
  accessControlScore?: number;
  monitoringScore?: number;
  incidentResponseScore?: number;
  createdAt: Date;
  updatedAt: Date;
}

// Business Analysis Types
export interface BusinessAnalysis {
  id: string;
  userId: string;
  name: string;
  description?: string;
  currentSystemCosts?: number;
  currentStaffCount?: number;
  currentDowntimeHours?: number;
  proposedSystemCosts?: number;
  proposedStaffCount?: number;
  expectedEfficiencyGain?: number;
  tcoSavings?: number;
  roiPercentage?: number;
  paybackPeriodMonths?: number;
  npv?: number;
  riskAnalysis?: string;
  opportunities?: string;
  recommendations?: string;
  status: 'pending' | 'analyzing' | 'completed';
  createdAt: Date;
  updatedAt: Date;
}

// Knowledge Graph Types
export type NodeType = 'component' | 'pattern' | 'principle' | 'technology' | 'standard';
export type EdgeType = 'uses' | 'implements' | 'relates_to' | 'depends_on' | 'contains';

export interface KnowledgeNode {
  id: string;
  type: NodeType;
  name: string;
  label: string;
  description?: string;
  properties?: Record<string, unknown>;
  createdAt: Date;
  updatedAt: Date;
}

export interface KnowledgeEdge {
  id: string;
  sourceId: string;
  targetId: string;
  type: EdgeType;
  weight: number;
  properties?: Record<string, unknown>;
  createdAt: Date;
}

export interface GraphData {
  nodes: KnowledgeNode[];
  edges: KnowledgeEdge[];
}

// Agent Types
export type AgentType = 'architecture' | 'compliance' | 'business';

export interface AgentTask {
  id: string;
  type: AgentType;
  status: 'pending' | 'running' | 'completed' | 'failed';
  progress: number;
  message?: string;
  result?: unknown;
  error?: string;
  startedAt?: Date;
  completedAt?: Date;
}

export interface AgentMessage {
  id: string;
  agent: AgentType;
  role: 'system' | 'assistant' | 'user';
  content: string;
  timestamp: Date;
}

// Dashboard Types
export interface DashboardMetric {
  name: string;
  value: number;
  change?: number;
  trend?: 'up' | 'down' | 'stable';
  unit?: string;
}

export interface SystemHealth {
  status: 'healthy' | 'degraded' | 'unhealthy';
  uptime: number;
  activeUsers: number;
  lastUpdated: Date;
}

// API Response Types
export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
}

// Form Types
export interface ArchitectureFormInput {
  name: string;
  description: string;
  type: ArchitectureType;
  businessRequirements: string;
  technicalRequirements: string;
  constraints?: string;
}

export interface ComplianceFormInput {
  name: string;
  framework: ComplianceFramework;
  targetSystem: string;
  scopeDetails?: string;
}

export interface BusinessAnalysisFormInput {
  name: string;
  description?: string;
  currentSystemCosts: number;
  currentStaffCount: number;
  currentDowntimeHours: number;
  proposedSystemCosts: number;
  proposedStaffCount: number;
  expectedEfficiencyGain: number;
}
