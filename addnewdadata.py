import requests
import json
import jsonpath

#
# url = "https://reqres.in/api/users"
# file = open("E:\\api_request\\new.json", "r")
# json_input = file.read()
# request_json = json.loads(json_input)
# print(request_json)
# response = requests.post(url, request_json)
# print(response.content)
# assert response.status_code == 201
# print(response.headers)
# print(response.headers.get('content-length'))
# response_json = json.loads(response.text)
# id = jsonpath.jsonpath(response_json, 'id')
# print(id[0])
# print(response_json)
# print(id[0])
# print(id[0])
# print(id[0])

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
response = requests.get(url)
print(response.content)
print(response.headers)
print(response.status_code)
result = response.json()
print(result)
list = result['list']
print(len(list))
temp_min = result['list'][0]['main']['temp_min']
print(temp_min)
for i in range(len(list)):
    x = (result['list'][i]['main']['temp'])
    y = (result['list'][i]['main']['temp_min'])
    z = (result['list'][i]['main']['temp_max'])
    a = result['list'][i]['weather'][0]['id']
    if y <= x <= z:
        if a == 500:
            print(result['list'][i])
            print('light rain')
            print(x)
        elif a == 800:
            print(result['list'][i])
            print(x)
            print('clear sky')
    elif x == y == z:
        if a == 500:
            print(result['list'][i])
            print('light rain')
            print(x)
        elif a == 800:
            print(result['list'][i])
            print(x)
            print('clear sky')
    else:
        print(result['list'][i])
        print(y)



#
#
#
#
#
#     else:
#         print(y)
# for i in range(len(list)):
#     a = result['list'][i]['weather'][0]['id']
#     if a == 500:
#
#         print('light rain')
#     elif a == 800:
#         print(result['list'][i])
#         print('clear sky')
#     else:
#         print(result['list'][i])
# a = result['list'][0]['weather'][0]['id']
# print(a)
# print(type(a))


# json_respnse = json.loads(response.text)
# print(json_respnse)
# temp_min= jsonpath.jsonpath(json_respnse,'list')
with open("C:/Users/Administrator/PycharmProjects/restapi/.pytest_cache/write.py", 'w') as f:
    f.write(str(result))
# # print(temp_min['main'].temp_min)
