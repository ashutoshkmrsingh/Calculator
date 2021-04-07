class SingletonClassException(Exception):
    """Raised when Singleton class get instantiated more than once.

    Attributes:
        msg -- explanation of the error
    """

    def __init__(self, msg='cannot instantiate Singleton class more than once'):
        self.msg = msg
        super().__init__(self.msg)
