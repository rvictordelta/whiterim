import time
from datetime import datetime
import schedule
import scrape
import excel
import my_send_email
import csv


class Group:
    def __init__(self, name, id, pw, emails):
        self.name = name
        self.id = id
        self.pw = pw
        self.emails = emails


groups = []
with open("groups.csv") as csvfile:  # not tracked
    rows = csv.reader(csvfile)
    for row in rows:
        groups.append(Group(row[0], row[1], row[2], [x for x in row[3:]]))


def scrape_go():
    print(f"---beginning scrape at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for group in groups:
        scrape.scrape(group)
    print(f"---finished  scrape at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def excel_go():
    print(f"---beginning mkexcel at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for group in groups:
        excel.consolidate_data_excel(group)
    print(f"---finished  mkexcel at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def email_go():
    print(f"---beginning email at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for group in groups:
        my_send_email.my_send_email(group)
    print(f"---finished  email at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


schedule.every().hour.at(":31").do(scrape_go)
schedule.every().hour.at(":33").do(excel_go)
schedule.every().hour.at(":34").do(email_go)

while True:
    schedule.run_pending()
    time.sleep(1)
