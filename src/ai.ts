// src/ai.ts
import { openai } from './config';

export async function interpretCommand(input: string): Promise<string> {
  const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: [
      { role: 'system', content: 'You are a helpful assistant that translates natural language commands into shell commands. Respond only with the shell command, nothing else.' },
      { role: 'user', content: `Translate the following natural language command to a shell command: "${input}"` }
    ],
  });

  return response.choices[0].message?.content || ''
}