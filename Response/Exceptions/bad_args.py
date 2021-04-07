class BadArgumentExceptions(Exception):
    """Raised when unexpected argument encounters.

    Attributes:
        msg -- explanation of the error
    """

    def __init__(self, msg='Bad Arguments'):
        self.msg = msg
        super().__init__(self.msg)