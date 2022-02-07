import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "snsd0805yoona"
TOKEN = "snsd0805yoona"
GRAPH_ID = "graph1"
DATE = datetime.date.today()


date_format = DATE.strftime("%Y%m%d")

headers={
    "X-USER-TOKEN":TOKEN
}
post_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_format}"

responses = requests.delete(url=post_pixel_endpoint, headers=headers)

print(responses.text)