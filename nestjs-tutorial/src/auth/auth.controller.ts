import { Body, Controller, Get, Post, UseGuards } from '@nestjs/common';
import { AuthService } from './auth.service';
import { RegisterDto } from '../user/dto/registerUser.dto';
import { SupabaseGuard } from '../app.guard';
import { Role } from './roles.enum';
import { Roles } from './role.decorator';
import { RolesGuard } from 'src/auth.roles.guard';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @Post('register')
  register(@Body() registerUserDto: RegisterDto) {
    // Logic for registering a user would go here
    const result = this.authService.registerUser(registerUserDto);
    return result;
  }

  @UseGuards(SupabaseGuard)
  @Get('get-all-users')
  getAllUsers() {
    return this.authService.getAllUsers();
  }

  @UseGuards(SupabaseGuard, RolesGuard)
  @Roles(Role.Admin)
  @Post('create-user')
  createUser(@Body() createUserDto: RegisterDto) {
    return this.authService.createUser(createUserDto);
  }
}
