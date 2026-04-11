import { Injectable } from '@nestjs/common';
import { PrismaService } from './prisma/prisma.service';

@Injectable()
export class AppService {
  constructor(private readonly prisma: PrismaService) {}

  async getHello(): Promise<string> {
    return 'Hello World!';
  }

  async getUsers(): Promise<any[]> {
    return this.prisma.user.findMany();
  }
}
