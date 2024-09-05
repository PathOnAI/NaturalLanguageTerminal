import { generateGitCommitMessage } from "../ai.js";
import { executeCommand } from "../shell.js";

async function getGitDiff(): Promise<string> {
    try {
      const stdout = await executeCommand('git diff');
      return stdout;
    } catch (error) {
      console.error('Error getting git diff:', error);
      return '';
    }
  }


  async function autoCommit() {
    const diff = await getGitDiff();
    if (!diff) {
      console.log('No changes to commit.');
      return;
    }
  
    const commitMessage = await generateGitCommitMessage(diff);
    try {
      await executeCommand('git add .');
      await executeCommand(`git commit -m "${commitMessage}"`);
      console.log('Changes committed successfully.');
    } catch (error) {
      console.error('Error committing changes:', error);
    }
  }