import requests
import getpass

def main():
    URL_michal = "http://10.0.0.27:5000/"
    URL_nir = "http://10.0.0.25:5000/"
    URL = URL_michal #URL_nir

    r = requests.get(url=URL+"user", params={"user": getpass.getuser()})  # , params = PARAMS)

    # r = requests.get(url=URL + "/worker", params={"user": "ozery", "x": {"q": 1}}).json()
    print(r.json())
if __name__ == '__main__':
    main()