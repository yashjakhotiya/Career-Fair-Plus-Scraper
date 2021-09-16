import sys, time
from selenium import webdriver
from playsound import playsound

def main():
    url = sys.argv[1]
    browser = webdriver.Firefox()
    while(1):
        browser.get(url)
        time.sleep(7)
        res = browser.find_elements_by_xpath("//*[contains(text(), 'Ready to meet with a recruiter?')]")
        print(res)
        if len(res) != 0:
            while(1):
                playsound('alarm.wav')

if __name__ == "__main__":
    main()
