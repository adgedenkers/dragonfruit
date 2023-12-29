# INSERT statements for 15 common cannabis strains
common_strains = [
    ("OG Kush", "Indica-dominant hybrid with a complex aroma profile and a unique terpene profile.", 19, 0.5, "Indica-dominant", "8-9 weeks", "Medium", "Pain, Stress, Insomnia", "Earthy, Pine, Woody", "North America"),
    ("Sour Diesel", "Sativa-dominant strain known for its fuel-like chemical aroma.", 22, 0.1, "Sativa-dominant", "10-11 weeks", "High", "Depression, Pain, Stress", "Diesel, Earthy, Pungent", "United States"),
    ("Blue Dream", "Sativa-dominant hybrid with a sweet berry aroma.", 18, 0.2, "Sativa-dominant", "9-10 weeks", "High", "Pain, Depression, Nausea", "Berry, Sweet, Herbal", "California, USA"),
    ("Granddaddy Purple", "Indica strain known for its grape and berry aroma.", 17, 0.1, "Indica", "8-11 weeks", "Medium", "Pain, Stress, Insomnia", "Berry, Grape, Sweet", "California, USA"),
    ("Afghan Kush", "Pure indica strain known for its heavy resin content.", 21, 0.6, "Indica", "7-8 weeks", "High", "Pain, Insomnia, Stress", "Earthy, Woody, Pungent", "Afghanistan"),
    ("Green Crack", "Sativa strain known for its energizing effects.", 16, 0.1, "Sativa", "7-9 weeks", "High", "Fatigue, Stress, Depression", "Citrus, Earthy, Sweet", "United States"),
    ("White Widow", "Balanced hybrid known for its white trichomes and potent effects.", 20, 0.2, "Hybrid", "8-9 weeks", "Medium", "Stress, Depression, Pain", "Earthy, Woody, Pungent", "Netherlands"),
    ("Girl Scout Cookies", "Hybrid strain with a sweet and earthy aroma.", 19, 0.2, "Hybrid", "9-10 weeks", "Medium", "Pain, Nausea, Appetite Loss", "Sweet, Earthy, Pungent", "California, USA"),
    ("Pineapple Express", "Sativa-dominant hybrid with a fruity, tropical aroma.", 17, 0.1, "Sativa-dominant", "7-8 weeks", "High", "Stress, Depression, Pain", "Tropical, Sweet, Pineapple", "Hawaii, USA"),
    ("Northern Lights", "Pure indica strain known for its resinous buds and fast flowering.", 18, 0.1, "Indica", "6-7 weeks", "Medium", "Stress, Pain, Insomnia", "Earthy, Pine, Sweet", "Afghanistan"),
    ("Amnesia Haze", "Sativa-dominant strain with a citrus and earthy aroma.", 20, 0.3, "Sativa-dominant", "10-11 weeks", "Medium", "Depression, Stress, Pain", "Citrus, Earthy, Lemon", "United States"),
    ("Trainwreck", "Sativa-dominant hybrid known for its strong effects.", 18, 0.2, "Sativa-dominant", "8-10 weeks", "High", "Pain, Stress, Anxiety", "Pine, Lemon, Earthy", "United States"),
    ("Bubba Kush", "Indica strain with a sweet and earthy aroma.", 17, 0.1, "Indica", "8-9 weeks", "Medium", "Stress, Insomnia, Pain", "Sweet, Earthy, Pungent", "California, USA"),
    ("AK-47", "Sativa-dominant hybrid known for its steady and long-lasting cerebral buzz.", 20, 0.1, "Sativa-dominant", "7-9 weeks", "High", "Depression, Pain, Stress", "Earthy, Pungent, Skunky", "Afghanistan"),
    ("Jack Herer", "Sativa-dominant strain known for its clear-headed and creative effects.", 18, 0.2, "Sativa-dominant", "8-10 weeks", "High", "Fatigue, Stress, Depression", "Earthy, Pine, Woody", "United States")
]

# Generating INSERT statements for strains
insert_statements_strains = [f"INSERT INTO strains (name, description, thc_content, cbd
