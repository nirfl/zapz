import requests
import getpass


def main():
    print("welcome", getpass.getuser())
    nirurl = "http://10.0.0.25:5000/"
    michalurl = "http://10.0.0.27:5000/"
    chose = int(input("Nir(1) or Michal(2)?"))
    if chose == 1:
        rr = requests.get(url=nirurl)
        print(rr.json())
    elif chose == 2:
        rr = requests.get(url=michalurl)
        print(rr.json())



if __name__ == '__main__':
    main()
