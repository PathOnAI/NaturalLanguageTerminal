import chalk from 'chalk';
import inquirer from 'inquirer';
import { loadConfig, saveConfig } from './config.js';

export async function setupCommand(): Promise<void> {
  console.log(chalk.bold('NLS Setup'));
  
  const currentConfig = loadConfig();

  const answers = await inquirer.prompt([
    {
      type: 'confirm',
      name: 'brain',
      message: 'Enable automatic command execution (brain mode)?',
      default: currentConfig.brain,
    },
    {
      type: 'number',
      name: 'executionTimeout',
      message: 'Set command execution timeout (in seconds):',
      default: currentConfig.executionTimeout / 1000,
      validate: (value) => (value! > 0) || 'Please enter a positive number',
    },
  ]);

  const newConfig = {
    ...currentConfig,
    ...answers,
    executionTimeout: answers.executionTimeout * 1000, // Convert to milliseconds
  };

  saveConfig(newConfig);
  console.log(chalk.green('Setup complete. Configuration saved.'));
}