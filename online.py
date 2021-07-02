from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import PIL
from selenium import webdriver
import time
import sys
import datetime
import os.path

website = sys.argv[1]
name = sys.argv[2]

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Ersel AKBAY\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

print ("\nBY ERSEL AKBAY\n")
print ("\nBaslaniyor")

browser = webdriver.Chrome()
browser.get(website)
time.sleep(10)   #you must read qr code in 10 second

user = browser.find_element_by_xpath("//span[@title='{}']".format(name))  
user.click()

counter=0
online_time=0 

if (not os.path.exists(name + "_history.txt")):
    f = open(name + "_History.txt", "x")
    f.close()
time.sleep(2) 
if (not os.path.exists(name + "_log.txt")):
    f = open(name + "_Log.txt", "x")
    f.close()
time.sleep(2) 


while True:
    browser.save_screenshot('download.png')

    img=Image.open("download.png")
    cropped_img=img.crop((530,35,750,65))  #left top right bottom
    cropped_img.save('newdownload.png') 
    time.sleep(5)

    first_text=pytesseract.image_to_string(Image.open('newdownload.png'),lang="tur")
    first_text=first_text.strip()


    if (first_text [ 0 : 3 ] == "çev" or first_text [ 0 : 3 ] == "yaz"):

        first_time = datetime.datetime.now()
        firsttime=str(first_time)
        
        f = open(name + "_log.txt","a")
        f.write(firsttime[ 0 : 19 ])
        f.write(" - ONLINE")
        f.write("\n\n")
        f.close()

        time.sleep(5)

        browser.save_screenshot('download.png')

        img=Image.open("download.png")
        cropped_img=img.crop((530,35,750,65))  #left top right bottom
        cropped_img.save('newdownload.png') 

        second_text=pytesseract.image_to_string(Image.open('newdownload.png'),lang="tur")
        second_text=second_text.strip()

        while (second_text [ 0 : 3 ] == "çev" or second_text [ 0 : 3 ] == "yaz"):

            browser.save_screenshot('download.png')
            img=Image.open("download.png")
            cropped_img=img.crop((530,35,750,65))  #left top right bottom
            cropped_img.save('newdownload.png') 
            second_text=pytesseract.image_to_string(Image.open('newdownload.png'),lang="tur")
            second_text=second_text.strip()
            time.sleep(5)

        later_time = datetime.datetime.now()
        latertime=str(later_time)

        f = open(name + "_log.txt","a")
        f.write(latertime[ 0 : 19 ])
        f.write(" - OFFLINE")
        f.write("\n\n")
        f.close()
      
        difference = later_time - first_time
        datetime.timedelta(0, 8, 562000)
        seconds_in_day = 24 * 60 * 60
        online_time = divmod(difference.days * seconds_in_day + difference.seconds, 60)

        
        f = open(name + "_history.txt", "a")
        f.write(name)
        f.write(" was online for duration ")
        f.write(str(online_time))
        f.write(" on date ")
        f.write(firsttime[ 0 : 19 ])
        f.write("\n\n")
        f.close()


        counter += 1
        if(counter >= 10):
            browser.get(website)
            time.sleep(5) 
            counter=0
            online_time=0
            user = browser.find_element_by_xpath("//span[@title='{}']".format(name))  
            user.click()
