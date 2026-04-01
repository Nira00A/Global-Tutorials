import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { UserModule } from './user/user.module';
import { SupabaseService } from './supabase/supabase.service';
import { UserService } from './supabase/user/user.service';

@Module({
  imports: [AuthModule, UserModule],
  controllers: [AppController],
  providers: [AppService, SupabaseService, UserService],
})
export class AppModule {}
