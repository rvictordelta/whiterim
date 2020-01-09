from selenium import webdriver
import time

def populate_form(month, day, year, campsite_row_num):
    url = 'https://canypermits.nps.gov/index.cfm'
    driver = webdriver.Chrome()
    driver.get(url)


    # first page
    elem = driver.find_element_by_name("StartMonth")
    elem.send_keys(month)

    elem = driver.find_element_by_name("StartDay")
    elem.send_keys(day)

    elem = driver.find_element_by_name("StartYear")
    elem.send_keys(year)

    submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
    submit_button.click()

    # second page
    elem = driver.find_element_by_name("DestinationID")
    elem.send_keys('Island in the Sky')

    submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
    submit_button.click()

    # third page
    table = driver.find_element_by_class_name("sitetable")
    rows = table.find_elements_by_tag_name("tr")

    cells = rows[campsite_row_num].find_elements_by_tag_name('td')
    radio_button = cells[1].find_element_by_tag_name('input')
    radio_button.click()
    submit_button = driver.find_elements_by_xpath(
        "//input[@value='Add Selected Sites']")[0]
    submit_button.click()

    # fourth page
    elem = driver.find_element_by_name("GroupCapacity_1")
    elem.send_keys(15)
    elem = driver.find_element_by_name("GroupCapacity_2")
    elem.send_keys(3)
    submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
    submit_button.click()

    # fifth page
    driver.find_element_by_class_name("button").click()

    # sixth page
    checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
    for box in checkboxes:
        box.click()

    elem = driver.find_element_by_name("Value_3")
    elem.send_keys("Gooseberry Hiking Trail")

    elem = driver.find_element_by_name("Value_4")
    elem.send_keys("Gooseberry Hiking Trail")

    driver.find_element_by_class_name("button").click()

    # seventh page
    elem = driver.find_element_by_name("FirstName")
    elem.send_keys("Robert")
    elem = driver.find_element_by_name("LastName")
    elem.send_keys("VanDusen")
    elem = driver.find_element_by_name("EmailAddress")
    elem.send_keys("rvd.work@gmail.com")
    elem = driver.find_element_by_name("Address1")
    elem.send_keys("151 N Michigan Ave")
    elem = driver.find_element_by_name("Address2")
    elem.send_keys("Apt 3209")
    elem = driver.find_element_by_name("city")
    elem.send_keys("Chicago")
    elem = driver.find_element_by_name("state")
    elem.send_keys("Illinois")
    elem = driver.find_element_by_name("phone")
    elem.send_keys("303-859-9961")
    elem = driver.find_element_by_name("zip")
    elem.send_keys(60601)

    driver.find_element_by_class_name("button").click()

    # eighth page
    driver.find_elements_by_class_name("button")[1].click()

    # ninth page
    driver.find_element_by_class_name("button").click()


    time.sleep(10)




# tests
populate_form('May', 9, 2020, 6)
