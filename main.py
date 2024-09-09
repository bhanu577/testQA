import requests
import unittest
import json
from bs4 import BeautifulSoup
class TestFrontendBackendIntegration(unittest.TestCase):
    def test_backend_message(self):
        backend_url = "http://127.0.0.1:57375/greet"
        try:
            backend_response = requests.get(backend_url,timeout=5)
            self.assertEqual(backend_response.status_code, 200)
        except requests.exceptions.RequestException as e:
            self.fail(f"Backend request failed: {e}")

    
    def test_frontend_message(self):
        fronend_url = "http://127.0.0.1:57688"
        try:
            frontend_response = requests.get(fronend_url,timeout=5)
            self.assertEqual(frontend_response.status_code,200)
        except requests.exceptions.HTTPError as http_err:
            self.fail(f"HTTP error occurred while accessing frontend: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            self.fail(f"Connection error occurred while accessing frontend: {conn_err}")
        except Exception as err:
            self.fail(f"An unexpected error occurred while accessing frontend: {err}")

    
    def test_test_euqal(self):
        backend_url = "http://127.0.0.1:57375/greet"
        try:
            backend_response = requests.get(backend_url,timeout=5)
            self.assertEqual(backend_response.status_code, 200)
            result1=json.loads(backend_response.text)
        except requests.exceptions.HTTPError as http_err:
            self.fail(f"HTTP error occurred while accessing backend: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            self.fail(f"Connection error occurred while accessing backend: {conn_err}")
        except Exception as err:
            self.fail(f"An unexpected error occurred while accessing backend: {err}")

        try:
            fronend_url = "http://127.0.0.1:57688"
            frontend_response = requests.get(fronend_url,timeout=5)
            soup = BeautifulSoup(frontend_response.text, 'html.parser')
            result2 = soup.get_text().strip()
            print("---------------------------------")
            print("backend",result1["message"])
            print("fronend",result2)
            self.assertEqual(result1["message"],result2,"!!!!!Does Not match with the backend data!!!!!")   
        except requests.exceptions.HTTPError as http_err:
            self.fail(f"HTTP error occurred while accessing frontend: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            self.fail(f"Connection error occurred while accessing frontend: {conn_err}")
        except Exception as err:
            self.fail(f"An unexpected error occurred while accessing frontend: {err}")
        
if __name__ == "__main__":
    unittest.main()
