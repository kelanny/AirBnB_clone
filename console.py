#!/usr/bin/python3
"""
This module provides a command-line interface
Used for interacting with the HBNB project.
Users can execute various commands to manage objects within the project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a command-line interpreter
    Used for managing objects in the HBNB project.

    Attributes:
    - prompt: The command prompt shown to the user.

    Public instance methods:
    - do_quit(self, arg): Command to exit the program.
    - do_EOF(self, arg): Command to exit the program.
    """

    prompt = " (hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Command to exit the program"""
        return (True)

    def do_EOF(self, arg):
        """Exit the program"""
        return (True)

    def do_create(self, arg):
        """It creates a new class instance.
        Usage: create <class>
        """
        
        arg = arg.split()
        print(arg)
        if not arg:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:            
            new_instance = eval(arg[0]())
            new_instance.save()
            print(new_instance.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
