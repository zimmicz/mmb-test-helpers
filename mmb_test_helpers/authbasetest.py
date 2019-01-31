from .basetest import BaseTestCase
from .setup_login import login

class AuthBaseTestCase(BaseTestCase):
    def setUp(self, app, login_username, login_password, conn_string, sql_file):
        super(AuthBaseTestCase, self).setUp(app, conn_string, sql_file)
        self.headers = login(login_username, login_password)

