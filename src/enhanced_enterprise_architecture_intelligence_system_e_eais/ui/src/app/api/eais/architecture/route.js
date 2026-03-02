/**
 * EAIS Architecture Generation API
 * POST /api/eais/architecture - Generate architecture design
 */

import { generateArchitecture } from '@/lib/eais/orchestrator';
import { saveArchitecture, getArchitectures } from '@/lib/eais/store';
import { NextResponse } from 'next/server';

export async function POST(request) {
  try {
    const body = await request.json();
    const {
      businessObjectives,
      technicalRequirements,
      complianceRequirements,
      domain,
      cloudProvider,
      projectName,
    } = body;

    if (!businessObjectives || !technicalRequirements) {
      return NextResponse.json(
        { success: false, error: 'Business objectives and technical requirements are required' },
        { status: 400 }
      );
    }

    // Generate architecture using AI
    const result = await generateArchitecture({
      businessObjectives,
      technicalRequirements,
      complianceRequirements,
      domain,
      cloudProvider,
    });

    if (!result.success) {
      return NextResponse.json(
        { success: false, error: result.error },
        { status: 500 }
      );
    }

    // Save to store
    // NOTE: In production, we'd get the userId from the session
    const saved = await saveArchitecture({
      projectName: projectName || 'Enterprise Architecture',
      architecture: result.architecture,
      requirements: {
        businessObjectives,
        technicalRequirements,
        complianceRequirements,
        domain,
        cloudProvider,
      },
      agent: result.agent,
      userId: body.userId || 'placeholder-user-id',
    });

    return NextResponse.json({
      success: true,
      id: saved.id,
      architecture: result.architecture,
      agent: result.agent,
      timestamp: result.timestamp,
    });

  } catch (error) {
    console.error('Architecture API error:', error);
    return NextResponse.json(
      { success: false, error: 'Architecture generation failed' },
      { status: 500 }
    );
  }
}

export async function GET() {
  const architectures = getArchitectures();

  return NextResponse.json({
    success: true,
    architectures,
    count: architectures.length,
  });
}
