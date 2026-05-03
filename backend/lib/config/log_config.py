# pyright: reportUntypedBaseClass=false, reportUnknownMemberType=false

#   Importing Third-party Libraries
from std_log import Log # type: ignore (Library 'std_log' lacks type stubs)


class AppWatcher(Log):

    def __init__(self):
        super().__init__(name=f"{self.__class__.__name__}")
        

class UtilityWatcher(Log):

    def __init__(self):
        super().__init__(name=f"{self.__class__.__name__}")

class MethodWatcher(Log):

    def __init__(self):
        super().__init__(name=f"{self.__class__.__name__}")

        
        
