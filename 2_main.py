import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

fn = "data_test.xlsx"
wb = load_workbook(fn)
ws = wb["Sheet"]

z = -1
count = [0, 10, 20, 30, 40, 50, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
urls = []
name = []
label = []
value = []
img = []
img_url = "http://ntt-energy.com.ua"

r = requests.get(f"http://ntt-energy.com.ua/ua/catalog/generatory/benzinoviy-generator/benzinovi-trifazni-380-220-v/")
soup = BeautifulSoup(r.content, "lxml")

img_red = soup.find_all("a", class_="highslide")
for l in range(11):
    img.append(img_url + img_red[l].get("href"))



data = soup.find_all("td", class_="itemProd")
label_pr = soup.find_all("td", class_="name_p")
value_pr = soup.find_all("td", class_="value_p")
print(data[0].find_next("a").text)

ws.append(["Модель", label_pr[0].text, label_pr[1].text, label_pr[2].text, label_pr[3].text, label_pr[4].text, label_pr[5].text, label_pr[6].text, label_pr[7].text, label_pr[8].text, label_pr[9].text, "img"])
wb.save(fn)
for i in count:
    z += 1
    try:
        #name.append(data[i].find_next("a").text)
        #label.append(label_pr[i].text)
        #value.append(value_pr[i].text)
        ws.append([data[z].find_next("a").text, value_pr[i].text, value_pr[i+1].text, value_pr[i+2].text, value_pr[i+3].text, value_pr[i+4].text, value_pr[i+5].text, value_pr[i+6].text, value_pr[i+7].text, value_pr[i+8].text, value_pr[i+9].text, img[z]])
        #ws.append([label_pr[i].text, value_pr[i].text])
        wb.save(fn)
    except:
        continue

wb.close()

print(value_pr)

