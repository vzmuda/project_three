
# project_three
Třetí projekt pro Engeto Python Akademii - skript pro scrapování dat českých voleb z roku 2017.

Pro spuštění jsou nutné externí balíky,které lze nainstalovat příkazem : pip install -r requierements.txt

# Jak script pracuje:
Vyberte si volební obvod z této stránky (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) stisknutím "X"  a zkopírujte webovou adresu.
Skript pro potřebuje tyto dva argumenty:
  URL stránku
  Název výstupního .csv souboru (název musí být kompletní včetně koncovky.csv)

# Příklad spouštění scriptu:

python project03.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "prostejov.csv"
Výstupní soubor se uloží do stejné složky.

pozn. Je nutné,aby argumenty při spouštění byly uvedeny v uvozovkách
