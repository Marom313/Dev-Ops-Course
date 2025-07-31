import requests as req

URL = "https://v2.jokeapi.dev/joke/Programming,Dark?type=single"


def lessonSix():
    def _loadJoke():
        try:
            response = req.get(URL)
            response.raise_for_status()
            print(response)

        except req.exceptions.RequestExceptionk as e:
            print("Error in initializing joke: ", e)

    _loadJoke()
