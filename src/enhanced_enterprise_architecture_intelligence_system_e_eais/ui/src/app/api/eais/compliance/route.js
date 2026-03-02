/**
 * EAIS Compliance Assessment API
 * POST /api/eais/compliance - Generate compliance assessment
 */

import { generateComplianceAssessment } from '@/lib/eais/orchestrator';
import { NextResponse } from 'next/server';

export async function POST(request) {
  try {
    const body = await request.json();
    const { architecture, frameworks } = body;
    
    if (!architecture) {
      return NextResponse.json(
        { success: false, error: 'Architecture design is required' },
        { status: 400 }
      );
    }
    
    // Generate compliance assessment using AI
    const result = await generateComplianceAssessment(architecture, frameworks);
    
    if (!result.success) {
      return NextResponse.json(
        { success: false, error: result.error },
        { status: 500 }
      );
    }
    
    return NextResponse.json({
      success: true,
      assessment: result.assessment,
      frameworks: result.frameworks,
      agent: result.agent,
      timestamp: result.timestamp,
    });
    
  } catch (error) {
    console.error('Compliance API error:', error);
    return NextResponse.json(
      { success: false, error: 'Compliance assessment failed' },
      { status: 500 }
    );
  }
}
