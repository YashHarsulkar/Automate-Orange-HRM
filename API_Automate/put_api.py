import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

# Correct URL with specific ID
url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities/160'

put_payload = {
    "id": 160,
    "title": "Data updated successfully",
    "dueDate": "2025-07-01T09:03:09.413Z",
    "completed": True
}

response = requests.put(url, headers=headers, json=put_payload)

print("Status Code:", response.status_code)

# Only print JSON if response contains JSON content
try:
    print(response.json())
except Exception as e:
    print("No JSON response or parse error:", e)

print("pass")
