import { exec, ChildProcess } from 'child_process';

export function executeCommand(command: string, progressCallback?: (chunk: string | Buffer) => void): Promise<string> {
    return new Promise((resolve, reject) => {
      let output = '';
      let errorOutput = '';
      const childProcess = exec(command, { maxBuffer: 1024 * 1024 * 10 }) // 10 MB buffer
  
      childProcess.stdout?.on('data', (data) => {
        output += data;
        if (progressCallback) progressCallback(data);
      });
  
      childProcess.stderr?.on('data', (data) => {
        errorOutput += data;
        if (progressCallback) progressCallback(data);
      });
  
      childProcess.on('error', (error) => {
        reject({ message: `Error: ${error.message}`, stderr: errorOutput });
      });
  
      childProcess.on('exit', (code) => {
        if (code === 0) {
          resolve(output);
        } else {
          reject({ message: `Command exited with code ${code}`, stderr: errorOutput });
        }
      });
    });
  }