import pandas as pd
from datetime import date, timedelta

# Provided list of school days off
school_days_off_list = [
    (date(2023, 11, 10), "Veterans Day (Observed)", "Full Day"),
    (date(2023, 11, 22), "Thanksgiving Recess", "Full Day"),
    (date(2023, 11, 23), "Thanksgiving Day", "Full Day"),
    (date(2023, 11, 24), "Thanksgiving Recess", "Full Day"),
    (date(2023, 12,  1), "Parent/Teacher Conferences", "Half Day"),
    (date(2023, 12,  4), "Parent/Teacher Conferences", "Half Day"),
    (date(2023, 12, 25), "Christmas Day", "Full Day"),
    (date(2023, 12, 26), "Winter Recess", "Full Day"),
    (date(2023, 12, 27), "Winter Recess", "Full Day"),
    (date(2023, 12, 28), "Winter Recess", "Full Day"),
    (date(2023, 12, 29), "Winter Recess", "Full Day"),
    (date(2024,  1,  1), "New Year's Day", "Full Day"),
    (date(2024,  1, 15), "Martin Luther King, Jr. Day", "Full Day"),
    (date(2024,  2, 19), "February Break", "Full Day"),
    (date(2024,  2, 20), "February Break", "Full Day"),
    (date(2024,  2, 21), "February Break", "Full Day"),
    (date(2024,  2, 22), "February Break", "Full Day"),
    (date(2024,  2, 23), "February Break", "Full Day"),
    (date(2024,  3, 18), "Vacation Day", "Full Day"),
    (date(2024,  3, 22), "Parent/Teacher Conferences", "Half Day"),
    (date(2024,  3, 25), "Parent/Teacher Conferences", "Half Day"),
    (date(2024,  3, 29), "Good Friday", "Full Day"),
    (date(2024,  4,  1), "Spring Recess", "Full Day"),
    (date(2024,  4,  2), "Spring Recess", "Full Day"),
    (date(2024,  4,  3), "Spring Recess", "Full Day"),
    (date(2024,  4,  4), "Spring Recess", "Full Day"),
    (date(2024,  4,  5), "Spring Recess", "Full Day"),
    (date(2024,  5, 28), "Memorial Day", "Full Day"),
    (date(2024,  6, 19), "Juneteenth", "Full Day"),
]

# Convert list of tuples to a DataFrame for easier processing
school_days_off_df = pd.DataFrame(school_days_off_list, columns=['date', 'event', 'duration'])

# Define the date range
start_date = date(2023, 1, 1)
end_date = date(2070, 12, 31)

# Initialize the DataFrame
# (Same initialization as previously)

# ... (rest of the script remains unchanged)

# Adjust the school days logic
school_day_start = date(2023, 9, 7)
school_day_end = date(2024, 7, 1)
school_days_off = set(school_days_off_df['date'])  # Set for efficient membership testing

# ... (rest of the script remains unchanged)

# Iterate through the date range and populate the DataFrame
# (Same iteration as previously, but with the following adjustments)

    # School day attributes
    school_open = int(school_day_start <= current_date <= school_day_end and not weekend)
    if school_open:
        if current_date not in school_days_off:
            school_day = 1
            school_ab_day = ab_day_flag
            ab_day_flag = 'B' if ab_day_flag == 'A' else 'A'  # Alternate A/B days
        else:
            school_day = 0
            school_ab_day = None  # Adjust for no school days
    else:
        school_day = 0
        school_ab_day = None  # Adjust for no school days

# ... (rest of the script remains unchanged)

# Output the DataFrame
# (Same output as previously)
