import requests
import getpass
import time

def main():
    print("welcome", getpass.getuser())
    nirurl = "http://10.0.0.25:5000/"
    michalurl = "http://10.0.0.27:5000/"
    chose = int(input("Nir(1) or Michal(2)?"))
    chose2 = int(input("are you happy? (1)yes (2)no"))
    while True:
        if chose == 1:
            url = nirurl
        else:
            url = michalurl
        if chose2 == 1:
            rr = requests.get(url=url)
        else:
            rr = requests.get(url=url+"user", params={"user": getpass.getuser()})
        print(rr.json())
        time.sleep(2)



if __name__ == '__main__':
    main()
