from selenium import webdriver
import xlsxwriter

workbook = xlsxwriter.Workbook('search_data.xlsx')
worksheet = workbook.add_worksheet()

def googleSearch(searchText):
    url = "https://www.google.com/search?q=" + searchText
    return url

driver = webdriver.Edge("drivers/msedgedriver.exe")

driver.get(googleSearch("Hello World"))

search_blocks = driver.find_elements_by_class_name("g")

row = 0
for search_block in search_blocks:
    try:
        ahref = search_block.find_element_by_tag_name("a")
        description = search_block.find_element_by_css_selector(".VwiC3b")
        worksheet.write(row, 0, ahref.get_attribute("href"))
        worksheet.write(row, 1, description.text)
        row+=1
    except:
        pass
workbook.close()
driver.close()

