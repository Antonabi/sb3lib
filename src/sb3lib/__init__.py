from typing import IO, Union
import zipfile

from . import classes


class Config: # config class
    throwFormatExceptions = True # if project format exceptions are thrown, like setting the position on a stage. If you still want to do just set it to false.

config = Config() # the config instance so you can change it



def loadProject(projectFile: Union[str, IO[bytes]]) -> classes.Project:
    with zipfile.ZipFile(projectFile) as zipRef:
        return classes.Project(zipRef)
    

def raiseFormatException(exception):
    if config.throwFormatExceptions:
        raise exception