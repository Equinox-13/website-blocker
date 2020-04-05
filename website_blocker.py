import time
from datetime import datetime as dt

# hosts file location for linux
hosts_path_linux = "/etc/hosts"

# hosts file location for testing
hosts_temp = "hosts"

# hosts file location for windows
# host_path_win = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

# website hosts to be blocked
website_list = ["www.facebook.com","www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hours")
        with open(hosts_path_linux, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+"\n")

    else:
        print("fun hours.")
        with open(hosts_path_linux,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
