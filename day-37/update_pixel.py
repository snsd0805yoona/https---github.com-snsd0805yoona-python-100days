import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "snsd0805yoona"
TOKEN = "snsd0805yoona"
GRAPH_ID = "graph1"
DATE = datetime.date.today()


date_format = DATE.strftime("%Y%m%d")
# print(date_format)
add_pixel_params = {
    "quantity":"2",
}
headers={
    "X-USER-TOKEN":TOKEN
}
post_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_format}"

responses = requests.put(url=post_pixel_endpoint, json=add_pixel_params, headers=headers)

print(responses.text)
print(DATE)