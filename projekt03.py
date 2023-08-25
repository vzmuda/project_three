"""
project_2.py: druhý projekt do Engeto Online Python Akademie

author: Václav Zmuda
email: vaclav.zmuda@gmail.com
discord: vaclav5301
"""


import csv
import requests
from bs4 import BeautifulSoup
import sys
from tqdm import tqdm
import time

def zkontroluj_argumenty(argv):
    print(argv)
    if len(argv) != 3:
        print(f"Špatně zadaný počet argumentů,požadovaný počet 2,zadáno {(len(argv) - 1)}")
        quit()
    elif "https://volby.cz/pls/ps2017nss/" not in argv[1]:
        print("Špatně zadaná adresa pro stáhnutí dat")
        quit()
    elif not argv[2].endswith(".csv"):
        print("Špatně zadaný název výstupního souboru")
        quit()
    
def main(url, soubor):

    try:
        print(f"Probíhá zpracování dat")
    except AttributeError:
        print("Nastala neočekávaná chyba")
        quit()
    
    soup = zpracovat_url(url)
    make_csv(soup, soubor, url)
    print(f"Soubor uložen jako: '{soubor}'")

def make_csv(soup, soubor, url):
    tabulka = soup.find_all('tr')

    with open(soubor, "w", encoding='utf-8', newline="") as f:
        thewriter = csv.writer(f)
        zahlavi = header(url)
        thewriter.writerow(zahlavi)
        pocitadlo_obci = 0

        progress_bar = tqdm(total=(len(tabulka)), desc="Progress", dynamic_ncols=True)

        for i in tabulka:
            try:
                progress_bar.update(1)
                pomocna = i.find('td', class_='cislo')
                cislo = pomocna.find('a').string
                url_obce = pomocna.find('a', href=True)
                data_url_obce = "https://volby.cz/pls/ps2017nss/"+url_obce['href']
                obec = i.find('td', class_='overflow_name').string
                soup_2 = zpracovat_url(data_url_obce)
                tds_1 = soup_2.find_all('td', class_='cislo')
                volici = tds_1[3].string
                vydane_obalky = tds_1[4].string
                platne_hlasy = tds_1[7].string
                data = [cislo, obec, volici, vydane_obalky, platne_hlasy]
                table_2 = soup_2.find_all('table', class_='table')
                tds_2 = table_2[1].find_all('td', attrs={'class': ['cislo'], 'headers': ['t1sa2 t1sb3']})
                for td in tds_2:
                    hlasy = td.string
                    data.append(hlasy)
                tds_3 = table_2[2].find_all('td', attrs={'class': ['cislo'], 'headers': ['t2sa2 t2sb3']})
                for td in tds_3:
                    hlasy = td.string
                    data.append(hlasy)
                thewriter.writerow(data)
                pocitadlo_obci += 1
                
            except AttributeError:
                continue
    progress_bar.close()
    print(f"Zpracováno {pocitadlo_obci} obcí")
                

def header(url):
    soup = zpracovat_url(url)
    try:
        obec = soup.find('td', attrs= {'class': 'cislo', 'headers': 't1sa1 t1sb1'}).a
        url_obce = "https://volby.cz/pls/ps2017nss/"+obec['href']
        soup_2 = zpracovat_url(url_obce)
        strany = soup_2.find_all('tr')
        zahlavi = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
    except AttributeError:
        print("Nastala chyba při stahování nebo řazení dat,zkontrolujte správnost adresy pro stažení. Ukončuji program.")
        quit()
    
    for i in strany:
        try:
            strana = i.find('td', class_='overflow_name').string
            zahlavi.append(strana)
        except AttributeError:
            continue
    return list(zahlavi)

def zpracovat_url(url):
    odpoved = requests.get(url)
    return BeautifulSoup(odpoved.text, "html.parser")

if __name__ == "__main__":
#    zkontroluj_argumenty(sys.argv)
    main(sys.argv[1], sys.argv[2])
