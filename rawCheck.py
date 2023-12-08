#HB file creation script
import os
import time
from datetime import datetime

def create_log_file(path):
    # Using underscores instead of colons and spaces for compatibility with Windows file naming
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f"log_{current_time}.txt"
    with open(os.path.join(path, log_filename), 'w') as f:
        f.write(f'No new files added as of {current_time}')

def main():
    d_drive_path = "D:\\"
    log_path = "O:\\Public\\Proteomics-Core-Lab-Data\\ChromCheck\\log"
    check_interval = 30 * 60  # 30 minutes check interval
    last_check_time = time.time()
    files_already_seen = set(os.listdir(d_drive_path))

    while True:
        current_time = time.time()
        if current_time - last_check_time >= check_interval:
            current_files = set(os.listdir(d_drive_path))
            new_files = current_files - files_already_seen
            if not new_files:
                create_log_file(log_path)
            files_already_seen = current_files
            last_check_time = current_time
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
