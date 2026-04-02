import { Injectable } from '@nestjs/common';

@Injectable()
export class UserService {
  registerUser() {
    return 'User profile created successfully';
  }

  getAllUsers() {
    return 'List of all users';
  }
}
