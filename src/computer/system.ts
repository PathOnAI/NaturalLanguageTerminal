import * as os from 'os';
import * as process from 'process';

export const getCwd = () => {
    return process.cwd();
}

export const getSystemData = () => {
    const osInfo = {
        platform: process.platform,
        release: os.release(),
        type: os.type(),
        architecture: os.arch(),
        hostname: os.hostname(),
    };

    return osInfo
}