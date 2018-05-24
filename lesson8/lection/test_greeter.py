import unittest
from lesson8.lection.greeter import Greeter
from unittest.mock import patch
from datetime import datetime


class GreeterTestCase(unittest.TestCase):
    def test_greet(self):
        gr = Greeter()
        self.assertEqual(gr.greet('Ivan'), 'Hello Ivan')

    def test_greet_2(self):
        gr = Greeter()
        self.assertEqual(gr.greet(' Ivan '), 'Hello Ivan')

    def test_greet_3(self):
        gr = Greeter()
        self.assertEqual(gr.greet('ivan'), 'Hello Ivan')

    @patch('lesson8.lection.greeter.datetime')
    def test_greet_4(self, mock_datetime):
        gr = Greeter()
        mock_datetime.now.return_value = datetime(2018, 5, 23, 7, 00)
        self.assertEqual(gr.greet('ivan'), 'Good morning Ivan')

    @patch('lesson8.lection.greeter.datetime')
    def test_greet_5(self, mock_datetime):
        gr = Greeter()
        mock_datetime.now.return_value = datetime(2018, 5, 23, 19, 00)
        self.assertEqual(gr.greet('ivan'), 'Good evening Ivan')

    @patch('lesson8.lection.greeter.datetime')
    def test_greet_6(self, mock_datetime):
        gr = Greeter()
        mock_datetime.now.return_value = datetime(2018, 5, 23, 23, 00)
        self.assertEqual(gr.greet('ivan'), 'Good night Ivan')

    @patch('lesson8.lection.greeter.logging')
    def test_greet_7(self, mock_logging):
        gr = Greeter()
        gr.greet('ivan')
        self.assertTrue(mock_logging.info.called)
