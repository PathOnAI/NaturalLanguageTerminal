// src/ai.ts
import { openai } from './config.js';
import { getOSInfo, getCurrentDirectory } from './computer.js';

export async function interpretCommand(input: string): Promise<string[]> {
  const osInfo = getOSInfo();
  const currentDir = getCurrentDirectory();

  const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: [
      {
        role: 'system',
        content: `You are a helpful assistant that translates natural language commands into shell commands. 
                    Consider the following system information when generating commands:
                    ${osInfo}
                    Current directory: ${currentDir}
                    
                    Respond with the appropriate shell command(s) for the given OS and shell.
                    If multiple commands are needed, separate them with a newline character.
                    Ensure the commands are safe to execute and won't cause unintended system changes.
                    If a command requires elevated privileges, prefix it with 'sudo' on Unix-like systems.
                    Do not include any explanations or markdown formatting in your response.`
      },
      // For destructive operations, include appropriate safeguards or confirmations.
      // Additional prompt safeguard?
      { role: 'user', content: `Translate the following natural language command to shell command(s): "${input}"` }
    ],
    temperature: 0.7,
    max_tokens: 250,
  });

  const content = response.choices[0].message?.content?.trim() || '';
  return content.split('\n').map(cmd => cmd.trim()).filter(cmd => cmd !== '');
}

export async function explainCommands(commands: string[]): Promise<string> {
  const commandsString = commands.join('\n');
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      {
        role: 'system',
        content: 'You are a helpful assistant that explains shell commands in simple terms.'
      },
      { role: 'user', content: `Explain the following shell command(s) in simple terms:\n${commandsString}` }
    ],
    temperature: 0.7,
    max_tokens: 300,
  });

  return response.choices[0].message?.content?.trim() || '';
}

export async function generateGitCommitMessage(diff: string): Promise<string> {
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      {
        role: 'system',
        content: 'You are a helpful assistant that creates proper git messages.'
      },
      { role: 'user', content: `Generate a concise git commit message based on the following diff:\n\n${diff}\n\nDo not include any explanations or markdown formatting in your response, just the commit message.` }
    ],
    temperature: 0.7,
    max_tokens: 50,
  });

  return response.choices[0].message?.content?.trim() || '';
}

