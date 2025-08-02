import requests as req

URL = "https://v2.jokeapi.dev/joke/Programming,Dark?type=single"
URL2 = "https://v2.jokeapi.dev/joke/Any?type=single"


def lessonSix():
    def projectLoadJoke():
        try:
            # Question 5:
            response = req.get(URL)
            response.raise_for_status()
            if response.status_code == 200:
                res_dic = response.json()
                # Question 6:
                print(res_dic['joke'])
            # Question 8:
            if res_dic['category'] == "Programming":
                print(res_dic['category'])
                print(res_dic['joke'])
        except req.exceptions.RequestExceptionk as e:
            print("Error in initializing joke: ", e)
        except ValueError:
            print("Response not Json")

    def exAPI1():
        # Question 1:
        try:
            flag = False
            while not flag:
                response = req.get(URL2)
                response.raise_for_status()
                if response.status_code == 200:
                    res_dic = response.json()
                print(res_dic['joke'].split())
                if 'banana' or 'Banana' in res_dic['joke'].split():
                    print("Found it!\nHere is a joke contains the word 'banana' or 'Banana':\n", res_dic['joke'])
                    flag = True
                    print(res_dic['joke'])
                    break
        except req.exceptions.RequestExceptionk as e:
            print("Error in initializing joke: ", e)

    def exAPI2():
        ratings = {}
        avg = []
        try:
            for i in range(10):
                response = req.get(URL)
                response.raise_for_status()
                if response.status_code == 200:
                    res_dic = response.json()
                    print("Hello please rate our joke,\nbetween 0 to 100")
                    print("Joke: ", res_dic['joke'])
                    temp = int(input("Enter your rating: "))
                    if temp < 0 or temp > 100:
                        print("Invalid input")
                        break
                    ratings[i] = temp
                    avg.append(temp)
            print("\n\n\n")
            print("Average rating for all jokes is: ", sum(avg) / 10)
        except req.exceptions.RequestExceptionk as e:
            print("Error in initializing joke: ", e)

    def exAPI3():
        jokes_dic = {}
        try:
            for i in range(10):
                response = req.get(URL)
                response.raise_for_status()
                if response.status_code == 200:
                    res_dic = response.json()
                    jokes_dic[i] = res_dic['joke']
        except req.exceptions.RequestException as e:
            print("Error in initializing joke: ", e)
        for i in range(10):
            if len(list(jokes_dic[i])) > 50:
                print("Joke: ", jokes_dic[i])

    # projectLoadJoke()
    # exAPI1()
    # exAPI2()
    exAPI3()
    # exAPI1()
