import unittest
from . import setup_db

class BaseTestCase(unittest.TestCase):
    def setUp(self, app):
        """
        Refresh database.

        :param app Flask app
        :param conn_string PostgreSQL connection string
        :param sql_file
        """
        self.app = app
        self.client = self.app.test_client

