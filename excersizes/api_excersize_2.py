import requests as req

URL = "https://dog.ceo/api/breeds/list/all"
URL2 = "https://dog.ceo/api/breeds/image/random/3"
URL3 = "https://jsonplaceholder.typicode.com/posts"
URL4 = "https://api.restful-api.dev/objects"
URL5 = "https://catfact.ninja/fact"


def q1():
    res_dic = {}
    try:
        response = req.get(URL)
        response.raise_for_status()
        res_dic = response.json()
    except req.exceptions.RequestException as e:
        print("Error: ", e)
        return
    for breed in res_dic['message']:
        print(breed)


def q2():
    res_dic = {}
    try:
        response = req.get(URL2)
        response.raise_for_status()
        res_dic = response.json()
    except req.exceptions.RequestException as e:
        print("Error: ", e)
        return
    for url in res_dic['message']:
        print(url)


def q3():
    res_dic = {}
    title = "My New Post"
    body = "This is the content of the new post"
    data = {"title": title, "body": body}
    try:
        response = req.post(URL3, data)
        response.raise_for_status()
        res_dic = response.json()
    except req.exceptions.RequestException as e:
        print("Error posting this data to the server\nThe error: ", e)
        return
    print("Created Post ID:", res_dic['id'])
    print("Title:", res_dic['title'])
    print("Body:", res_dic['body'])


def q4():
    res_dic = {}
    payload = {"name": "Apple iPhone 12 Pro Max", "data": {
        "capacity GB": 512,
        "color": "Cloudy White"
    }
               }
    try:
        response = req.post(URL4, json=payload)
        response.raise_for_status()
        res_dic = response.json()
        print(res_dic)
    except req.exceptions.RequestException as e:
        print("Error posting this data to the server\nError: ", e)
    print("Created Object ID: ", res_dic['id'])
    print("Name:", res_dic['name'])
    print("Data:", end=' ')
    print(res_dic['data'])


def q5():
    res_dic = {}
    try:
        response = req.get(URL5)
        response.raise_for_status()
        res_dic = response.json()
    except req.exceptions.RequestException as e:
        print("Error: ", e)
    print("Cat Fact: ", res_dic['fact'])


def runIt():
    print("Question 1:")
    q1()
    print("Question 2:")
    q2()
    print("Question 3:")
    q3()
    print("Question 4:")
    q4()
    print("Question 5:")
    q5()
