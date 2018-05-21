# coding=gbk
import requests
import bs4
import re
import time
from selenium import webdriver

urlList = []
compList = []
filter = ["关于浙江省固体废物利用处...", "2018年4月浙江省地表...", "2018年4月浙江省饮用...", "关于浙江省固体废物利用处...", "2018年4月浙江省环境...",
          "关于浙江省固体废物利用处...", "2018年4月浙江省饮用...",
          "2018年4月浙江省地表...", "关于拟对前列腺素系列、S...", "关于拟对前列腺素系列、S..."]
baseUrl = "http://www.zjepb.gov.cn"
if __name__ == '__main__':
    browser = webdriver.Chrome("E:\chromedriver.exe")
    pattern = '<a.*?href="(.+)".*?>(.*?)</a>'

    browser.get("http://www.zjepb.gov.cn/col/col1201374/index.html")
    soup = bs4.BeautifulSoup(browser.page_source, "html.parser")
    x = soup.findAll("a", {'style': 'font-size:12px;line-height:24px;margin-left:5px;'})
    for a in x:
        if a.string in filter:
            continue
        compList.append(a.string)
        urlList.append(a['href'])

    for j in range(0, 93):
        browser.find_element_by_xpath("//*[contains(@class, 'default_pgBtn default_pgNext')]").click()
        time.sleep(2)
        soup = bs4.BeautifulSoup(browser.page_source, "html.parser")
        x = soup.findAll("a", {'style': 'font-size:12px;line-height:24px;margin-left:5px;'})
        for a in x:
            if a.string in filter:
                continue
            compList.append(a.string)
            urlList.append(a['href'])
    browser.close()

    file = open('comp.txt', 'w', encoding="utf8")
    for comp in compList:
        file.write(comp + "\n")
    file.close()

    file = open('url.txt', 'w', encoding="utf8")
    for url in urlList:
        file.write(url + "\n")
    file.close()
    for i in range(0, compList.__len__()):
        response = requests.get(baseUrl + urlList[i])
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        tmpResult = soup.findAll("p")
        content = ""
        for tmp in tmpResult:
            content += str(tmp)

        out = re.sub('<.*?>', '', content)

        tmpResult = soup.findAll("a")
        docName = ""
        docLink = ""
        for tmp in tmpResult:
            if str(tmp.string).__contains__(".doc"):
                docName = tmp.string
                docLink = baseUrl + tmp['href']
                break

        saveFile = open("E:/shadowsocks/" + str(i) + compList[i] + '.txt', 'w', encoding="utf8")
        saveFile.write(out + "\n" + docName + "\n" + docLink)
        saveFile.close()
