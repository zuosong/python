#import csv
#with open('E:\Private Doc\\files\\test.csv','rb') as csvfile:
#    reader = csv.reader(csvfile)
#    url_list = [row for row in reader]
#print url_list
#from selenium import webdriver
#import time
#chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
#def load_page_done(obj):
#    browser = obj
#    return browser.execute_script('''document.readyState == "complete" ''')

#browser = webdriver.Chrome(executable_path=chrome_path)
#browser.get("http://www.gongsibao.com")
#browser.maximize_window()
#time.sleep(5)
#print browser.execute_script(" return document.readyState ;")=="complete"
#System.out.println("readyState: "
#        + js.executeScript("return document.readyState").toString());
#def load_page_done(obj):
#    browser = obj
#    return browser.execute_script("return document.readyState;")=="complete"
def grade(score):
    if  90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def get_mode(num):
    if num % 100 == 0:
        if num % 400 == 0:
            return "It's a leap year!"
        else:
            return "It's not a leap year!"
    elif num % 4 == 0:
        return "It's a leap year!"
    else:
        return "It's not a leap year!"

def main():
    #score =int(raw_input("Please inpunt your score: "))
    #print grade(score)
    year = int (raw_input("Please inpunt your score: "))
    print get_mode(year)

if __name__=="__main__":
    main()
