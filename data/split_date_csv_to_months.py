import csv
import os
from datetime import datetime

def split_dates_into_months(input_file, output_folder):
    # Create the 'months' sub-folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    monthly_data = {}

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header

        for row in reader:
            # Parse the date assuming the format is 'MM/DD/YYYY'
            date = datetime.strptime(row[0], '%m/%d/%Y')
            year_month = date.strftime('%Y_%m')

            if year_month not in monthly_data:
                monthly_data[year_month] = [header]  # Add header to each new month file

            monthly_data[year_month].append(row)

    # Write each month's data to a separate file
    for year_month, data in monthly_data.items():
        month_file = os.path.join(output_folder, f'{year_month}.csv')
        with open(month_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    print("Splitting completed.")

# Usage
input_csv_file = 'dates.csv'  # Path to your 'dates.csv' file
output_directory = 'months'   # Sub-folder for monthly files
split_dates_into_months(input_csv_file, output_directory)
