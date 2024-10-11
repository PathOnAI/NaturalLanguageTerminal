import os
import platform
import socket
import psutil
import subprocess

class SystemInfo:
    def __init__(self):
        self.os_info = platform.system()
        self.os_release = platform.release()
        self.os_version = platform.version()
        self.machine = platform.machine()
        self.processor = platform.processor()
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(socket.gethostname())

    def get_os_info(self):
        os_details = f"OS: {self.os_info} {self.os_release} ({self.os_version})"
        
        if self.os_info == "Darwin":  # macOS
            mac_version = platform.mac_ver()
            os_details += f"\nMacOS Version: {mac_version[0]}"
            os_details += f"\nArchitecture: {mac_version[2]}"
            os_details += "\nAppleScript Support: Available"
        elif self.os_info == "Windows":
            win_version = platform.win32_ver()
            os_details += f"\nWindows Version: {win_version[0]}"
            os_details += f"\nService Pack: {win_version[2]}"
            os_details += "\nPowerShell Support: Available"
        elif self.os_info == "Linux":
            try:
                distro = subprocess.check_output(["lsb_release", "-ds"]).decode().strip()
                os_details += f"\nDistribution: {distro}"
            except:
                os_details += "\nDistribution: Unable to determine"
            os_details += "\nBash Support: Available"
        
        return os_details

    def get_machine_info(self):
        return f"Machine: {self.machine}, Processor: {self.processor}"

    def get_network_info(self):
        return f"Hostname: {self.hostname}, IP: {self.ip_address}"

    def get_memory_info(self):
        mem = psutil.virtual_memory()
        return f"Total Memory: {self.bytes_to_gb(mem.total):.2f} GB, Available: {self.bytes_to_gb(mem.available):.2f} GB"

    def get_disk_info(self):
        disk = psutil.disk_usage('/')
        return f"Total Disk: {self.bytes_to_gb(disk.total):.2f} GB, Free: {self.bytes_to_gb(disk.free):.2f} GB"

    def get_current_shell(self):
        return os.environ.get('SHELL', 'Unknown')

    def get_python_version(self):
        return platform.python_version()

    def get_cpu_info(self):
        return f"CPU Cores: {psutil.cpu_count(logical=False)}, Threads: {psutil.cpu_count(logical=True)}"

    def get_gpu_info(self):
        try:
            if self.os_info == 'Windows':
                gpu_info = subprocess.check_output(['wmic', 'path', 'win32_VideoController', 'get', 'name']).decode().strip().split('\n')[1:]
            elif self.os_info == 'Darwin':  # macOS
                gpu_info = subprocess.check_output(['system_profiler', 'SPDisplaysDataType']).decode().strip().split('\n')
                gpu_info = [line.strip() for line in gpu_info if 'Chipset Model:' in line]
            else:  # Linux
                gpu_info = subprocess.check_output(['lspci', '-v']).decode().strip().split('\n')
                gpu_info = [line for line in gpu_info if 'VGA' in line or '3D' in line]
            return "\n".join(gpu_info).strip()
        except:
            return "GPU information not available"

    def get_specific_os_info(self):
        if self.os_info == "Darwin":  # macOS
            try:
                xcode_version = subprocess.check_output(["xcodebuild", "-version"]).decode().strip().split("\n")[0]
                return f"Xcode: {xcode_version}"
            except:
                return "Xcode: Not installed or unable to determine version"
        elif self.os_info == "Windows":
            try:
                powershell_version = subprocess.check_output(["powershell", "$PSVersionTable.PSVersion"]).decode().strip()
                return f"PowerShell Version: {powershell_version}"
            except:
                return "PowerShell: Unable to determine version"
        elif self.os_info == "Linux":
            try:
                kernel_version = subprocess.check_output(["uname", "-r"]).decode().strip()
                return f"Kernel Version: {kernel_version}"
            except:
                return "Kernel: Unable to determine version"

    @staticmethod
    def bytes_to_gb(bytes_value):
        return bytes_value / (1024 ** 3)

    def get_all_info(self):
        return {
            "OS Information": self.get_os_info(),
            "Machine Information": self.get_machine_info(),
            "Network Information": self.get_network_info(),
            "Memory Information": self.get_memory_info(),
            "Disk Information": self.get_disk_info(),
            "Current Shell": self.get_current_shell(),
            "Python Version": self.get_python_version(),
            "CPU Information": self.get_cpu_info(),
            "GPU Information": self.get_gpu_info(),
            "Specific OS Information": self.get_specific_os_info()
        }

if __name__ == "__main__":
    sys_info = SystemInfo()
    all_info = sys_info.get_all_info()
    
    for key, value in all_info.items():
        print(f"{key}:")
        print(f"  {value}")
        print()