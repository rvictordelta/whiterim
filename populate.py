from selenium import webdriver
import time


def populate_form(camper):
    """ takes in an instance of the camper class which contains the relevant
     information to register a camper for the trail """
    url = 'https://canypermits.nps.gov/index.cfm'
    driver = webdriver.Chrome()
    driver.get(url)

    # first page
    while driver.current_url == 'https://canypermits.nps.gov/index.cfm':
        driver.refresh()
        elem = driver.find_element_by_name("StartMonth")
        elem.send_keys(camper.month)

        elem = driver.find_element_by_name("StartDay")
        elem.send_keys(camper.day)

        elem = driver.find_element_by_name("StartYear")
        elem.send_keys(camper.year)

        submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
        submit_button.click()
        time.sleep(1)

    # second page
    elem = driver.find_element_by_name("DestinationID")
    elem.send_keys('Island in the Sky')

    submit_button = driver.find_elements_by_xpath("//input[@value='Next']")[0]
    submit_button.click()

    # third page
    table = driver.find_element_by_class_name("sitetable")
    rows = table.find_elements_by_tag_name("tr")
    r = camper.campsite
    while r < 23:
        try:
            cells = rows[r].find_elements_by_tag_name('td')
            try:
                radio_button = cells[2].find_element_by_tag_name('input')
                radio_button.click()
                break
            except:
                radio_button = cells[1].find_element_by_tag_name('input')
                radio_button.click()
                break
        except Exception as e:
            r += 1
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
    elem.send_keys(camper.first_name)
    elem = driver.find_element_by_name("LastName")
    elem.send_keys(camper.last_name)
    elem = driver.find_element_by_name("EmailAddress")
    elem.send_keys(camper.email_address)
    elem = driver.find_element_by_name("Address1")
    elem.send_keys(camper.address1)
    elem = driver.find_element_by_name("Address2")
    elem.send_keys(camper.address2)
    elem = driver.find_element_by_name("city")
    elem.send_keys(camper.city)
    elem = driver.find_element_by_name("state")
    elem.send_keys(camper.state)
    elem = driver.find_element_by_name("phone")
    elem.send_keys(camper.phone)
    elem = driver.find_element_by_name("zip")
    elem.send_keys(camper.zip)

    driver.find_element_by_class_name("button").click()

    # eighth page
    driver.find_elements_by_class_name("button")[1].click()

    # ninth page
    driver.find_element_by_class_name("button").click()

    time.sleep(100)

# tests
# class Camper:
#     def __init__(self, month, day, year, campsite, first_name, last_name,
#                 email_address, address1, address2, city, state, zip, phone):
#         self.month = month
#         self.day = day
#         self.year = year
#         self.campsite = campsite
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email_address = email_address
#         self.address1 = address1
#         self.address2 = address2
#         self.city = city
#         self.state = state
#         self.zip = zip
#         self.phone = phone
#
#
# import csv
# my_list = []
#
# with open('campers.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for i, r in enumerate(reader):
#         if i != 0:
#             my_list.append(Camper(r[0], r[1], r[2], int(r[3]), r[4], r[5], r[6],
#                                   r[7], r[8], r[9], r[10], r[11], r[12]))
#
# populate_form(my_list[0])
