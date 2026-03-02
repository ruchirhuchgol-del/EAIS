/**
 * EAIS Statistics API
 * GET /api/eais/statistics - Get system statistics
 */

import { getStatistics } from '@/lib/eais/store';
import { NextResponse } from 'next/server';

export async function GET() {
  try {
    const stats = getStatistics();
    
    return NextResponse.json({
      success: true,
      statistics: {
        ...stats,
        systemHealth: 'healthy',
        uptime: process.uptime(),
        version: '2.0.0',
      },
    });
    
  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Failed to fetch statistics' },
      { status: 500 }
    );
  }
}
