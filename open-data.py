# 網路連線示範
# import urllib.request as request
# src = "https://www.nkust.edu.tw"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")
# print(data)

# 串接，擷取公開資料
import urllib.request as request
import json
src = "	https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)
alist = data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in alist:
        file.write(company["公司名稱"]+"\n")

    