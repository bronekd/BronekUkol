#Úkol 1
#Máte dva textové soubory. Zjistěte, zda se jejich linie shodují. Pokud ne, vytiskněte neshodující se řádek z každého souboru.
"""
with open('Task1_1.txt', 'r') as file1, open('Task1_2.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1) and i < len(lines2):
        if lines1[i] != lines2[i]: #Shoda stejných řádků
            print(f"Chyba na řádku {i+1}:\nSoubor 1: {lines1[i]} Soubor 2: {lines2[i]}")
    #Ošetření více řídků v souboru
    elif i < len(lines1):
        print(f"Chyba na řádku {i + 1}:\nSoubor 1: {lines1[i]} Soubor 2: Chybí řádek")
    elif i < len(lines2):
        print(f"Chyba na řádku {i + 1}:\nSoubor 1: Chybí řádek Soubor 2: {lines2[i]}")
"""
#Úkol 2
#Máte textový soubor. Vytvořte nový soubor a zapište do něj následující statistiky založené na zdrojovém souboru:
#■ Počet znaků;
# ■ Počet řádků;
#■ Počet samohlásek;
#■ Počet souhlásek;
# ■ Počet číslic.
"""
pocet_znaku = pocet_radku = pocet_samohlasek = pocet_souhlasek = pocet_cislic = 0
samohlasky = "aeiouyáéěíóúůýAEIOUYÁÉĚÍÓÚŮÝ"
souhlasky = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

#Čtení
with open('Task2_source.txt', 'r') as soubor:
    for radek in soubor:
        pocet_radku += 1
        pocet_znaku += len(radek)
        for znak in radek:
            if znak.lower() in samohlasky:
                pocet_samohlasek += 1
            elif znak.lower() in souhlasky:
                pocet_souhlasek += 1
            elif znak.isdigit():
                pocet_cislic += 1


#Zápis
with open('Task2_statistic.txt', 'w') as vystup:
    vystup.write(f"Počet znaků: {pocet_znaku}\n")
    vystup.write(f"Počet řádků: {pocet_radku}\n")
    vystup.write(f"Počet samohlásek: {pocet_samohlasek}\n")
    vystup.write(f"Počet souhlásek: {pocet_souhlasek}\n")
    vystup.write(f"Počet číslic: {pocet_cislic}\n")

print(f"Počet znaků: {pocet_znaku}\n")
print(f"Počet řádků: {pocet_radku}\n")
print(f"Počet samohlásek: {pocet_samohlasek}\n")
print(f"Počet souhlásek: {pocet_souhlasek}\n")
print(f"Počet číslic: {pocet_cislic}\n")

"""

#Úkol 3
#Máte textový soubor. Odstraňte z něj poslední řádek. Výsledek zapište do jiného souboru.
"""
#Otevření souboru
with open("Task3.txt", "r") as source_file:
    lines = source_file.readlines()

# odebrání posledního řádku
lines.pop()

#zápis
with open("Task3_output.txt", "w") as target_file:
    for line in lines:
        target_file.write(line)
        print(f"Zapíši: {line}")
"""


#Úkol 4
#Máte textový soubor. Najděte délku nejdelší čáry.
"""
max_lenght = 0
cislo_nejdelsiho_radku = 0
aktualni_cislo_radku = 0

with open("Task4.txt", "r") as file:
    for line in file:
        aktualni_cislo_radku += 1 # zvýšíme číslo řádku
        lenght_line = len(line.rstrip("\n")) # Odebrání nového řádku z délky v případě potřeby

        if lenght_line > max_lenght:
            max_lenght = lenght_line
            cislo_nejdelsiho_radku = aktualni_cislo_radku

print(f"Délka nejdelšího řádku: {max_lenght}")
print(f"Číslo řádku s nejdelším textem: {cislo_nejdelsiho_radku}")

"""


#Úkol 5
#Máte textový soubor. Spočítejte, kolikrát se v něm vyskytuje slovo určené uživatelem.
"""
#hledané slovo
hledane_slovo = input("Zadej slovo pro vyhledání:  ").strip()   #Zadejte ahoj

#Proměná pro výpočet vyskytů
pocet_slov = 0

with open("Task5.txt", "r") as file:
    for line in file:
        #rozdeleni slov
        slova = line.strip().split()
        #počítání výskytů
        for slovo in slova:
            if slovo.lower() == hledane_slovo.lower():
                pocet_slov += 1

print(f"Slovo {hledane_slovo} se v souboru vyskytuje {pocet_slov}.")

"""

#Úkol 6
#Máte textový soubor. Najděte a nahraďte zadané slovo. Uživatel určuje, co má hledat a čím má být nahrazeno.

hledane_slovo = input("Zadej hledané slovo (ahoj): ").strip()
nahradni_slovo = input("Zadej slovo pro nahrazeni (Dobrý den): ").strip()

with open("Task6.txt", "r") as file:
    obsah = file.read()

#nahrazeni
upraveny_obsah = obsah.replace(hledane_slovo, nahradni_slovo)

#zápis upraveného obsahu
with open("Task6_output.txt", "w") as file2:
    file2.write(upraveny_obsah)

print(f"Slovo {hledane_slovo} bylo nahrazeno slovem {nahradni_slovo} v souboru.")
