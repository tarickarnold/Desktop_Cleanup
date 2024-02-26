import shutil
import time
import pathlib
from icecream import ic
from rich import print
from extensions import extensions_folders
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def MakeUnique(DestinationPath, Name):
    Counter = 0
    while True:
        Counter += 1
        Path = DestinationPath / Name.format(Counter)
        if not Path.exists():
            return Path
    
def MoveFile(DestinationPath, Entry, Name):
    if pathlib.Path.exists(f"{DestinationPath}/{Name}"):
        UniqueName = MakeUnique(DestinationPath, Name)
        OldName = pathlib.Path.joinpath(DestinationPath, Name)
        NewName = pathlib.Path.joinpath(DestinationPath, UniqueName)
        pathlib.Path.rename(OldName,NewName)
    shutil.move(Entry,DestinationPath)

class Watcher:

    def __init__(self, Directory, Handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = Handler
        self.directory = Directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")

class MyHandler(FileSystemEventHandler):

    def on_modified(self, DestinationPath, BaseDestinationPath, event):
        for Name in Directory.interdir():
            if Name.is_file() and Name.suffix.lower() in extensions_folders:
                DestinationPath = MakeUnique(DestinationPath, Name)
                MoveFile(DestinationPath, Name)
        
if __name__=="__main__":
    Directory = pathlib.Path.home() / 'Desktop'
    BaseDestinationPath = str(pathlib.Path.home())
    DestinationPath = BaseDestinationPath / f'{datetime.today().year}' / f'{datetime.today().month:02d}'
    w = Watcher(Directory, MyHandler())
    w.run()        




        
        
        
        
        
        
        
#Date and time
#         now = datetime.now()
#         year = now.strftime("%Y")
#         month = now.strftime("%m")
        
#         # Year check
#         year_exists = False
#         month_exists = False

#         # Loop through files on desktop and extensions dict
#         for files in desktop.glob('*'):
#             for extensions in extensions_folders.keys():
#                 path = extensions_folders[extensions]
#                 if extensions == files.suffix:
#                     destinationPath = baseDestinationPath + path
#                     yearPath = destinationPath + '/' + year
#                     monthPath = yearPath + '/' + month
#                     if pathlib.Path(yearPath).exists():
#                         year_exists = True
#                     else: pathlib.Path(yearPath).mkdir(parents=True, exist_ok=False)
#                     if pathlib.Path(monthPath).exists():
#                         month_exists = True
#                     else: pathlib.Path(monthPath).mkdir(parents=True, exist_ok=False)
#                     shutil.move(files, monthPath)
#                     ic("Files were moved successfully!")

# if __name__=="__main__":
    # w = Watcher(Directory, MyHandler())
    # w.run()


