import pathlib
import shutil
import time
from icecream import ic
from rich import print
from extensions import extensions_folders
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#
# Source directory folder path goes here
desktop = pathlib.Path.home() / 'Desktop'
# Destination directory folder path
baseDestinationPath = 'C:/Users/Tarick Arnold'   

class Watcher:
    """Watch user's desktop folder and move appropriate location."""

# Initialize Watcher
    def Watcher(self):
        def __init__(self, source_dir, destination_dir):
        super().__init__()
        self.source_dir = Path(source_dir)
        self.destination_dir = Path(destination_dir)
    
    def run(source_dir, destination_dir):
        event_handler = FileHandler(source_dir, destination_dir)
        observer = Observer()
        observer.schedule(event_handler, path=source_dir, recursive=False)
        observer.start()     
        ic("Watcher Running in {}".format(self.desktop))
        try:
            while True:
                time.sleep(100)
        except: 
            self.observer.stop()
        self.observer.join()
        ic("\nWatcher Terminated\n")

class Handler(FileSystemEventHandler):
    """Perform moving of file if they have been modified from desktop to respective folder."""
        def on_modified(self, event):
            if event.is_directory:
                return
            file_path = Path(event.src_path)
            file_name = file_path.name
            destination_path = self.destination_dir / file_name
            try:
                 for files in source_dir.glob('*'):
                    for extensions in extensions_folders.keys():
                        path = extensions_folders[extensions]
                        if extensions == files.suffix:
                            destinationPath = destination_dir + path
                            yearPath = destinationPath + '/' + year
                            monthPath = yearPath + '/' + month
                            if pathlib.Path(yearPath).exists():
                                year_exists = True
                            else: pathlib.Path(yearPath).mkdir(parents=True, exist_ok=False)
                            if pathlib.Path(monthPath).exists():
                                month_exists = True
                            else: pathlib.Path(monthPath).mkdir(parents=True, exist_ok=False)
                            shutil.move(files, monthPath)
                            ic("Files were moved successfully!")
                print(f"Moved '{file_name}' to '{self.destination_dir}'")
            except Exception as e:
                print(f"Error moving '{file_name}': {e}")
           

if __name__ == "__main__":
    source_dir = pathlib.Path.home() / 'Desktop'  # Path to desktop
    destination_dir = pathlib.Path(monthPath)  # Destination directory
    run(source_dir, destination_dir)
