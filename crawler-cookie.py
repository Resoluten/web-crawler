# 抓取PTT時事板的網頁原始碼(HTML)
import urllib.request as req
# 建立一個Request物件，附加Request Headers的資訊
def getData(url, QQQ):
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)
    # 解析原始碼，取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            # print(title.a.string)
            file.write(title.a.string + "\n")
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]
# 抓取一個頁面的標題
with open("data2.txt", "w", encoding="utf-8") as file:
    pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"
    count = 0
    while count<2:
        pageurl = "https://www.ptt.cc" + getData(pageurl,file)
        count+=1
