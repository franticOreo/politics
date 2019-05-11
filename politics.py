from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": "C:/Users/admin/Documents/politics" ,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
  "plugins.always_open_pdf_externally": True,
  "plugins.always_open_xml_externally": False

})

browser = webdriver.Chrome('C:/Users/admin/Documents/politics/chromedriver.exe', chrome_options=options)
page = browser.get('https://www.aph.gov.au/Parliamentary_Business/Hansard')


for j in range(1):
    # loop over the amount of speeches on the page
    # for i in range(len(browser.find_elements_by_xpath('//*[@id="main_0_content_1_pnlResults"]/table/tbody/tr'))):
    for i in range(1):
        # loop through all PDF imgs to download
        print(browser.find_element_by_tag_name('html'))
        xpath = '//*[@id="main_0_content_1_lvHansard_hlXML_{}"]'.format(i)
        elem = browser.find_element_by_xpath(xpath)
        elem.click()


        # browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
        # text_with_xml = browser.find_element_by_class_name('pretty-print')
        # print(text_with_xml)
        print(browser.find_element_by_tag_name('html'))

    # click 'previous sitting week to go to previous date'
    previous_sit = browser.find_element_by_xpath('//*[@id="main_0_content_1_hlPrevSittingWeek"]')
    previous_sit.click()
