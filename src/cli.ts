// src/cli.ts
import { interpretCommand } from './ai';
import { executeCommand } from './shell';
import * as readline from 'readline';

export async function runCLI(args: string[]): Promise<void> {
  if (args.length === 0) {
    console.log('Usage: nls <your natural language command>');
    process.exit(0);
  }

  const input = args.join(' ');

  try {
    const shellCommand = await interpretCommand(input);
    console.log(`Interpreted command: ${shellCommand}`);
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    rl.question('Execute this command? (y/n): ', async (answer) => {
      if (answer.toLowerCase() === 'y') {
        try {
          const output = await executeCommand(shellCommand);
          console.log('Output:');
          console.log(output);
        } catch (error) {
          console.error('Error executing command:', error);
        }
      } else {
        console.log('Command execution cancelled.');
      }
      
      rl.close();
      process.exit(0);
    });
  } catch (error) {
    console.error('An error occurred:', error);
    process.exit(1);
  }
}