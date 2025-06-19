#!/usr/bin/env python3

import psutil
import time
import sys
import select

#adding colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET_COLOR = "\033[0m"

def monitor_cpu_usage():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent

        cpu_color = RED if cpu > 80 else GREEN
        mem_color = RED if mem > 80 else GREEN

        print(f"{cpu_color}CPU: {cpu}%{RESET_COLOR} | {mem_color}RAM: {mem}%{RESET_COLOR}")
        time.sleep(5)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            if sys.stdin.read(1) == 'q':
                print("\nExiting...")
                break


def disk_usage():
    disk = psutil.disk_usage('/').percent
    print(f'Disk usage: {disk}')


disk_usage()
monitor_cpu_usage()