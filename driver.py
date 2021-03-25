from selenium import webdriver

def GetDriver():

    driver = webdriver.Chrome(r'C:\Users\Santiago\Desktop\SeleniumSaleor\chromedriver\chromedriver.exe')
    driver.get("https://campusvirtual.univalle.edu.co/moodle/")
    return driver
