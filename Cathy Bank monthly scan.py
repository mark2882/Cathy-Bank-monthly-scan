# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:43:55 2023

@author: CI-Mark.Huang
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from datetime import datetime
import requests
import os
import glob

from collections.abc import Iterable #这是不会报警告的用法
print(isinstance('abc', Iterable))



url="https://localhost:8834/#/"

options = Options()
options.add_argument('--disable-notifications')     #阻擋彈跳視窗
drivers_path=Service(r'/Users/test/Downloads/國泰弱掃自動化排程/chromedriver_mac64/chromedriver')
chrome = webdriver.Chrome(service=drivers_path, options=options)
#cfd79974c2742a1e16f46cea842a58480cb4f9cfe1290f90

chrome.get(url)
chrome.maximize_window()








PDF_list=['#templates > option:nth-child(6)','#templates > option:nth-child(2)','#templates > option:nth-child(4)']

#@duplicate_gen()
def gen_report(list2):
    for item in list2:
        #prjName = '國泰正式區'
        download_path = r'/Users/test/Downloads/'
        download_file = download_path + prjName + "*.pdf"
        old_file = glob.glob(download_file)
        print(old_file)
        for delete in old_file:
            os.remove(delete)

        #if not chrome.find_element(By.ID,'modal'):
        chrome.find_element(By.ID, 'generate-scan-report').click()

        time.sleep(2)
        option=chrome.find_element(By.CSS_SELECTOR, item)
        option.click()
        ele_text=option.text
        print(ele_text)

        # 下載    get_attribute('href')
        chrome.find_element(By.ID,'report-save').click()

        # 獲取當前日期, ele.text
        time22=datetime.now()
        today =time22.strftime("%Y-%m-%d")
        time.sleep(20)


        old_file = glob.glob(download_file)
        new_name = download_path+ele_text + "_" + today + ".pdf"
        print(new_name)

        # 設置下載檔名
        for old in old_file:
            if os.path.isfile(old):
                print('rename download file')
                os.rename(old, new_name)
    return


WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.ID,'details-button')),"找不到指定元素").click()  #等待5秒找到元素就執行
chrome.find_element(By.ID,'proceed-link').click()   #進入安全連線




#chrome.execute_script("window.localStorage.setItem('Nessus.token','374e426810740223efb86a7bfa3ea30289f9343422309789');")
#chrome.refresh()


#登入
WebDriverWait(chrome,60).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.nosession-content > form > div:nth-child(1) > input")),"找不到指定元素").clear  #清空帳號紀錄


chrome.find_element(By.CSS_SELECTOR,'div.form-group:nth-child(1)>input').send_keys("developer@cloud-interactive.com")
chrome.find_element(By.CSS_SELECTOR,'div.form-group:nth-child(2)>input').send_keys('Cloud@1234')
chrome.find_element(By.CSS_SELECTOR,'button[type=submit]').click()




WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr[data-id="11"]')),"找不到指定元素")
prjName=chrome.find_element(By.CSS_SELECTOR, 'td.scan-visible-name.pointer.mI.pr20').text       #修改複製瀏覽器的ＣＳＳ才找到
print(prjName)



#開始掃描
WebDriverWait(chrome,15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'i[data-id="11"]')),"找不到指定元素").click()

time.sleep(10)
WebDriverWait(chrome,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'tr[data-id="11"]')),"找不到指定元素").click()  #進入專案
WebDriverWait(chrome,2100).until(EC.presence_of_element_located((By.ID,'generate-scan-report')),"找不到指定元素")

#driver.execute_script('arguments[0].setAttribute("new_attribute", "new_value");', element) #取得屬性值, 前面為屬性，後面為內容




#產生報告    沒有寫出掃描錯誤例外
gen_report(PDF_list)




chrome.close()




