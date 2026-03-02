'use client';

/**
 * EAIS - Enterprise Architecture Intelligence System
 * Main Application Page
 * 
 * Industry-Grade AI-Powered Enterprise Architecture Platform
 */

import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Checkbox } from '@/components/ui/checkbox';
import { Separator } from '@/components/ui/separator';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { Skeleton } from '@/components/ui/skeleton';
import { ScrollArea } from '@/components/ui/scroll-area';
import { 
  Building2, 
  Shield, 
  TrendingUp, 
  Brain, 
  FileText, 
  Settings, 
  LogOut,
  ChevronRight,
  Sparkles,
  CheckCircle,
  AlertCircle,
  Clock,
  DollarSign,
  Target,
  Layers,
  Cloud,
  Lock,
  BarChart3,
  Activity,
  Users,
  Zap,
  Menu,
  X
} from 'lucide-react';

// Configuration
const EAIS_CONFIG = {
  complianceFrameworks: [
    { id: 'gdpr', name: 'GDPR', description: 'General Data Protection Regulation' },
    { id: 'soc2', name: 'SOC 2 Type II', description: 'Service Organization Control' },
    { id: 'pci-dss', name: 'PCI-DSS', description: 'Payment Card Industry' },
    { id: 'hipaa', name: 'HIPAA', description: 'Healthcare Privacy' },
    { id: 'iso27001', name: 'ISO 27001', description: 'Information Security' },
    { id: 'nist', name: 'NIST CSF', description: 'Cybersecurity Framework' },
  ],
  domains: ['E-commerce', 'Finance', 'Healthcare', 'Logistics', 'Manufacturing', 'Public Sector'],
  cloudProviders: ['AWS', 'Azure', 'GCP', 'Multi-Cloud', 'Hybrid'],
};

// Demo users
const DEMO_USERS = [
  { email: 'admin@eais.com', password: 'admin123', name: 'System Administrator', role: 'admin' },
  { email: 'architect@eais.com', password: 'architect123', name: 'Enterprise Architect', role: 'architect' },
  { email: 'analyst@eais.com', password: 'analyst123', name: 'Business Analyst', role: 'analyst' },
  { email: 'viewer@eais.com', password: 'viewer123', name: 'Report Viewer', role: 'viewer' },
];

export default function EAISPlatform() {
  // State management
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [currentPage, setCurrentPage] = useState('dashboard');
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [loading, setLoading] = useState(false);
  const [notifications, setNotifications] = useState([]);
  
  // Architecture generation state
  const [architectureForm, setArchitectureForm] = useState({
    projectName: '',
    businessObjectives: '',
    technicalRequirements: '',
    complianceRequirements: [],
    domain: '',
    cloudProvider: '',
  });
  const [generatedArchitecture, setGeneratedArchitecture] = useState(null);
  const [generationProgress, setGenerationProgress] = useState(0);
  const [generationStatus, setGenerationStatus] = useState('');
  
  // Statistics
  const [stats, setStats] = useState({
    totalArchitectures: 24,
    avgComplianceScore: 87,
    openRisks: 12,
    estimatedSavings: '$1.2M',
  });

  // Check for existing session
  useEffect(() => {
    const savedToken = localStorage.getItem('eais_token');
    const savedUser = localStorage.getItem('eais_user');
    if (savedToken && savedUser) {
      setToken(savedToken);
      setUser(JSON.parse(savedUser));
    }
  }, []);

  // Authentication
  const handleLogin = async (email, password) => {
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      
      const data = await response.json();
      
      if (data.success) {
        setToken(data.token);
        setUser(data.user);
        localStorage.setItem('eais_token', data.token);
        localStorage.setItem('eais_user', JSON.stringify(data.user));
        addNotification('Welcome back, ' + data.user.name, 'success');
      } else {
        addNotification(data.error || 'Login failed', 'error');
      }
    } catch (error) {
      addNotification('Connection error. Please try again.', 'error');
    }
  };

  const handleLogout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem('eais_token');
    localStorage.removeItem('eais_user');
    setCurrentPage('dashboard');
  };

  // Notifications
  const addNotification = (message, type = 'info') => {
    const id = Date.now();
    setNotifications(prev => [...prev, { id, message, type }]);
    setTimeout(() => {
      setNotifications(prev => prev.filter(n => n.id !== id));
    }, 5000);
  };

  // Architecture generation
  const generateArchitecture = async () => {
    if (!architectureForm.businessObjectives || !architectureForm.technicalRequirements) {
      addNotification('Please fill in required fields', 'error');
      return;
    }

    setLoading(true);
    setGenerationProgress(0);
    setGenerationStatus('Initializing AI agents...');

    try {
      // Simulate progress
      const progressInterval = setInterval(() => {
        setGenerationProgress(prev => {
          if (prev >= 90) {
            clearInterval(progressInterval);
            return prev;
          }
          return prev + 10;
        });
      }, 500);

      setGenerationStatus('Architecture Specialist analyzing requirements...');
      
      const response = await fetch('/api/eais/architecture', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(architectureForm),
      });

      const data = await response.json();
      
      clearInterval(progressInterval);
      setGenerationProgress(100);
      setGenerationStatus('Generation complete!');

      if (data.success) {
        setGeneratedArchitecture(data);
        addNotification('Architecture generated successfully!', 'success');
        
        // Update stats
        setStats(prev => ({
          ...prev,
          totalArchitectures: prev.totalArchitectures + 1,
        }));
      } else {
        addNotification(data.error || 'Generation failed', 'error');
      }
    } catch (error) {
      addNotification('Failed to generate architecture', 'error');
    } finally {
      setLoading(false);
    }
  };

  // Quick demo login
  const quickLogin = (role) => {
    const demoUser = DEMO_USERS.find(u => u.role === role);
    if (demoUser) {
      handleLogin(demoUser.email, demoUser.password);
    }
  };

  // If not authenticated, show login
  if (!user) {
    return <LoginScreen onLogin={handleLogin} quickLogin={quickLogin} />;
  }

  // Main application
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      {/* Notifications */}
      <div className="fixed top-4 right-4 z-50 space-y-2">
        {notifications.map(notification => (
          <Alert 
            key={notification.id} 
            className={`w-80 ${
              notification.type === 'success' ? 'border-green-500 bg-green-50' :
              notification.type === 'error' ? 'border-red-500 bg-red-50' :
              'border-blue-500 bg-blue-50'
            }`}
          >
            <AlertCircle className="h-4 w-4" />
            <AlertDescription>{notification.message}</AlertDescription>
          </Alert>
        ))}
      </div>

      {/* Header */}
      <header className="bg-white border-b shadow-sm sticky top-0 z-40">
        <div className="flex items-center justify-between px-6 py-4">
          <div className="flex items-center gap-4">
            <Button 
              variant="ghost" 
              size="icon" 
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="lg:hidden"
            >
              {sidebarOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </Button>
            <div className="flex items-center gap-3">
              <div className="h-10 w-10 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
                <Building2 className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-slate-900">EAIS Platform</h1>
                <p className="text-xs text-slate-500">Enterprise Architecture Intelligence System</p>
              </div>
            </div>
          </div>
          
          <div className="flex items-center gap-4">
            <Badge variant="outline" className="hidden sm:flex">
              <Activity className="h-3 w-3 mr-1 text-green-500" />
              System Healthy
            </Badge>
            <Separator orientation="vertical" className="h-8" />
            <div className="flex items-center gap-3">
              <Avatar className="h-8 w-8">
                <AvatarFallback className="bg-blue-600 text-white text-xs">
                  {user.name.split(' ').map(n => n[0]).join('')}
                </AvatarFallback>
              </Avatar>
              <div className="hidden md:block">
                <p className="text-sm font-medium">{user.name}</p>
                <p className="text-xs text-slate-500 capitalize">{user.role}</p>
              </div>
              <Button variant="ghost" size="icon" onClick={handleLogout}>
                <LogOut className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </header>

      <div className="flex">
        {/* Sidebar */}
        <aside className={`${sidebarOpen ? 'w-64' : 'w-0'} transition-all duration-300 bg-white border-r min-h-[calc(100vh-73px)] sticky top-[73px]`}>
          <nav className="p-4 space-y-2">
            {[
              { id: 'dashboard', icon: BarChart3, label: 'Dashboard' },
              { id: 'architecture', icon: Layers, label: 'Architecture Generator' },
              { id: 'compliance', icon: Shield, label: 'Compliance & Security' },
              { id: 'business', icon: TrendingUp, label: 'Business Analysis' },
              { id: 'knowledge', icon: Brain, label: 'Knowledge Graph' },
              { id: 'reports', icon: FileText, label: 'Reports & Analytics' },
              { id: 'settings', icon: Settings, label: 'Settings' },
            ].map(item => (
              <Button
                key={item.id}
                variant={currentPage === item.id ? 'default' : 'ghost'}
                className={`w-full justify-start ${currentPage === item.id ? 'bg-blue-600' : ''}`}
                onClick={() => setCurrentPage(item.id)}
              >
                <item.icon className="h-4 w-4 mr-3" />
                {item.label}
              </Button>
            ))}
          </nav>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-6">
          {currentPage === 'dashboard' && (
            <DashboardPage stats={stats} setCurrentPage={setCurrentPage} />
          )}
          {currentPage === 'architecture' && (
            <ArchitecturePage 
              form={architectureForm}
              setForm={setArchitectureForm}
              onGenerate={generateArchitecture}
              loading={loading}
              progress={generationProgress}
              status={generationStatus}
              result={generatedArchitecture}
            />
          )}
          {currentPage === 'compliance' && <CompliancePage />}
          {currentPage === 'business' && <BusinessPage />}
          {currentPage === 'knowledge' && <KnowledgePage />}
          {currentPage === 'reports' && <ReportsPage />}
          {currentPage === 'settings' && <SettingsPage user={user} />}
        </main>
      </div>
    </div>
  );
}

// Login Screen Component
function LoginScreen({ onLogin, quickLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    await onLogin(email, password);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-indigo-900 to-purple-900 flex items-center justify-center p-4">
      <div className="w-full max-w-md space-y-8">
        <div className="text-center">
          <div className="mx-auto h-16 w-16 bg-white rounded-2xl flex items-center justify-center shadow-xl mb-6">
            <Building2 className="h-10 w-10 text-blue-600" />
          </div>
          <h1 className="text-3xl font-bold text-white">EAIS Platform</h1>
          <p className="mt-2 text-blue-200">Enterprise Architecture Intelligence System</p>
        </div>

        <Card className="shadow-2xl">
          <CardHeader>
            <CardTitle>Sign In</CardTitle>
            <CardDescription>Access your enterprise architecture workspace</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="password">Password</Label>
                <Input
                  id="password"
                  type="password"
                  placeholder="Enter your password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
              <Button type="submit" className="w-full" disabled={loading}>
                {loading ? 'Signing in...' : 'Sign In'}
              </Button>
            </form>

            <div className="mt-6">
              <div className="relative">
                <div className="absolute inset-0 flex items-center">
                  <Separator className="w-full" />
                </div>
                <div className="relative flex justify-center text-xs uppercase">
                  <span className="bg-white px-2 text-slate-500">Demo Access</span>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-2 mt-4">
                {DEMO_USERS.map(user => (
                  <Button
                    key={user.role}
                    variant="outline"
                    size="sm"
                    onClick={() => quickLogin(user.role)}
                    className="text-xs"
                  >
                    {user.role.charAt(0).toUpperCase() + user.role.slice(1)}
                  </Button>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>

        <p className="text-center text-blue-200 text-sm">
          AI-Powered Enterprise Architecture • Version 2.0.0
        </p>
      </div>
    </div>
  );
}

// Dashboard Page
function DashboardPage({ stats, setCurrentPage }) {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-slate-900">Executive Dashboard</h2>
          <p className="text-slate-500">Real-time insights and analytics for your architecture portfolio</p>
        </div>
        <Button onClick={() => setCurrentPage('architecture')}>
          <Sparkles className="h-4 w-4 mr-2" />
          New Architecture
        </Button>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {[
          { label: 'Total Architectures', value: stats.totalArchitectures, change: '+3 this month', icon: Layers, color: 'blue' },
          { label: 'Avg. Compliance Score', value: stats.avgComplianceScore + '%', change: '+2.4%', icon: Shield, color: 'green' },
          { label: 'Open Risks', value: stats.openRisks, change: '-4 Critical', icon: AlertCircle, color: 'orange' },
          { label: 'Est. Annual Savings', value: stats.estimatedSavings, change: '+$150k', icon: DollarSign, color: 'purple' },
        ].map((kpi, i) => (
          <Card key={i} className="hover:shadow-lg transition-shadow">
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div className={`h-12 w-12 rounded-lg bg-${kpi.color}-100 flex items-center justify-center`}>
                  <kpi.icon className={`h-6 w-6 text-${kpi.color}-600`} />
                </div>
                <Badge variant="secondary" className="text-green-600">{kpi.change}</Badge>
              </div>
              <div className="mt-4">
                <p className="text-2xl font-bold">{kpi.value}</p>
                <p className="text-sm text-slate-500">{kpi.label}</p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Recent Activity</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {[
                { action: 'Architecture Generated', project: 'E-commerce Platform v2', time: '2 hours ago', status: 'completed' },
                { action: 'Compliance Assessment', project: 'Healthcare System', time: '5 hours ago', status: 'completed' },
                { action: 'Business Analysis', project: 'FinTech Migration', time: '1 day ago', status: 'completed' },
              ].map((activity, i) => (
                <div key={i} className="flex items-center justify-between p-3 bg-slate-50 rounded-lg">
                  <div className="flex items-center gap-3">
                    <CheckCircle className="h-5 w-5 text-green-500" />
                    <div>
                      <p className="font-medium">{activity.action}</p>
                      <p className="text-sm text-slate-500">{activity.project}</p>
                    </div>
                  </div>
                  <span className="text-sm text-slate-400">{activity.time}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <Button className="w-full justify-start" variant="outline" onClick={() => setCurrentPage('architecture')}>
              <Layers className="h-4 w-4 mr-2" />
              Generate Architecture
            </Button>
            <Button className="w-full justify-start" variant="outline" onClick={() => setCurrentPage('compliance')}>
              <Shield className="h-4 w-4 mr-2" />
              Run Compliance Check
            </Button>
            <Button className="w-full justify-start" variant="outline" onClick={() => setCurrentPage('business')}>
              <TrendingUp className="h-4 w-4 mr-2" />
              Business Analysis
            </Button>
            <Button className="w-full justify-start" variant="outline" onClick={() => setCurrentPage('reports')}>
              <FileText className="h-4 w-4 mr-2" />
              Generate Report
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

// Architecture Generator Page
function ArchitecturePage({ form, setForm, onGenerate, loading, progress, status, result }) {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Architecture Generator</h2>
        <p className="text-slate-500">Transform business requirements into production-ready architectures</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Input Form */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Target className="h-5 w-5" />
              Requirements Input
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label>Project Name</Label>
              <Input
                placeholder="e.g., E-commerce Platform v2"
                value={form.projectName}
                onChange={(e) => setForm({ ...form, projectName: e.target.value })}
              />
            </div>

            <div className="space-y-2">
              <Label>Business Objectives *</Label>
              <Textarea
                placeholder="e.g., Modernize legacy platform, reduce costs by 30%, improve scalability..."
                className="min-h-[100px]"
                value={form.businessObjectives}
                onChange={(e) => setForm({ ...form, businessObjectives: e.target.value })}
              />
            </div>

            <div className="space-y-2">
              <Label>Technical Requirements *</Label>
              <Textarea
                placeholder="e.g., Microservices architecture, 99.99% availability, sub-100ms latency..."
                className="min-h-[100px]"
                value={form.technicalRequirements}
                onChange={(e) => setForm({ ...form, technicalRequirements: e.target.value })}
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label>Industry Domain</Label>
                <Select value={form.domain} onValueChange={(v) => setForm({ ...form, domain: v })}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select domain" />
                  </SelectTrigger>
                  <SelectContent>
                    {EAIS_CONFIG.domains.map(d => (
                      <SelectItem key={d} value={d}>{d}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label>Cloud Provider</Label>
                <Select value={form.cloudProvider} onValueChange={(v) => setForm({ ...form, cloudProvider: v })}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select provider" />
                  </SelectTrigger>
                  <SelectContent>
                    {EAIS_CONFIG.cloudProviders.map(p => (
                      <SelectItem key={p} value={p}>{p}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>

            <div className="space-y-2">
              <Label>Compliance Frameworks</Label>
              <div className="grid grid-cols-2 gap-2">
                {EAIS_CONFIG.complianceFrameworks.map(fw => (
                  <div key={fw.id} className="flex items-center space-x-2">
                    <Checkbox
                      id={fw.id}
                      checked={form.complianceRequirements.includes(fw.id)}
                      onCheckedChange={(checked) => {
                        if (checked) {
                          setForm({ ...form, complianceRequirements: [...form.complianceRequirements, fw.id] });
                        } else {
                          setForm({ ...form, complianceRequirements: form.complianceRequirements.filter(r => r !== fw.id) });
                        }
                      }}
                    />
                    <label htmlFor={fw.id} className="text-sm">{fw.name}</label>
                  </div>
                ))}
              </div>
            </div>

            <Button 
              onClick={onGenerate} 
              disabled={loading || !form.businessObjectives || !form.technicalRequirements}
              className="w-full"
            >
              {loading ? (
                <>
                  <Zap className="h-4 w-4 mr-2 animate-pulse" />
                  Generating...
                </>
              ) : (
                <>
                  <Sparkles className="h-4 w-4 mr-2" />
                  Generate Architecture
                </>
              )}
            </Button>
          </CardContent>
        </Card>

        {/* Results */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Layers className="h-5 w-5" />
              Generated Architecture
            </CardTitle>
          </CardHeader>
          <CardContent>
            {loading ? (
              <div className="space-y-4">
                <div className="text-center py-8">
                  <div className="animate-spin h-12 w-12 border-4 border-blue-600 border-t-transparent rounded-full mx-auto mb-4" />
                  <p className="text-lg font-medium">{status}</p>
                </div>
                <Progress value={progress} className="h-2" />
              </div>
            ) : result ? (
              <ScrollArea className="h-[500px]">
                <div className="prose prose-sm max-w-none">
                  <pre className="whitespace-pre-wrap text-sm bg-slate-50 p-4 rounded-lg">
                    {result.architecture}
                  </pre>
                </div>
              </ScrollArea>
            ) : (
              <div className="text-center py-16 text-slate-400">
                <Layers className="h-16 w-16 mx-auto mb-4 opacity-50" />
                <p>Your generated architecture will appear here</p>
                <p className="text-sm">Fill in the requirements and click Generate</p>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

// Compliance Page
function CompliancePage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Compliance & Security</h2>
        <p className="text-slate-500">Automated regulatory assessment and security posture monitoring</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Framework Assessment</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {EAIS_CONFIG.complianceFrameworks.map(fw => (
                <div key={fw.id} className="p-4 border rounded-lg hover:bg-slate-50 cursor-pointer">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <Shield className="h-8 w-8 text-blue-600" />
                      <div>
                        <p className="font-medium">{fw.name}</p>
                        <p className="text-sm text-slate-500">{fw.description}</p>
                      </div>
                    </div>
                    <Badge variant="outline">
                      {Math.floor(Math.random() * 20) + 80}%
                    </Badge>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Compliance Scores</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            {[
              { label: 'Data Protection', score: 95 },
              { label: 'Access Control', score: 88 },
              { label: 'Audit Logging', score: 92 },
              { label: 'Encryption', score: 90 },
            ].map((item, i) => (
              <div key={i}>
                <div className="flex justify-between text-sm mb-1">
                  <span>{item.label}</span>
                  <span className="font-medium">{item.score}%</span>
                </div>
                <Progress value={item.score} className="h-2" />
              </div>
            ))}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

// Business Analysis Page
function BusinessPage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Business Analysis</h2>
        <p className="text-slate-500">TCO modeling, ROI projections, and strategic business impact</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          { label: '5-Year TCO', value: '$2.4M', change: 'Estimated' },
          { label: 'Annual ROI', value: '156%', change: '+20%' },
          { label: 'Payback Period', value: '14 Months', change: '-2 Months' },
        ].map((kpi, i) => (
          <Card key={i}>
            <CardContent className="pt-6">
              <p className="text-sm text-slate-500">{kpi.label}</p>
              <p className="text-3xl font-bold mt-2">{kpi.value}</p>
              <Badge variant="secondary" className="mt-2">{kpi.change}</Badge>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Financial Projections</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-[300px] flex items-center justify-center bg-slate-50 rounded-lg">
            <div className="text-center text-slate-400">
              <BarChart3 className="h-16 w-16 mx-auto mb-4 opacity-50" />
              <p>Financial projection charts will appear here</p>
              <p className="text-sm">Connect with an architecture to see analysis</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

// Knowledge Graph Page
function KnowledgePage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Enterprise Knowledge Graph</h2>
        <p className="text-slate-500">Semantic exploration of architectural patterns and relationships</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="lg:col-span-2">
          <CardContent className="pt-6">
            <div className="h-[400px] bg-slate-50 rounded-lg flex items-center justify-center">
              <div className="text-center text-slate-400">
                <Brain className="h-20 w-20 mx-auto mb-4 opacity-50" />
                <p className="text-lg font-medium">Knowledge Graph Visualization</p>
                <p className="text-sm">Interactive entity relationship map</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Popular Patterns</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {['Microservices', 'Event-Driven', 'Serverless', 'CQRS', 'Hexagonal'].map((pattern, i) => (
                <div key={i} className="flex items-center justify-between p-2 bg-slate-50 rounded">
                  <span className="font-medium">{pattern}</span>
                  <ChevronRight className="h-4 w-4 text-slate-400" />
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

// Reports Page
function ReportsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Reports & Analytics</h2>
        <p className="text-slate-500">Generate and export professional reports for stakeholders</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {[
          { title: 'Executive Summary', desc: 'High-level overview of architecture decisions', icon: FileText },
          { title: 'Compliance Audit', desc: 'Detailed mapping of controls to requirements', icon: Shield },
          { title: 'Technical Specification', desc: 'Component breakdown and infrastructure blueprints', icon: Layers },
          { title: 'Financial ROI Report', desc: 'TCO modeling and financial projections', icon: DollarSign },
        ].map((report, i) => (
          <Card key={i} className="hover:shadow-lg transition-shadow cursor-pointer">
            <CardContent className="pt-6">
              <div className="flex items-start gap-4">
                <div className="h-12 w-12 bg-blue-100 rounded-lg flex items-center justify-center">
                  <report.icon className="h-6 w-6 text-blue-600" />
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold">{report.title}</h3>
                  <p className="text-sm text-slate-500">{report.desc}</p>
                  <Button size="sm" variant="outline" className="mt-3">
                    Generate PDF
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}

// Settings Page
function SettingsPage({ user }) {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Settings</h2>
        <p className="text-slate-500">Manage application configuration and user preferences</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Profile Settings</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label>Name</Label>
                <Input defaultValue={user?.name} />
              </div>
              <div className="space-y-2">
                <Label>Email</Label>
                <Input defaultValue={user?.email} disabled />
              </div>
            </div>
            <div className="space-y-2">
              <Label>Role</Label>
              <Input defaultValue={user?.role} disabled className="capitalize" />
            </div>
            <Button>Save Changes</Button>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>System Info</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="flex justify-between">
              <span className="text-slate-500">Version</span>
              <span className="font-medium">2.0.0</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-500">AI Model</span>
              <span className="font-medium">GPT-4o</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-500">Status</span>
              <Badge className="bg-green-100 text-green-700">Healthy</Badge>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
