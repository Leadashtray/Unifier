import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Unifier():
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.headers  = {"Accept": "application/json",
                   "Content-Type": "application/json"}

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_headers(self):
        return self.headers

    def make_request(self, endpoint):
        # Set credentials and URL for the API call

        host = self.get_host()
        port = self.get_port()
        url = f"https://{host}:{port}/api/login"
        user = self.get_user()
        password = self.get_password()
        headers = self.get_headers()

        # Set the headers and body for the call

        body = {
            'username': user,
            'password': password,
        }

        # Create a session object
        session = requests.Session()

        # User the session object to make the call to the API
        response = session.post(url, headers=headers,
                                data=json.dumps(body), verify=False, )

        # Open the Json object returned by the call
        response = response.json()

        # If you are logged in
        if response['meta']['rc'] == 'ok':
            endpoint = endpoint
            url = f"https://{host}:{port}/{endpoint}"
            response = session.get(url, headers=headers, verify=False,)
            response = response.json()
            response = response['data']
            return response

        else:
            print('Login failed, please check your credentials')


    def get_sites(self):
        # Make request for site information
        data = self.make_request('api/self/sites')
        # Print the results in a readable fashion
        for row in data:
            if row:
                for item in row:
                    print(item, ' : ', row[item])
            print('*'*100)