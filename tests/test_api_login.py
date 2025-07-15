import allure
from api.login_api import LoginAPI

@allure.epic("API Tests")
@allure.feature("OrangeHRM API Login and Protected Pages")
class TestAPILogin:

    def setup_class(self):
        self.api = LoginAPI()
        self.username = "Admin"
        self.password = "admin123"

    def test_login_success(self):
        res = self.api.login(self.username, self.password)
        assert res.status_code == 200 #success

    def test_access_dashboard(self):
        self.api.login(self.username, self.password)
        res = self.api.get_dashboard()
        assert res.status_code == 200
        assert "<title>" in res.text.lower()

    def test_logout(self):
        self.api.login(self.username, self.password)
        res = self.api.logout()
        assert res.status_code == 200
