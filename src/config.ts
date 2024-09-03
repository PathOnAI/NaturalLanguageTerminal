// src/config.ts
import dotenv from 'dotenv';
import OpenAI from 'openai';

dotenv.config();

export const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});