import os
import pandas as pd
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def list_files_and_sort(path):
    files = []
    
    # Walk through directory and list all files
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_type = filename.split('.')[-1].upper() if '.' in filename else 'UNKNOWN'
            files.append((file_path, file_type))

    # Create a DataFrame for the files
    df_files = pd.DataFrame(files, columns=['File Name', 'File Type'])
    df_files.sort_values(by='File Type', inplace=True)
    
    # Write to Excel
    with pd.ExcelWriter(r'C:\\Users\\phani\\OneDrive\\Desktop\\all_files.xlsx', engine='openpyxl') as writer:
        df_files.to_excel(writer, sheet_name='Files', index=False, startrow=1)
        worksheet = writer.sheets['Files']
        worksheet.cell(row=1, column=1, value='All Files')

    # Sort files into directories based on file type
    for file_path, file_type in files:
        target_dir = os.path.join(path, file_type + 's')
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, os.path.basename(file_path))
        if not os.path.exists(target_path):
          shutil.move(file_path, target_path)
    
    # Generate report for sorted files
    sorted_files_report = []
    for root, dirs, filenames in os.walk(path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            for file_name in os.listdir(dir_path):
                sorted_files_report.append((dir_name, file_name))

    # Create a DataFrame for the sorted files report
    df_sorted_report = pd.DataFrame(sorted_files_report, columns=['Directory', 'File Name'])
    
    # Write to CSV
    df_sorted_report.to_csv(r'C:\\Users\\phani\\OneDrive\\Desktop\\sorted_files_report.csv', index=False)
    
    # Display DataFrames
    print("All Files DataFrame:")
    print(df_files)
    print("\nSorted Files Report DataFrame:")
    print(df_sorted_report)

# Create a FileSystemEventHandler subclass to handle file system events
class Watcher:
    DIRECTORY_TO_WATCH = r'C:\\Users\\phani\\Downloads'

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            list_files_and_sort(Watcher.DIRECTORY_TO_WATCH)

    def on_created(self, event):
        if not event.is_directory:
            list_files_and_sort(Watcher.DIRECTORY_TO_WATCH)

if __name__ == '__main__':
    w = Watcher()
    w.run()
