#!/usr/bin/python3
"""Unitestets file for the file_storage implementatin
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

class TestFileStorage_instantiation(unittest.TestCase):
    """Test mainly focused on the instansiation of class"""

    def test_FileStorage_standard_instantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instnatiation_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_Privacy_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_provacy_obj_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
