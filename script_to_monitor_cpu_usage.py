#!/usr/bin/env python3

import psutil
import time

def monitor_cpu_usage():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        print(f"CPU: {cpu}% | RAM: {mem}%")
        time.sleep(5)

monitor_cpu_usage()