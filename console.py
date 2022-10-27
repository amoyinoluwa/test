#!/usr/bin/python3
from models.base_model import BaseModel
from inspect import isclass
import cmd, shlex, models

"""The HBNB command console"""

class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class is a limited-use command line interpreter for manipulating objects"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = BaseModel()
            print(arg.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if not args[0] in globals():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Extra command that exits the program"""
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
