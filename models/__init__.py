#!/usr/bin/python3
""" __init__.py file for models directory """

module_name = "models.engine.file_storage"
FileStorage = __import__(module_name).FileStorage


storage = FileStorage()
storage.reload()
