from Response.Exceptions import singleton_error
import time


class Interaction:
    """Return responses to Text
    """
    __instance = None

    def __init__(self):
        if Interaction.__instance != None:
            raise singleton_error.SingletonClassException()
        else:
            Interaction.__instance = self

    @staticmethod
    def get_instance():
        """return instance of Interaction
        """
        if Interaction.__instance == None:
            Interaction()
        return Interaction.__instance

    def forbidden(self):
        return '''Sorry! I am not able to understand you, Please say it again'''

    def whatsup(self):
        return "I'm Fine! What about you"

    def name(self):
        return "I'm Corlex Cool"

    def do(self):
        return 'I do many interesting stuff, more formerly calculation'

    def feel(self):
        return "I'm felling happy"

    def how(self):
        return "I'm Fine"

    def amazing(self):
        return 'Yeah !!!'

    def oops(self):
        return 'Sorry !!!'

    def created(self):
        self.name()
        return "And I'm created by Ashutosh"

    def age(self):
        return "I'm in my development stage"

    def date_time(self):
        return time.asctime(time.localtime())

    def greet(self):
        return 'Hii! I am a Calculator. How can I help you?'
