# class Editor
# attributes=name,vendor
# display print=> name 



class Editor:

    name=str

    vendor=str

    def __init__(self,name,vendor):  #__init__ is a constructor

        self.name=name

        self.vendor=vendor

    def display(self):

        print(self.name,self.vendor)

    def __str__(self):

        return self.name

editor_instance1=Editor("pycharm","jebrains")

editor_instance2=Editor("vscode","microsoft")

print(editor_instance1)


        