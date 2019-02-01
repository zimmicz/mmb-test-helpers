import unittest
from . import setup_db

class BaseTestCase(unittest.TestCase):
    def setUp(self, app, conn_string, sql_file):
        """
        Refresh database.

        :param app Flask app
        :param conn_string PostgreSQL connection string
        :param sql_file
        """
        self.app = app
        self.client = self.app.test_client
        setup_db.run_file(conn_string, sql_file)

