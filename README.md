
# project_three
Třetí projekt pro Engeto Python Akademii - skript pro scrapování dat českých voleb z roku 2017
Pro spuštění jsou nutné externí balíky,které lze nainstalovat příkazem : pip install -r requirements.txt

# Jak script pracuje:
Vyberte si volební obvod z této stránky (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) stisknutím "X"  a zkopirujte webovou adresi.
Skript potřebuje dva argumenty:
  URL stránku
  Název výstupního .csv souboru (název musí být kompletní včetně koncovky.csv)

# Příklad spouštění scriptu:

python3 project03.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" "beroun.csv"
Výstupní soubor se uloží do stejné složky.

pozn. Je nutné,aby argumenty při spouštění byly uvedeny v uvozovkách
