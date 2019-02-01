from .basetest import BaseTestCase
from .setup_login import login

class AuthBaseTestCase(BaseTestCase):
    def setUp(self, app, settings):
        super(AuthBaseTestCase, self).setUp(app, settings['conn_string'], settings['sql_file'])
        self.headers = login(settings['login_username'], settings['login_password'])

