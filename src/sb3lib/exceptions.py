class WrongBlockType(Exception):
    def __init__(self, message=""):
        self.message = "The type of this block doent have this attribute. (If its a topBlock or not) \nIf you still want to do this set 'b3lib.config.throwFormatExceptions' to false."
        super().__init__(self.message)

class WrongSpriteType(Exception):
    def __init__(self, message=""):
        self.message = "This sprite type doesnt allow that. (If it is a stage or not) \nIf you still want to set this attribute set 'sb3lib.config.throwFormatExceptions' to false."
        super().__init__(self.message)