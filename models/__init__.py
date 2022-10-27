#!/usr/bin/python3
"""creates a unique file storage instance for the application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
