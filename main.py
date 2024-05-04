import shutil
import time
from pathlib import Path
from extensions import extensions_folders
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def AddDatePath(Path):
    DatePath = Path / f'{datetime.today().year}' / f'{datetime.today().month:02d}'
    DatePath.mkdir(parents=True, exist_ok=True)
    return DatePath

def MakeUnique(Source: Path, DestinationPath: Path):
    if Path(DestinationPath / Source.name).exists():
        Counter = 0
        while True:
            Counter += 1
            NewName = DestinationPath / f'{Source.stem}_{Counter}{Source.suffix}'
            if not NewName.exists():
                return NewName
    else: 
        return DestinationPath / Source.name
    
class Handler(FileSystemEventHandler):

    def __init__(self, Directory: Path, destination_root: Path):
        self.Directory = Directory.resolve()
        self.destination_root = destination_root.resolve()

    def on_modified(self, event):
        for child in self.Directory.iterdir():
            # skips directories and non-specified extensions
            if child.is_file() and child.suffix.lower() in extensions_folders:
                DestinationPath = self.destination_root / extensions_folders[child.suffix.lower()]
                DestinationPath = AddDatePath(Path=DestinationPath)
                DestinationPath = MakeUnique(Source=child, DestinationPath=DestinationPath)
                shutil.move(src=child, dst=DestinationPath)
        
if __name__=="__main__":
    Directory = Path.home() / 'Desktop'
    destination_root = Path.home()
    EventHandler = Handler(Directory=Directory, destination_root=destination_root)

    observer = Observer()
    observer.schedule(EventHandler, f'{Directory}', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
        

