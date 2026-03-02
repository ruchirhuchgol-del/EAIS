/**
 * EAIS Knowledge Graph API
 * GET /api/eais/knowledge - Get knowledge entities
 * POST /api/eais/knowledge - Search knowledge
 */

import { 
  getKnowledgeEntities, 
  getKnowledgeRelationships, 
  searchKnowledge 
} from '@/lib/eais/store';
import { NextResponse } from 'next/server';

export async function GET() {
  try {
    const entities = getKnowledgeEntities();
    const relationships = getKnowledgeRelationships();
    
    return NextResponse.json({
      success: true,
      entities,
      relationships,
      stats: {
        totalEntities: entities.length,
        totalRelationships: relationships.length,
      },
    });
    
  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Failed to fetch knowledge graph' },
      { status: 500 }
    );
  }
}

export async function POST(request) {
  try {
    const body = await request.json();
    const { query } = body;
    
    if (!query) {
      return NextResponse.json(
        { success: false, error: 'Search query required' },
        { status: 400 }
      );
    }
    
    const results = searchKnowledge(query);
    
    return NextResponse.json({
      success: true,
      query,
      results,
      count: results.length,
    });
    
  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Knowledge search failed' },
      { status: 500 }
    );
  }
}
