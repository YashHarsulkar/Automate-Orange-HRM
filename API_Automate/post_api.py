import requests

header = {
     'accept': 'text/plain',
     'Content-Type': 'application/json'
 }


request_payload = {
    "id": 160,
     "title": "string",
   "dueDate": "2025-07-01T09:03:09.413Z",
     "completed": True
 }


response = requests.post(
     "https://fakerestapi.azurewebsites.net/api/v1/Activities",
    headers=header,
   json=request_payload)

print("Status Code:", response.status_code)
print("Response Body:", response.text)









