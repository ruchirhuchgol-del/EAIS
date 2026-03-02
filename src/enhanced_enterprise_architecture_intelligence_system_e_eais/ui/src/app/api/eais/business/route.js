/**
 * EAIS Business Analysis API
 * POST /api/eais/business - Generate business impact analysis
 */

import { generateBusinessAnalysis } from '@/lib/eais/orchestrator';
import { NextResponse } from 'next/server';

export async function POST(request) {
  try {
    const body = await request.json();
    const { architecture, investmentParams } = body;
    
    if (!architecture) {
      return NextResponse.json(
        { success: false, error: 'Architecture design is required' },
        { status: 400 }
      );
    }
    
    // Generate business analysis using AI
    const result = await generateBusinessAnalysis(architecture, investmentParams || {});
    
    if (!result.success) {
      return NextResponse.json(
        { success: false, error: result.error },
        { status: 500 }
      );
    }
    
    return NextResponse.json({
      success: true,
      analysis: result.analysis,
      parameters: result.parameters,
      agent: result.agent,
      timestamp: result.timestamp,
    });
    
  } catch (error) {
    console.error('Business Analysis API error:', error);
    return NextResponse.json(
      { success: false, error: 'Business analysis failed' },
      { status: 500 }
    );
  }
}
