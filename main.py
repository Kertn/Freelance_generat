import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

fn = "benz_1_2.xlsx"
wb = load_workbook(fn)
ws = wb["Sheet"]



urls = []
desk = []
desk_final = []
count = [0, 21,42,63,84,105,126,147,168,189,210,231,252,273,294,315,336,357,378,399,420,441,462,483,504,525,546,567,588,609,630,651,672,693,714,735,756,777,798,819,840,861,882,903,924]
label = []


r = requests.get(f"https://matari.ua/generatory/dizelni-generatori")
soup = BeautifulSoup(r.content, "lxml")
pred_urls_page = soup.find_all("div", class_="astra-shop-summary-wrap")
for i in range(41):
    try:
        urls.append(pred_urls_page[i].find_next("a").get("href"))
    except:
        continue


for i in urls:
    r_page = requests.get(i)
    print("1234")
    soup_page = BeautifulSoup(r_page.content, "lxml")
    label_all = soup_page.find_all("th", class_="attribute_name")
    desk_all = soup_page.find_all("td", class_="attribute_value")
    for v in range(70):
        try:
            desk_final.append(desk_all[v].find_next("p").text)
            label.append(label_all[v].text)
        except:
            continue

print(label[0])

ws.append([label[0],label[1],label[2],label[3],label[4],label[5],label[6],label[7],label[8],label[9],label[10],label[11],label[12],label[13],label[14],label[15],label[16],label[17],label[18],label[19],label[20], "img", "Описание"])
wb.save(fn)
for p in count:
    try:
        ws.append([desk_final[p], desk_final[p+1], desk_final[p+2], desk_final[p+3], desk_final[p+4], desk_final[p+5], desk_final[p+6], desk_final[p+7], desk_final[p+8], desk_final[p+9], desk_final[p+10], desk_final[p+11], desk_final[p+12], desk_final[p+13], desk_final[p+14], desk_final[p+15], desk_final[p+16], desk_final[p+17], desk_final[p+18], desk_final[p+19], desk_final[p+20]])
        wb.save(fn)
    except:
        continue
wb.close()