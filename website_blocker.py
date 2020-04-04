import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
# host_path_win = r"C:\Windows\System32\drivers\etc"

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")
    else:
        print("Fun hours")
    time.sleep(5)
