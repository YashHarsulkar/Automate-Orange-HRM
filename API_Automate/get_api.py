import requests



header={
    'content-type':'application/json',
    'accept':'text/Plain'
}

url="https://fakerestapi.azurewebsites.net/api/v1/Activities/2"

response = requests.request("GET",url,headers=header)

print(response.json())

assert response.status_code==200

print ("pass")


