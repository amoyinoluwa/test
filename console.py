#!/usr/bin/python3
import cmd

"""The HBNB command console"""

class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class is a limited-use command line interpreter for manipulating objects"""
    prompt = '(hbnb) '

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
