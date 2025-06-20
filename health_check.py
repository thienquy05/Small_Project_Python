import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

print(f"Disk free: {shutil.disk_usage('/').free / shutil.disk_usage('/').total * 100:.2f}%")
print(f"CPU usage: {psutil.cpu_percent(1)}%")

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error")
else:
    print("Everything is Okay!")
