#!/usr/bin/python3
""" Airbnb Console """

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User

class BnBConsole(cmd.Cmd):
    """ Interactive point for the program """
    prompt = '(bnb)'
    classes = ['BaseModel', 'User']

    def do_quit(self, line):
        """ Exits the console """
        return True

    def do_EOF(self, line):
        """ Handles end-of-file (EOF) input """
        print()
        return True

    def do_create(self, line):
        """ Creates a new instance of a given class and prints the ID and saves to json """
        if not line:
            print('** class name missing **')
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = eval(f"{line}()")
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance """
        args = line.split()
        if not line:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            classname = args[0]
            objid = args[1]
            key = f"{classname}.{objid}"
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not line:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            classname = args[0] if args else None
            objid = args[1]
            instances = storage.all()
            key = f"{classname}.{objid}"
            if key not in instances:
                print('** No instance found **')
                return

            instance = instances[key]
            del instances[key]
            storage.save()

    def do_all(self, line):
        """ Prints the string representation of all instances """
        args = line.split()
        if args and args[0] not in self.classes:
            print('** class doesn\'t exist **')
        else:
            classname = args[0] if args else None
            instances = storage.all()
            result = []
            for key, value in instances.items():
                if classname is None or value.__class__.__name__ == classname:
                    result.append(str(value))
            print('\n'.join(result))

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        args = line.split()

        if not line:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            classname = args[0]
            objid = args[1]
            attr = args[2]
            value = args[3]

        cannot_update = ['id', 'created_at', 'updated_at']
        if attr in cannot_update:
                print('** attribute can\'t be updated **')
                return

        if value.startswith(("'", '"')) and value.endswith(("'", '"')):
            if value[0] != value[-1]:
                print("** A string argument must be between double quotes **")
                return
            value = value[1:-1]
        else:
            try:
                value = float(value) if '.' in value else int(value)
            except ValueError:
                print("** A string argument must be between double quotes **")
                return

        if attr.startswith(("'", '"')) and attr.endswith(("'", '"')):
            if attr[0] != attr[-1]:
                print("** A string argument must be between double quotes **")
                return
            attr = attr[1:-1]

        key = f"{classname}.{objid}"
        try:
            instance = storage.all()[key]
            instance.__dict__[attr] = value
            instance.save()
        except KeyError:
            print('** no instance found **')

if __name__ == '__main__':
    BnBConsole().cmdloop()
