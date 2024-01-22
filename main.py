import pathlib
import shutil
import time
from icecream import ic
from rich import print
from extensions import extensions_folders
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Source directory folder path goes here
desktop = pathlib.Path.home() / 'Desktop'
# Destination directory folder path
baseDestinationPath = 'C:/Users/Tarick Arnold'   

class WatchFolder:
    """Watch user's desktop folder and move appropriate location."""

# Initialize Watcher
    def __init__(self, desktop = desktop, handler = FileSystemEventHandler()):
        self.observer = Observer()
        self.desktop = desktop
        self.handler = handler   
        ic("Watcher initialized")    

# Run Watcher to observe directory on a schedule
    def run(self):
        self.observer.schedule(self.handler,self.desktop,recursive=True)
        self.observer.start()
        ic("Watcher Running in {}".format(self.desktop))
        try:
            while True:
                time.sleep(100)
        except: 
            self.observer.stop()
        self.observer.join()
        ic("\nWatcher Terminated\n")

class MyEventHandler(FileSystemEventHandler):
    """Perform moving of file if they have been modified from desktop to respective folder."""
    def on_modified(self, event):
       
        # Date and time
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        
        # Year check
        year_exists = False
        month_exists = False

        # Loop through files on desktop and extensions dict
        for files in desktop.glob('*'):
            for extensions in extensions_folders.keys():
                path = extensions_folders[extensions]
                if extensions == files.suffix:
                    destinationPath = baseDestinationPath + path
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

if __name__ == '__main__':
    Watchdog = WatchFolder()
    Watchdog.run()