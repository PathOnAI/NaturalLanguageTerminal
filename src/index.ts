#!/usr/bin/env node
import { runCLI } from './cli';

const args = process.argv.slice(2);
runCLI(args).catch(error => {
  console.error('Unhandled error:', error);
  process.exit(1);
});