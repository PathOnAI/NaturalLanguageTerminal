import os from 'os';
import { execSync } from 'child_process';

export function getOSInfo(): string {
    const platform = os.platform();
    const release = os.release();
    const type = os.type();
    
    let shellInfo = '';
    try {
      if (platform === 'win32') {
        shellInfo = execSync('echo %SHELL%').toString().trim();
      } else {
        shellInfo = execSync('echo $SHELL').toString().trim();
      }
    } catch (error) {
      shellInfo = 'Unknown shell';
    }
  
    return `OS: ${type} ${platform} ${release}, Shell: ${shellInfo}`;
  }
  
  export function getCurrentDirectory(): string {
    return process.cwd();
  }