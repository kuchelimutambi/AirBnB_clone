#!/usr/bin/python3
""" a unique FileStorage instance for the application, ensuring that any previously stored instances are reloaded and available for use """
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
