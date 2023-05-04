import requests


headers = {
    'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMTkyNDI4LCJpYXQiOjE2ODMxOTIwNDMsImp0aSI6ImZjMTRmY2Y2ODQxODQ1YzU5YzRkZDZiNTlhYzM2Mjk2IiwidXNlcl9pZCI6M30.zpyo47XsKN2qufpl898KGSCbxebzAAOHyMaqTBx4cSg'
}
response = requests.get('http://127.0.0.1:8000/api/v1/restaurants/', headers=headers)
print(response)