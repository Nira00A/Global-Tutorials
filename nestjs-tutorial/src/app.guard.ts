import {
  Injectable,
  CanActivate,
  ExecutionContext,
  UnauthorizedException,
} from '@nestjs/common';
import { supabase } from './supabase/supabase';

@Injectable()
export class SupabaseGuard implements CanActivate {
  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const authHeader = request.headers.authorization;

    if (!authHeader) {
      throw new UnauthorizedException('No authorization header found');
    }

    // Extract the JWT (Format: "Bearer <token>")
    const token = authHeader.split(' ')[1];

    // Validate the token with Supabase
    const {
      data: { user },
      error,
    } = await supabase.auth.getUser(token);

    if (error || !user) {
      throw new UnauthorizedException('Invalid or expired token');
    }

    // Attach the user to the request so your controller can use their ID
    request.user = user;
    return true;
  }
}
