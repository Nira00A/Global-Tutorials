import { Module } from '@nestjs/common';
import { UserService } from './user.service';
import { SupabaseService } from './supabase/supabase.service';

@Module({
  providers: [UserService, SupabaseService],
  exports: [UserService],
})
export class UserModule {}
