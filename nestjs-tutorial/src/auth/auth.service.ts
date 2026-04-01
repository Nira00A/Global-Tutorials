import { Injectable, Post } from '@nestjs/common';
import { RegisterDto } from '../user/dto/registerUser.dto';
import { UserService } from '../user/user.service';

@Injectable()
export class AuthService {
    constructor(private readonly userService: UserService) {}

    registerUser(registerUserDto: RegisterDto) {
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
        
        return { message: 'User registered successfully' };
    }
}
