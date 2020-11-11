import requests
from bs4 import BeautifulSoup


def search(word):
    r = requests.get("https://www.dictionary.com/browse/" + word.lower())
    cont = r.content

    soup = BeautifulSoup(cont, "html.parser")
    try:
        #meaning = soup.find("span", {"class": "one-click-content css-1p89gle e1q3nk1v4"}).text
        meaning = soup.find("span", {"class": "one-click-content css-1p89gle e1q3nk1v4"}).text
        #print(f"{word.title()}:{meaning}")
        print(word.title() + ":" + meaning)

    except:
        print(word + "doesn't exist.")

    except requests.exceptions.ConnectionError:
        print("No connection available.")

def main():
    print("Write the words correctly using coma and space(person, animal, crazy, ...)")
    inp = input()
    words = inp.split(", ")
    print("---")
    for i in words:
        search(i)
    print("---")


main()