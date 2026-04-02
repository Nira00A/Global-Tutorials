import { Injectable, Post } from '@nestjs/common';
import { RegisterDto } from '../user/dto/registerUser.dto';
import { UserService } from '../user/user.service';
import { supabase } from '../supabase/supabase';

@Injectable()
export class AuthService {
  constructor(private readonly userService: UserService) {}

  async registerUser(registerUserDto: RegisterDto) {
    console.log('Registering user:', registerUserDto);
    console.log('UserService:', this.userService.registerUser);
    // Logic for registering a user would go here
    /**
     * 1. Check if the user already exists in the database
     * 2. Hash the user's password
     * 3. Save the user to the database
     * 4. Generate a JWT token for the user
     * 5. Return the token in response
     */
    const { data, error } = await supabase.from('users').select('*');
    console.log('Supabase data:', data);
    console.log('Supabase error:', error);
    return { message: 'User registered successfully' };
  }

  async getAllUsers() {
    const { data, error } = await supabase.from('users').select('*');

    if (error) {
      console.error('Error fetching users:', error);
      return { message: 'Error fetching users', error };
    }

    return {
      message: this.userService.getAllUsers(),
      data: data,
      error: error || 'null',
    };
  }

  async createUser(createUserDto: RegisterDto) {
    const { email, password } = createUserDto;
  }
}
