class EmptyHashValueException(Exception):
    def __init__(self, message):
        self.message = "Hash value can not be empty it have to be a valid url"
        super().__init__(message)

class InvalidHashValueException(Exception):
    def __init__(self, message, type):
        self.message = f"Hash value can not be {type} it have to be a valid url"
        super().__init__(message)
