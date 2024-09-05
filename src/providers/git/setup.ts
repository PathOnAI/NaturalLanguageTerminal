import * as path from 'path';

const activationFilePath = path.join(process.cwd(), '.git-auto-commit-active');

async function isActivated(): Promise<boolean> {
  try {
    const { stdout } = await execAsync('git config --get alias.auto-commit');
    return stdout.trim() !== '';
  } catch (error) {
    return false;
  }
}

async function activate() {
  if (await isActivated()) {
    console.log('Git auto-commit is already activated for this repository.');
    return;
  }
  
  const scriptPath = path.resolve(__filename);
  await execAsync(`git config alias.auto-commit "!node ${scriptPath} execute-auto-commit"`);
  console.log('Git auto-commit activated for this repository.');
}

async function deactivate() {
  if (!await isActivated()) {
    console.log('Git auto-commit is not activated for this repository.');
    return;
  }
  
  await execAsync('git config --unset alias.auto-commit');
  console.log('Git auto-commit deactivated for this repository.');
}