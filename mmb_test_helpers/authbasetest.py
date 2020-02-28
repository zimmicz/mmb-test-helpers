from .basetest import BaseTestCase
from .setup_login import login

class AuthBaseTestCase(BaseTestCase):
    def setUp(self, app, settings):
        super(AuthBaseTestCase, self).setUp(app)
        self.headers = login(settings['login_url'], settings['login_username'], settings['login_password'])

