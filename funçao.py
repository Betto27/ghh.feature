from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://demo.automationtesting.in/Register.html"
driver.get(url)
sleep(3)

def nav_sobre():

    cadas = driver.find_element_by_css_selector("#submitbtn")
    cadas.click()

def combo2():

    combo_box = driver.find_element_by_css_selector("#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(4) > a")
    webdriver.ActionChains(driver).click_and_hold(combo_box).perform()
    sleep(3)

    combo_box_opcao2 = driver.find_element_by_css_selector("#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(4) > ul > li:nth-child(2) > a")
    combo_box_opcao2.click()
    sleep(3)

def combom1():

    combo_box = driver.find_element_by_css_selector(
        "#header > nav > div > div.navbar-collapse.collapse.navbar-right > ul > li:nth-child(4) > a")
    webdriver.ActionChains(driver).click_and_hold(combo_box).perform()
    sleep(3)

    combo_box_opcao1 = driver.find_element_by_xpath('//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[1]/a')
    combo_box_opcao1.click()
    sleep(3)

    fechar_anuncio = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/svg')
    fechar_anuncio.click()



nav_sobre()
#combo2()
combom1()