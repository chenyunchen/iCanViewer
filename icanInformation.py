# encoding: utf-8


'''
UnicodeEncodeError
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
'''

import getpass
import mechanize
from bs4 import BeautifulSoup

url = "http://www.elearn.fju.edu.tw/login.aspx"
ican = "http://www.elearn.fju.edu.tw/Header.aspx"
icanurl = "http://www.elearn.fju.edu.tw/DashBoard.aspx"

print "\r"
user = raw_input("請輸入學號: ")
password = getpass.getpass()

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.open(url)
browser.select_form(name="form1")
browser["tbManNo"] = user
browser["tbPwd"] = password
browser.submit()

print "\r"
results = browser.open(ican)
soup = BeautifulSoup(results.read())
results =  soup.findAll("span", {"style": "font-weight:bold;"})[0].text.split(" ")
print "目前學年期: 102 學年第二學期"
print results[0]+" "+results[8]+" "+results[9],
print "- iCAN遠距教學平台"
print "\r"

results = browser.open(icanurl)
soup = BeautifulSoup(results.read())
course = soup.findAll("td", {"class": "detailtd"})
allcourse = (len(str(course).split('<td align="left" class="detailtd" width="15%">'))-1)/2

print "課程資訊"
print "===================================================================="
defaultname = "ctl00_ContentPlaceHolder1_gvCourseList_ctl"
coursenumber = 2
for number in range(0,allcourse):
    print soup.find(id=defaultname+str(coursenumber).zfill(2)+"_lblCourseApartment").text,
    print course[0+8*number].findAll(text=True)[2].strip().split(" ")[0].split("\r")[0],
    print soup.find(id=defaultname+str(coursenumber).zfill(2)+"_lbCourName1000").text,
    print soup.find(id=defaultname+str(coursenumber).zfill(2)+"_lblCourseNo").text,
    print course[2+8*number].text.strip()
    coursenumber = coursenumber + 1
print "===================================================================="
print "\r"
