import requests

res = requests.put("http://127.0.0.1:3000/api/courses/1", {"name": "Golang", "videos": 5})
# get - получение
# delete - удаление
# put - обновление
# post - добавление
print(res.json())
