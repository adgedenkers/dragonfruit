import machine
import uos
from m5stack import lcd
import time

def read_csv(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        return data

def display_info(data):
    lcd.clear()
    for line in data:
        lcd.println(line)
        time.sleep(1)  # Adjust the delay as needed

# Example usage
current_month_file = '2023_01.csv'  # Adjust to the current month
date_data = read_csv(current_month_file)
display_info(date_data)
