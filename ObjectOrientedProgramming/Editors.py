
from abc import ABC,abstractmethod

class Editor:

    @abstractmethod
    def open(self):

        pass

    @abstractmethod
    def write(self):

        pass

    @abstractmethod
    def debug(self):

        pass

    @abstractmethod
    def execute(self):

        pass

class VSCode(Editor):

    def open(self):
        print("VScode open method")

    def write(self):
        print("vscode write method") 

    def debug(self):
        print("vscode debug method")

    def execute(self):
        print("vscode execute")           


vscode_instance=VSCode()

vscode_instance.write()


