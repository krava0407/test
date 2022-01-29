import re
import time
from selenium.webdriver.common.by import By
from driver import Driver
import pandas as pd



class Constructor:

    driver = Driver.get_instance()

    def open_page(self):
        self.driver.get('https://itdashboard.gov/')
        time.sleep(3)

    def click_dive(self):
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-default btn-lg-2x trend_sans_oneregular']").click()
        time.sleep(3)

    def print_list(self):
        agency = self.driver.find_element(By.XPATH, "//div[@id='agency-tiles-widget']").text
        agency = agency.replace('view', '').replace('Total', '').replace('FY2021', '').replace('Spending', '').replace(':', '')
        agency = agency.replace('   ', '').replace('  ', '')
        new_agency = list(re.split('\n', agency))      #str to list
        agency_list = [x for x in new_agency if x]     #del elements = ''
        df = pd.DataFrame(agency_list)
        df.to_excel('agency.xlsx', sheet_name='agency')
        time.sleep(3)

    def click_agency(self):
        self.driver.find_element(By.XPATH, "(//a[@class='btn btn-default btn-sm'][normalize-space()='view'])[25]").click()
        time.sleep(3)

    def show_all(self):
        self.driver.find_element(By.XPATH, "//select[@name='investments-table-object_length']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//body/main[@id='main-content']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/label[1]/select[1]/option[4]").click()
        time.sleep(5)

    def print_individ_invest(self):
        data_invest = self.driver.find_element(By.XPATH, "//div[@id='investments-table-object_wrapper']").text
        data_invest = list(re.split('\n', data_invest))

        read_data_agency = pd.read_excel('agency.xlsx', engine='openpyxl')
        ind_inv = pd.DataFrame(data_invest)

        data_sheets = {'Agency_2': read_data_agency, 'individ_investment': ind_inv}
        writer = pd.ExcelWriter('agency.xlsx', engine='xlsxwriter')

        for sheet_name in data_sheets.keys():
            data_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
        writer.save()
        time.sleep(1)

    def click_uii_0004(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'422-000000004')]").click()
        time.sleep(10)

    def click_download(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Download Business Case PDF')]").click()
        time.sleep(10)

    def back(self):
        self.driver.back()
        time.sleep(10)

    def click_uii_1327(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'422-000001327')]").click()
        time.sleep(5)

    def click_uii_1328(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'422-000001328')]").click()
        time.sleep(5)

#this str need del after test git















    def quit(self):
        self.driver.quit()

