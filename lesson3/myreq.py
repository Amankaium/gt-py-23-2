import requests
from requests.models import Response


my_response = requests.get("https://pypi.org/alksdjflkasjdklfasd")
print(my_response.url)
# print(my_response.text)
print(my_response.status_code)
