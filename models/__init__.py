#!/usr/bin/python3
"""creates a unique file storage instance for the application"""


from engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
