date_times = [
    "2023-05-18 08:00:00-0400",
    "2023-05-18 09:30:00-0400",
    "2023-05-18 11:15:00-0400",
    "2023-05-18 13:45:00-0400",
    "2023-05-18 16:00:00-0400"
]

lines = [
    "pain-meds - oxycodone 15 mg",
    "bowel-movement - diarrhea",
    "morning-meds (see group)",
    "bowel-movement - diarrhea",
    "pain-meds - oxycodone 15 mg"
]

details = [
    "location:abdomen_lower-right-quadrant, level:6",
    "liquid",
    None,
    "diced",
    "location:abdomen_lower-right-quadrant, level:5"
]

combined_list = list(zip(date_times, lines, details))

for item in combined_list:
    print(item)
