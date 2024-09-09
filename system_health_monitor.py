import psutil
import logging
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
LOG_FILE = "system_health.log"  

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert = f"High CPU usage detected: {cpu_usage}%"
        print(alert)
        logging.warning(alert)

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert = f"High memory usage detected: {memory_usage}%"
        print(alert)
        logging.warning(alert)

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        alert = f"High disk usage detected: {disk_usage}%"
        print(alert)
        logging.warning(alert)

def check_running_processes():
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])
    for proc in processes:
        try:
            cpu_usage = proc.info['cpu_percent']
            if cpu_usage is not None and cpu_usage > CPU_THRESHOLD:
                alert = f"High CPU usage by process {proc.info['name']} (PID: {proc.info['pid']}): {cpu_usage}%"
                print(alert)
                logging.warning(alert)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


check_cpu_usage()
check_memory_usage()
check_disk_usage()
check_running_processes()
