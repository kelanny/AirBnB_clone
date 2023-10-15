#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a command-line interpreter for managing objects in the HBNB project.

    Attributes:
    - prompt: The command prompt shown to the user.

    Public instance methods:
    - do_quit(self, arg): Command to exit the program.
    - do_EOF(self, arg): Command to exit the program.
    """

    prompt = " (hbnb) "

    def do_quit(self, arg):
        """Command to exit the program"""
        return (True)

    def do_EOF(self, arg):
        """Exit the program"""
        return (True)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
