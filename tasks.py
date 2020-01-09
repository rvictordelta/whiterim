import time
from datetime import datetime
import schedule
import multiprocessing as mp
import csv

import populate


class Camper:
    def __init__(self, month, day, year, campsite, first_name, last_name,
                email_address, address1, address2, city, state, zip, phone):
        self.month = month
        self.day = day
        self.year = year
        self.campsite = campsite
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone


campers = []
with open('campers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, r in enumerate(reader):
        if i != 0:
            campers.append(Camper(r[0], r[1], r[2], int(r[3]), r[4], r[5],
                                  r[6], r[7], r[8], r[9], r[10], r[11], r[12]))


def populate_go():
    mp.freeze_support()
    pool = mp.Pool(processes=3)
    ret = pool.map(populate.populate_form, campers)


if __name__ == '__main__':
    schedule.every().day.at("16:20:30").do(populate_go)
    while True:
        schedule.run_pending()
        time.sleep(1)

