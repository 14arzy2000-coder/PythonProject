import os
import sys
import platform
import datetime

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]

now = datetime.datetime.now()
date_time = sys.stdout("%Y-%m-%d %H:%M:%S")
print(f"{os_name} \n"
      f"{os_version} \n"
      f"{now.year} \n"
      f"{now.day} \n"
      f"{now.month} \n"
      f"{now.hour} \n")

a = os.