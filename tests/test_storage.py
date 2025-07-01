import unittest, os
from storage.engine import JSONDatabase, Expense

class TestStorage(unittest.TestCase):

    def test_sync(self):
        database = JSONDatabase('test_data.json')

        database._objects = [Expense(100, 'TEST')]
        objects_before = database._objects
        
        database.save()

        new_database = JSONDatabase('test_data.json')
        objects_new = new_database._objects
        
        os.remove('storage/test_data.json')
        self.assertAlmostEqual(objects_before, objects_new)