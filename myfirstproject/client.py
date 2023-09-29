import requests
import getpass


def main():
    print(getpass.getuser())
    nirurl = "http://10.0.0.25:5000/"
    michalurl = "http://10.0.0.27:5000/"
    rr = requests.get(url=michalurl)
    print(rr.json())


if __name__ == '__main__':
    main()
