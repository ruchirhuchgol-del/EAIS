/**
 * EAIS Authentication API
 * POST /api/auth/login - Authenticate user
 */

import { authenticateUser } from '@/lib/eais/auth';
import { NextResponse } from 'next/server';

export async function POST(request) {
  try {
    const body = await request.json();
    const { email, password } = body;
    
    if (!email || !password) {
      return NextResponse.json(
        { success: false, error: 'Email and password required' },
        { status: 400 }
      );
    }
    
    const result = authenticateUser(email, password);
    
    if (!result.success) {
      return NextResponse.json(
        { success: false, error: result.error },
        { status: 401 }
      );
    }
    
    return NextResponse.json({
      success: true,
      user: result.user,
      token: result.token,
      permissions: result.permissions,
    });
    
  } catch (error) {
    return NextResponse.json(
      { success: false, error: 'Authentication failed' },
      { status: 500 }
    );
  }
}
