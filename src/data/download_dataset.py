import joblib
import requests

def main():

    u = 'https://www.bantaykrimen.com/data.php?regionid='

    for i in range(1, 19):
        x = str(i)
        if len(x) < 2:
            x = '0' + x
        r = requests.get(u + str(x) + '0000000')
        joblib.dump(r.json(), str(x)+'bk_230319')

if __name__ == '__main__':
    main()
