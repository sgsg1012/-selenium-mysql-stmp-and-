from selenium import webdriver
import re
import os
import time
from config import path, url, username, pwd
from test_mail import mail
from handleData import handle_data


def getData(page_data):
    list = []
    table = re.findall(r'<table.*?tabGrid.*?(<tbody.*?>.*?</tbody>).*</table>', page_data, re.S)[0]
    # print(table)
    # table=table[0]
    rows = re.findall('<tr.*?>(.*?)</tr>', table, re.S)[1:]
    if (rows[1] == ""):
        return list
    for i in rows:
        dic = {}
        # print(i)
        dic['id'] = re.findall('<td.*?tabGrid_kch.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['name'] = re.findall('<td.*?tabGrid_kcmc.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['year'] = re.findall('<td.*?tabGrid_xnmmc.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['sem'] = re.findall('<td.*?tabGrid_xqmmc.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['nature'] = re.findall('<td.*?tabGrid_kcxzmc.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['credit'] = re.findall('<td.*?tabGrid_xf\s*".*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['score'] = re.findall('<td.*?tabGrid_cj\s*".*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['gpa'] = re.findall('<td.*?tabGrid_jd.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['class'] = re.findall('<td.*?tabGrid_jxbmc.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['teacher'] = re.findall('<td.*?tabGrid_jsxm.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        dic['credit_gpa'] = re.findall('<td.*?tabGrid_xfjd.*?>\s*(.*?)\s*</td>', i, re.S)[0]
        # print(dic)
        list.append(dic)

    return list


def check(score, path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            num = fp.readline()[4]
            print(type(num))
            if (num != str(len(score))):
                return True
            else:
                return False
    else:
        return True


def computeGpu(score):
    totle = 0
    myTotle = 0
    for i in score:
        totle = totle + float(i['credit'])
        myTotle = myTotle + float(i['credit']) * float(i['gpa'])
    gpa = myTotle / totle
    return gpa


def write_in(score, path):
    gpa = computeGpu(score)
    with open(path, 'w', encoding='utf-8')as fp:
        fp.write('迄今出了')
        fp.write((str)(len(score)))
        fp.write('门成绩')
        fp.write('\n')
        for i in score:
            fp.write(i['subject'])
            fp.write(' ')
            fp.write(i['credit'])
            fp.write(' ')
            fp.write(i['score'])
            fp.write(' ')
            fp.write(i['gpa'])
            fp.write(' ')
            fp.write('\n')
        fp.write("本学期gpa: ")
        fp.write(str(gpa))
        fp.write('\n')


def handle(score, path):
    update = check(score, path)
    if update:
        print('更新')
        write_in(score, path)
        fp = open(path, 'r', encoding='utf-8')
        content = fp.read()
        content = '本学期有新成绩了\n' + content
        mail(content)


chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument(r'--user-data-dir=C:\Users\sgsg\AppData\Local\Google\Chrome\User Data') #设置成用户自己的数据目录
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
browser = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
browser.implicitly_wait(30)
browser.get(url=url)
# print(browser.page_source)
username = browser.find_element_by_xpath("//input[@id='yhm']").send_keys(username)
pwd = browser.find_element_by_xpath("//input[@id='mm']").send_keys(pwd)
enter = browser.find_element_by_xpath("//button[@id='dl']").click()
info = browser.find_element_by_xpath("//*[@id='cdNav']/ul/li[4]//a").click()
score_page = browser.find_element_by_xpath("//*[@id='cdNav']/ul/li[4]/ul/li[2]/a").click()
browser.switch_to.window(browser.window_handles[1])
score = []
for i in (5, 4, 3, 2):
    year_choose = browser.find_element_by_xpath("//*[@id='xnm_chosen']/a").click()
    year = browser.find_element_by_xpath(f"//*[@id='xnm_chosen']/div/ul/li[{i}]").click()
    for j in (2, 3, 4):
        term_choose = browser.find_element_by_xpath("//*[@id='xqm_chosen']/a").click()
        term = browser.find_element_by_xpath(f"//*[@id='xqm_chosen']/div/ul/li[{j}]").click()
        query = browser.find_element_by_xpath("//*[@id='search_go']").click()
        time.sleep(3)
        score += getData(browser.page_source)
print(score)
# handle(score, path)
handle_data(score)
browser.close()
# count = 1
# while (True):
#     print('---------------------------', count)
#     count = count + 1
#     time.sleep(60 * 60)
#     browser.refresh()
#     time.sleep(2)
#     year_choose = browser.find_element_by_xpath("//*[@id='xnm_chosen']/a").click()
#     year = browser.find_element_by_xpath("//*[@id='xnm_chosen']/div/ul/li[5]").click()
#     term_choose = browser.find_element_by_xpath("//*[@id='xqm_chosen']/a").click()
#     term = browser.find_element_by_xpath("//*[@id='xqm_chosen']/div/ul/li[4]").click()
#     query = browser.find_element_by_xpath("//*[@id='search_go']").click()
#     time.sleep(5)
#     score = getData(browser.page_source)
#     handle(score, path)
