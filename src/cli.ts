import { interpretCommand, explainCommands } from './ai.js';
import { executeCommand } from './shell.js';
import * as readline from 'readline';
import chalk from 'chalk';
import ora from 'ora';
import figlet from 'figlet';
import gradient from 'gradient-string';
import { loadConfig, saveConfig } from './config.js';
import { setupCommand } from './setup.js';
import { ProgressTracker } from './progressTracker.js';

const MAX_RETRIES = 3;

export async function runCLI(args: string[]): Promise<void> {
  console.log(gradient.pastel.multiline(figlet.textSync('NLS', { horizontalLayout: 'full' })));
  
  if (args.length === 0) {
    console.log(chalk.yellow('Usage: nls <your natural language command>'));
    console.log(chalk.yellow('       nls setup'));
    console.log(chalk.dim('Example: nls list all JavaScript files in the current directory'));
    process.exit(0);
  }

  if (args[0] === 'setup') {
    await setupCommand();
    process.exit(0);
  }

  const input = args.join(' ');
  const config = loadConfig();

  try {
    const spinner = ora('Interpreting your command...').start();
    let shellCommands = await interpretCommand(input);
    spinner.succeed(chalk.green('Command(s) interpreted successfully!'));

    console.log(chalk.cyan('Interpreted command(s):'));
    shellCommands.forEach((cmd, index) => {
      console.log(chalk.bold(`${index + 1}. ${cmd}`));
    });
    
    if (config.brain) {
      await executeCommandsWithRetry(shellCommands, config.executionTimeout);
    } else {
      await promptAndExecuteCommands(shellCommands, config.executionTimeout);
    }
  } catch (error) {
    console.error(chalk.red('An error occurred:'), error);
  } finally {
    process.exit(0);
  }
}

async function promptAndExecuteCommands(shellCommands: string[], timeout: number): Promise<void> {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve) => {
    rl.question(chalk.yellow('Execute these commands? ') + chalk.green('(y)es') + '/' + chalk.red('(n)o') + '/' + chalk.blue('(e)xplain') + ': ', async (answer) => {
      if (answer.toLowerCase() === 'y') {
        await executeCommandsWithRetry(shellCommands, timeout);
      } else if (answer.toLowerCase() === 'e') {
        const explanation = await explainCommands(shellCommands);
        console.log(chalk.cyan('\nExplanation:'));
        console.log(explanation);
        await promptAndExecuteCommands(shellCommands, timeout);
      } else {
        console.log(chalk.yellow('Command execution cancelled.'));
      }
      rl.close();
      resolve();
    });
  });
}

async function executeCommandsWithRetry(shellCommands: string[], timeout: number, retryCount = 0): Promise<void> {
    for (const [index, command] of shellCommands.entries()) {
      console.log(chalk.cyan(`\nExecuting command ${index + 1} of ${shellCommands.length}:`));
      console.log(chalk.bold(command));
  
      const executionSpinner = ora('Executing command...').start();
      const progressTracker = new ProgressTracker();
  
      let timeoutId: NodeJS.Timeout | null = null;
      let commandAborted = false;
  
      try {
        progressTracker.start();
  
        const output = await Promise.race([
          new Promise<string>((resolve, reject) => {
            executeCommand(command, (chunk) => {
              progressTracker.update(chunk);
            }).then(resolve).catch(reject);
          }),
          new Promise<never>((_, reject) => {
            timeoutId = setTimeout(() => {
              commandAborted = true;
              reject(new Error('Command execution timed out'));
            }, timeout);
          })
        ]);
  
        if (timeoutId) clearTimeout(timeoutId);
        progressTracker.stop();
        executionSpinner.succeed(chalk.green('Command executed successfully!'));
        
        if (output) {
          console.log(chalk.bold('\nOutput:'));
          console.log(chalk.dim('----------------------------------------'));
          console.log(output);
          console.log(chalk.dim('----------------------------------------'));
        } else {
          console.log(chalk.yellow('\nCommand executed successfully, but produced no output.'));
        }
      } catch (error) {
        if (timeoutId) clearTimeout(timeoutId);
        progressTracker.stop();
        executionSpinner.fail(chalk.red('Error executing command'));
  
        if (typeof error === 'object' && error !== null) {
          console.error(chalk.red('Error details:'), (error as Error).message);
          if ('stderr' in error && typeof error.stderr === 'string') {
            console.error(chalk.red('System error message:'));
            console.error(chalk.dim('----------------------------------------'));
            console.error(error.stderr);
            console.error(chalk.dim('----------------------------------------'));
          }
        } else {
          console.error(chalk.red('An unknown error occurred'));
        }
  
        if (commandAborted || retryCount >= MAX_RETRIES) {
          if (commandAborted) {
            console.log(chalk.yellow('Command execution timed out and was aborted.'));
          } else {
            console.log(chalk.red(`Command failed after ${MAX_RETRIES} retries.`));
          }
          break;  // Stop executing further commands
        } else {
          console.log(chalk.yellow(`Retrying command (Attempt ${retryCount + 2} of ${MAX_RETRIES + 1})...`));
          await executeCommandsWithRetry([command], timeout, retryCount + 1);
        }
      }
    }
  }