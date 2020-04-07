import requests
from bs4 import BeautifulSoup


def search(word):
    r = requests.get(f"https://dle.rae.es/?w={word.lower()}")
    cont = r.content

    soup = BeautifulSoup(cont, "html.parser")
    try:
        meaning = soup.find("p", {"class": "j"}).text

        if "1. " in meaning:
            meaning = meaning.replace("1. ", "")

            filters = ["f.", "adj.", "y ", "m.", "coloq.", "U. t. c. s.", "Anat.", "Zool."]
            for filter in filters:
                if filter in meaning:
                    meaning = meaning.replace(filter, "")

        print(f"{word.title()}:{meaning}")
    except:
        print(f"\"{word}\" está mal escrito o no existe.")


def main():
    print("Escribe las palabras correctamente, separadas por coma y espacio(persona, animal, fácil, ...)")
    inp = input()
    words = inp.split(", ")
    print("---")
    for i in words:
        search(i)
    print("---")


main()
