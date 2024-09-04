// src/config.ts
import dotenv from 'dotenv';
import OpenAI from 'openai';
import fs from 'fs';
import path from 'path';
import os from 'os';

dotenv.config();

export const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

interface Config {
    brain: boolean;
    executionTimeout: number;
  }
  
  const CONFIG_FILE = path.join(os.homedir(), '.nlsrc');
  
  const DEFAULT_CONFIG: Config = {
    brain: false,
    executionTimeout: 10000, // 10 seconds default
  };
  
  export function loadConfig(): Config {
    try {
      const configData = fs.readFileSync(CONFIG_FILE, 'utf8');
      return { ...DEFAULT_CONFIG, ...JSON.parse(configData) };
    } catch (error) {
      return DEFAULT_CONFIG;
    }
  }
  
  export function saveConfig(config: Config): void {
    fs.writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2));
  }