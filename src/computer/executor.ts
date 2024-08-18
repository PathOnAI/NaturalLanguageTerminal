import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export async function executeCommand(command: string): Promise<string> {
    try {
      const { stdout, stderr } = await execPromise(command);
      if (stderr) {
        console.error(`Command execution error: ${stderr}`);
      }
      return stdout.trim();
    } catch (error) {
      console.error(`Error executing command: ${error}`);
      return '';
    }
  }