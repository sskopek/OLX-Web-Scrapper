import requests
import re
from bs4 import BeautifulSoup

url='https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/gdansk/'

polaczenie = requests.get(url)

if polaczenie:
    print('Połączono z serwerem')
else:
    print('Brak połączenia z serwerem')

soup = BeautifulSoup(polaczenie.content, 'html.parser')

lista_cen=soup.find_all('p', class_='price')
pattern = '<p class="price">\n<strong>(.*?) zł</strong>\n</p>'

lista_po_edycji=[]

for element in lista_cen:
    element_string = str(element)
    substring = re.search(pattern, element_string).group(1)
    substring_bez_spacji = int(substring.replace(" ", ""))
    lista_po_edycji.append(substring_bez_spacji)

liczba_mieszkan = len(lista_po_edycji)
suma_cen_mieszkan = sum(lista_po_edycji)
print('Liczba mieszkań na stronie to ' + str(liczba_mieszkan))
print('Suma cen mieszkań na stronie to ' + str(suma_cen_mieszkan))
print('Średnia cena mieszkania to ' + str(suma_cen_mieszkan/liczba_mieszkan))

f=open('f1.txt','w')
for elementy in lista_po_edycji:
    f.write(str(elementy)+"\n")
f.close()

