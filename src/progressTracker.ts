import { SingleBar } from 'cli-progress';
import chalk from 'chalk';

export class ProgressTracker {
  private bar: SingleBar;
  private startTime: number;
  private lastUpdateTime: number;
  private totalBytes: number = 0;

  constructor() {
    this.bar = new SingleBar({
      format: 'Progress |' + chalk.cyan('{bar}') + '| {percentage}% || {value}/{total} Bytes || Speed: {speed} KB/s',
      barCompleteChar: '\u2588',
      barIncompleteChar: '\u2591',
      hideCursor: true,
      stopOnComplete: true,
    });
    this.startTime = Date.now();
    this.lastUpdateTime = this.startTime;
  }

  start(): void {
    this.bar.start(100, 0, {
      speed: "N/A"
    });
  }

  update(chunk: string | Buffer): void {
    const chunkSize = Buffer.byteLength(chunk);
    this.totalBytes += chunkSize;
    const currentTime = Date.now();
    const timeDiff = (currentTime - this.lastUpdateTime) / 1000; // in seconds
    const speed = timeDiff > 0 ? (chunkSize / 1024 / timeDiff).toFixed(2) : 'N/A';
    
    this.bar.setTotal(this.totalBytes);
    this.bar.update(this.totalBytes, {
      speed: speed,
    });
    
    this.lastUpdateTime = currentTime;
  }

  stop(): void {
    this.bar.stop();
    const totalTime = (Date.now() - this.startTime) / 1000; // in seconds
    const averageSpeed = (this.totalBytes / 1024 / totalTime).toFixed(2);
    console.log(chalk.cyan(`\nTotal: ${this.totalBytes} Bytes | Average Speed: ${averageSpeed} KB/s | Time: ${totalTime.toFixed(2)}s`));
  }
}