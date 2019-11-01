import unittest
from csvReader.CsvReader import CsvReader, class_factory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Unit_Test_Addition.csv.csv')


'''
    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = class_factory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)
'''

if __name__ == '__main__':
    unittest.main()
