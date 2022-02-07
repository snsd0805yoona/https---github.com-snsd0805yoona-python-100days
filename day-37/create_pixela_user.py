import requests

pixela_endpoint = "https://pixe.la/v1/users"

create_user_params={
    "token": "snsd0805yoona",
    "username": "snsd0805yoona",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=create_user_params)

print(response)