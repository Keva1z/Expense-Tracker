import unittest, os
from storage.engine import JSONDatabase, Expense

class TestStorage(unittest.TestCase):

    def test_sync(self):
        database = JSONDatabase('test_data.json')

        database._objects = [Expense(100, 'TEST')]
        objects_before = [object.to_dict() for object in database._objects]
        
        database.save()

        new_database = JSONDatabase('test_data.json')
        objects_new = [object.to_dict() for object in new_database._objects]
        
        os.remove('storage/test_data.json')

        self.assertListEqual(objects_before, objects_new)