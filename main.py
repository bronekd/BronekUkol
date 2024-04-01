#Úkol 1
#Máte dva textové soubory. Zjistěte, zda se jejich linie shodují. Pokud ne, vytiskněte neshodující se řádek z každého souboru.
with open('Task1_1.txt', 'r') as file1, open('Task1_2.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1) and i < len(lines2):
        if lines1[i] != lines2[i]: #Shoda stejných řádků
            print(f"Chyba na řádku {i+1}:\nSoubor 1: {lines1[i]}Soubor 2: {lines2[i]}")


#Úkol 2
#Máte textový soubor. Vytvořte nový soubor a zapište do něj následující statistiky založené na zdrojovém souboru:
#■ Počet znaků; ■ Počet řádků;
#■ Počet samohlásek;
#■ Počet souhlásek; ■ Počet číslic.


#Úkol 3
#Máte textový soubor. Odstraňte z něj poslední řádek. Výsledek zapište do jiného souboru.


#Úkol 4
#Máte textový soubor. Najděte délku nejdelší čáry.


#Úkol 5
#Máte textový soubor. Spočítejte, kolikrát se v něm vyskytuje slovo určené uživatelem.


#Úkol 6
#Máte textový soubor. Najděte a nahraďte zadané slovo. Uživatel určuje, co má hledat a čím má být nahrazeno.



