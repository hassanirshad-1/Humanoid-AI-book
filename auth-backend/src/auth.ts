import { betterAuth } from 'better-auth';
import { prismaAdapter } from 'better-auth/adapters/prisma';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: 'postgresql',
  }),
  baseURL: process.env.BETTER_AUTH_BASE_URL || "http://localhost:3001/api/auth",
  secret: process.env.BETTER_AUTH_SECRET || "your-ultra-secure-secret-key-at-least-32-chars",
  trustedOrigins: ["http://localhost:3000"],
  user: {
    additionalFields: {
      skill_level: {
        type: 'string',
        required: false,
      },
      operating_system: {
        type: 'string',
        required: false,
      },
    },
  },
  emailAndPassword: {
    enabled: true,
  },
});