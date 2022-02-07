import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "snsd0805yoona"
TOKEN = "snsd0805yoona"

create_graph_params={
    "id":"graph1",
    "name":"Leetcode_challenge",
    "unit":"commit",
    "type":"int",
    "color":"sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


response = requests.post(url=graph_endpoint, json=create_graph_params, headers=headers)

print(response.text)