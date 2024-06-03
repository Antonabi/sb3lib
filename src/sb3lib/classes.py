import json
import zipfile
from typing import Union

from . import exceptions
from .__init__ import raiseFormatException


class Meta: # the info about the project
    def __init__(self, metaJson) -> None:
        self.metaJson = metaJson
    
    @property
    def semver(self): # synching the semver with the json one
        return self.metaJson["semver"]

    @semver.setter # synching the semver with the json one
    def semver(self, value: str):
        self.metaJson["semver"] = value

    @property
    def vm(self): # doing the same as above
        return self.metaJson["vm"]

    @vm.setter
    def vm(self, value: str):
        self.metaJson["vm"] = value

    @property
    def agent(self):
        return self.metaJson["agent"]

    @agent.setter
    def agent(self, value: str):
        self.metaJson["agent"] = value

    def __repr__(self) -> str:
        return f"<sb3lib.Meta object with {self.metaJson}>"

class Comment: # the class for the programming blocks
    def __init__(self, commentId: str, commentJson: dict, spriteParent) -> None:
        self.commentJson = commentJson
        self.spriteParent = spriteParent
        self._id = commentId

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self.spriteParent.setComment(self.value, self.commentJson, oldCommentId=self._id)
        self._id = value

    @property
    def parentBlockItId(self): # the id of the block the comment is for
        return self.commentJson["blockId"]

    @parentBlockItId.setter
    def parentBlockId(self, value: str):
        self.commentJson["blockId"] = value
        self.spriteParent.setComment(self._id, self.commentJson)

    @property
    def text(self):
        return self.commentJson["text"]

    @text.setter
    def text(self, value: str):
        self.commentJson["text"] = value
        self.spriteParent.setComment(self._id, self.commentJson)

    @property
    def width(self): # the width of the comment
        return self.blockJson.get("x")

    @width.setter
    def width(self, value: int):
        self.commentJson["width"] = value
        self.spriteParent.setComment(self._id, self.commentJson)

    @property
    def height(self): # the width of the comment
        return self.blockJson.get("height")

    @height.setter
    def height(self, value: bool):
        self.commentJson["height"] = value
        self.spriteParent.setComment(self._id, self.commentJson)

    @property
    def minimized(self): # if the comment was minimized
        return self.blockJson["minimized"]

    @minimized.setter
    def minimized(self, value: bool):
        self.commentJson["minimized"] = value
        self.spriteParent.setComment(self._id, self.commentJson)
    
    @property
    def y(self): # the y position of the comment
        return self.commentJson.get("y")

    @y.setter
    def x(self, value: bool):
        self.commentJson["y"] = value
        self.spriteParent.setComment(self._id, self.commentJson)

    @property
    def x(self): # the x position of the comment
        return self.commentJson.get("x")

    @x.setter
    def x(self, value: float):
        self.commentJson["x"] = value
        self.spriteParent.setComment(self._id, self.commentJson)
    
    @property
    def y(self): # the y position of the comment
        return self.commentJson.get("y")

    @y.setter
    def x(self, value: float):
        self.commentJson["y"] = value
        self.spriteParent.setComment(self._id, self.commentJson)
        
    def __repr__(self) -> str:
        infoDict = {"id": self.id, "text": self.text}
        return f"<sb3lib.Comment object with {infoDict}>"

class Block: # the class for the programming blocks
    def __init__(self, blockId: str, blockJson: dict, spriteParent) -> None:
        self.blockJson = blockJson
        self.spriteParent = spriteParent
        self._id = blockId

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self.spriteParent.setBlock(self.value, self.blockJson, oldBlockId=self._id)
        self._id = value

    @property
    def opcode(self): # the block type in this format: 'category_blockname'
        return self.blockJson["opcode"]

    @opcode.setter
    def opcode(self, value: str):
        self.blockJson["opcode"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def nextId(self): # the id of the next block
        return self.blockJson["next"]

    @nextId.setter
    def nextId(self, value: str):
        self.blockJson["next"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def parentId(self): # the id of the block before
        return self.blockJson["parent"]

    @parentId.setter
    def parentId(self, value: str):
        self.blockJson["parent"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def inputs(self): # the inputs of the block
        return self.blockJson["inputs"]

    @inputs.setter
    def inputs(self, value: dict):
        self.blockJson["inputs"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def fields(self): # if an input has a variable I think
        return self.blockJson["fields"]

    @fields.setter
    def fields(self, value: dict):
        self.blockJson["fields"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def shadow(self): # idk I think if its invisisble
        return self.blockJson["shadow"]

    @shadow.setter
    def shadow(self, value: bool):
        self.blockJson["shadow"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def topLevel(self): # if its a top block (a block like 'if flag clicked')
        return self.blockJson["topLevel"]

    @topLevel.setter
    def topLevel(self, value: bool):
        self.blockJson["topLevel"] = value
        self.spriteParent.setBlock(self._id, self.blockJson)

    @property
    def x(self): # the x position of the block
        return self.blockJson.get("x")

    @x.setter
    def x(self, value: int):
        if self.blockJson.get("x") != None:
            self.blockJson["x"] = value
            self.spriteParent.setBlock(self._id, self.blockJson)
        else:
            raiseFormatException(exceptions.WrongBlockType)
    
    @property
    def y(self): # the x position of the block
        return self.blockJson.get("y")

    @y.setter
    def x(self, value: int):
        if self.blockJson.get("y") != None:
            self.blockJson["y"] = value
            self.spriteParent.setBlock(self._id, self.blockJson)
        else:
            raise raiseFormatException(exceptions.WrongBlockType)
        
    def __repr__(self) -> str:
        infoDict = {"id": self.id, "opcode": self.opcode}
        return f"<sb3lib.Block object with {infoDict}>"

class Broadcast:
    def __init__(self, broadcastId: str, broadcastName: str, spriteParent) -> None: # the broadcast class
        self._id = broadcastId
        self._name = broadcastName
        self.spriteParent = spriteParent
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self.spriteParent.setBroadcast(self._id, self._name, self._values, oldBroadcastId=self._id)
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.spriteParent.setBroadcast(self._id, self._name, self._values)

    
    def __repr__(self) -> str:
        infoDict = {"id": self.id, "name": self.name}
        return f"<sb3lib.Broadcast object with {infoDict}>"


class List:
    def __init__(self, listId: str, listName: str, listValues: list, spriteParent) -> None: # the list class
        self._id = listId
        self._name = listName
        self._values = listValues
        self.spriteParent = spriteParent
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self.spriteParent.setList(self._id, self._name, self._values, oldListId=self._id)
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.spriteParent.setList(self._id, self._name, self._values)

    @property
    def values(self):
        return self._value

    @values.setter
    def values(self, value: str):
        self._value = value
        self.spriteParent.setList(self._id, self._name, self._values)

    def __repr__(self) -> str:
        infoDict = {"id": self.id, "name": self.name, "valueCount": len(self.values)}
        return f"<sb3lib.List object with {infoDict}>"

class Variable:
    def __init__(self, varId: str, varName: str, varValue: Union[str, int, float], spriteParent) -> None: # the variable class
        self._id = varId
        self._name = varName
        self._value = varValue
        self.spriteParent = spriteParent
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self.spriteParent.setVariable(value, self._name, self._value, oldVarId=self._id)
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.spriteParent.setVariable(self._id, self._name, self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value
        self.spriteParent.setVariable(self._id, self._name, self._value)

    def __repr__(self) -> str:
        infoDict = {"id": self.id, "name": self.name, "value": self.value}
        return f"<sb3lib.Variable object with {infoDict}>"


class Sprite:
    def __init__(self, spriteJson: dict) -> None:
        self.spriteJson = spriteJson
        self.variables = self.getVariables()
        self.lists = self.getLists()
        self.broadcasts = self.getBroadcasts()
        self.blocks = self.getBlocks()

        pass
    
    #----------------------------------------------------
    # properties
    #----------------------------------------------------

    @property
    def name(self): # synching the name with the json one
        return self.spriteJson["name"]

    @name.setter # synching the name with the json one
    def name(self, value: str):
        self.spriteJson["name"] = value

    @property
    def isStage(self): # doing the same as above
        return self.spriteJson["isStage"]

    @isStage.setter
    def isStage(self, value: bool):
        self.spriteJson["isStage"] = value

    @property
    def volume(self): 
        return self.spriteJson["volume"]

    @volume.setter
    def volume(self, value: int): # from one to hundred
        self.spriteJson["volume"] = value

    @property
    def layerOrder(self):
        return self.spriteJson["layerOrder"]

    @layerOrder.setter
    def layerOrder(self, value: int):
        self.spriteJson["layerOrder"] = value
    
    @property
    def visible(self):
        return self.spriteJson["visible"]

    @visible.setter
    def visible(self, value: bool):
        self.spriteJson["visible"] = value

    @property
    def x(self):
        return self.spriteJson.get("x")

    @x.setter
    def x(self, value: int): # the x position of the sprite
        if self.spriteJson.get("x") != None:
            self.spriteJson["x"] = value
        else:
            raise raiseFormatException(exceptions.WrongSpriteType)

    @property
    def y(self):
        return self.spriteJson.get("y")

    @y.setter
    def y(self, value: int): # the y position of the sprite
        if self.spriteJson.get("y") != None:
            self.spriteJson["y"] = value
        else:
            raise raiseFormatException(exceptions.WrongSpriteType)
        
    @property
    def size(self):
        return self.spriteJson.get("size")

    @size.setter
    def size(self, value: int): # the size of the sprite
        if self.spriteJson.get("size") != None:
            self.spriteJson["size"] = value
        else:
            raise raiseFormatException(exceptions.WrongSpriteType)
        
    @property
    def direction(self):
        return self.spriteJson.get("direction")

    @direction.setter
    def direction(self, value: int): # the direction in wich the sprite is facing
        if self.spriteJson.get("direction") != None:
            self.spriteJson["direction"] = value
        else:
            raise raiseFormatException(exceptions.WrongSpriteType)
        
    @property
    def draggable(self):
        return self.spriteJson.get("draggable") # if the sprite is draggable

    @draggable.setter
    def draggable(self, value: bool): # 
        if self.spriteJson.get("draggable") != None:
            self.spriteJson["draggable"] = value
        else:
            raise raiseFormatException(exceptions.WrongSpriteType)
        
    @property
    def rotationStyle(self):
        return self.spriteJson.get("rotationStyle") # the rotation style of the sprite

    @rotationStyle.setter
    def rotationStyle(self, value: bool): # 
        if self.spriteJson.get("rotationStyle") != None:
            self.spriteJson["rotationStyle"] = value
        else:
            raise raiseFormatException(exceptions.WrongSpriteType)

    #----------------------------------------------------
    # functions
    #----------------------------------------------------

    def setVariable(self, varId, varName, varValue, oldVarId=None): # this code sets a variable in the sprite json. It only gets called by the variable class. (sorry for the wackyness of this code bruh)
        if oldVarId != None: # only sets the id, when a new one is provided (because vars work with ids)
            self.spriteJson["variables"][varId] = self.spriteJson["variables"].pop(oldVarId) # sets the varId in the json
        self.spriteJson["variables"][varId][0] = varName # sets the varName in the json
        self.spriteJson["variables"][varId][1] = varValue # sets the varValue in the json
    
    def setList(self, listId, listName, listValues, oldListId=None): # does the same as above but for lists
        if oldListId != None: # only sets the id, when a new one is provided (because lists work with ids)
            self.spriteJson["lists"][listId] = self.spriteJson["lists"].pop(oldListId) # sets the id in the json
        self.spriteJson["lists"][listId][0] = listName # sets the name in the json
        self.spriteJson["lists"][listId][1] = listValues # sets the values in the json

    def setBroadcast(self, broadcastId, broadcastName, oldBroadcastId=None): # does the same as above but for broadcasts (this only sets the name)
        if oldBroadcastId != None: # only sets the id, when a new one is provided (because broadcasts work with ids like lists and vars)
            self.spriteJson["broadcasts"][broadcastId] = self.spriteJson["broadcasts"].pop(oldBroadcastId) # sets the id in the json
        self.spriteJson["broadcasts"][broadcastId] = broadcastName # sets the name in the json

    def setBlock(self, blockId, blockJson, oldBlockId=None): # does the same as above but for blocks
        if oldBlockId != None: # only sets the id, when a new one is provided
            self.spriteJson["blocks"][blockId] = self.spriteJson["blocks"].pop(oldBlockId) # sets the id in the json
        self.spriteJson["blocks"][blockId] = blockJson # sets the complete data in the json

    def setComment(self, commentId, commentJson, oldCommentId=None): # does the same as above but for comments
        if oldCommentId != None: # only sets the id, when a new one is provided
            self.spriteJson["comments"][commentId] = self.spriteJson["comments"].pop(oldCommentId) # sets the id in the json
        self.spriteJson["comments"][commentId] = commentJson # sets the complete data in the json

    def getBroadcasts(self) -> list: # gets the broadcasts from the spriteJson as a list of broadcast objects
        broadcasts = []
        for broadcast in self.spriteJson["broadcasts"]:
            broadcastId = broadcast
            broadcastName = self.spriteJson["broadcasts"][broadcastId]

            broadcasts.append(Broadcast(broadcastId, broadcastName, self))
        return broadcasts

    def getVariables(self) -> list: # gets the variables from the spriteJson as a list of var objects
        variables = []
        for variable in self.spriteJson["variables"]:
            varId = variable
            varName = self.spriteJson["variables"][varId][0]
            varValue = self.spriteJson["variables"][varId][1]

            variables.append(Variable(varId, varName, varValue, self))
        return variables
    
    def getLists(self) -> list: # gets the lists from the spriteJson as a list of list objects
        lists = []
        for list in self.spriteJson["lists"]:
            listId = list
            listName = self.spriteJson["lists"][listId][0]
            listValue = self.spriteJson["lists"][listId][1]

            lists.append(List(listId, listName, listValue, self))
        return lists
    
    def getBlocks(self) -> list: # gets the blocks from the spriteJson as a list of block objects
        blocks = []
        for block in self.spriteJson["blocks"]:
            blockJson = self.spriteJson["blocks"][block]

            blocks.append(Block(block, blockJson, self))
        return blocks
    
    def getComments(self) -> list: # gets the comments from the spriteJson as a list of comment objects
        comments = []
        for comment in self.spriteJson["comments"]:
            commentJson = self.spriteJson["comments"][comment]

            comments.append(Comment(comment, commentJson, self))
        return comments
    
    def __repr__(self) -> str:
        infoDict = {"name": self.name, "isStage": self.isStage, "variableCount": len(self.variables), "broadcastCount": len(self.broadcasts), "listCount": len(self.lists)}
        return f"<sb3lib.Sprite object with {infoDict}>"

class ProjectJson:
    def __init__(self, projectJson: dict) -> None:
        self.projectJson = projectJson
        self.sprites = self.getSprites()
        self.meta = Meta(projectJson["meta"])

        pass

    def getSprites(self) -> list: # gets the sprites (targets) from the projectJson as a list
        sprites = []
        for sprite in self.projectJson["targets"]:
            sprites.append(Sprite(sprite))
        return sprites

    def __repr__(self) -> str:
        return json.dumps(self.projectJson)
    
    def __repr__(self) -> str:
        infoDict = {"spriteCount": len(self.sprites)}
        return f"<sb3lib.ProjectJson object with {infoDict}>"


class Project: # the project file
    def __init__(self, projectFile: zipfile.ZipFile) -> None:
        self.projectFile = projectFile
        self.json = ProjectJson(self.getJson())

        pass
    
    def getJson(self) -> ProjectJson: # will get and load the project.json
        with self.projectFile.open("project.json", "r") as projectJson:
            return json.loads(projectJson.read())
        
