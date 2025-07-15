import requests

class LoginAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://opensource-demo.orangehrmlive.com"

    def login(self, username, password):
        url = f"{self.base_url}/web/index.php/auth/validate"
        return self.session.post(url, data={"username": username, "password": password})

    def get_dashboard(self):
        url = f"{self.base_url}/web/index.php/dashboard/index"
        return self.session.get(url)

    def logout(self):
        url = f"{self.base_url}/web/index.php/auth/logout"
        return self.session.get(url)
