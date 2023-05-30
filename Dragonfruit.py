import datetime
from datetime import date, time, datetime, timedelta
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = "Dragonfruit",
    page_icon = "🐉",
)

def main():
    st.write(f"# Dragonfruit | ")
    #t.sidebar.success("Select an Option")
    menu = ["Home", "Track Pain", "Track Meds", "Track Sleep", "Track Vitals", "Track Metrics", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    patient = st.sidebar.selectbox("User", ["Adge", "Becky", "Fitzy"])
    you = "sir"
    
    if patient == "Becky":
        you = "ma'am"
    
    pain_types = ["sharp", "dull", "stabbing", "burning", "cramping", "throbbing", "shooting", "aching", "stinging", "sore", "tight", "tender", "numb", "pins and needles", "other"]

    # ----------------------------
    # Each Individual Page
    # ----------------------------
    
    if choice == "Home":
        #st.write("Welcome to Dragonfruit")
        st.markdown(
            """
            ## Family Information Tracking System (FITS)
            
            Select an option from the menu to get started.        
            """)
    
    if choice == "Track Pain":
        # ----------------------------
        # pain management form
        # ----------------------------
        with st.form("pain_mgmt"):
            st.write(f"# Pain Tracking")
            
            #st.header("Location")
            if patient == "Becky":
                common_pain_locations = ["lower-right-quadrant", "lower back", "middle of back", "ovaries", "migraine", "headache"]
            else:
                common_pain_locations = ["lower back", "middle of back", "neck", "neck-headache", "headache"]
            
            common_locations = st.multiselect(f"***{patient}*** Common Locations", common_pain_locations)
            st.write("If your pain is somewhere else, provide it in the `Location` field below.")
            location = st.text_input("Location")
            
            #st.header("Type of Pain")
            #type = st.choice("Type", pain_types)
            type = st.multiselect("Type", pain_types, default='aching')
            
            #st.header("Severity")
            #level = st.slider("Level", 0, 10, 5)
            level = st.number_input("Pain Level", 0, 10, 5)

            #st.header("Anything else you'd like to say?")
            notes = st.text_area("Notes")
            dt = st.date_input("Date", date.today())
            tm = st.time_input("Time", time(datetime.now().hour, datetime.now().minute))
            submit_button = st.form_submit_button(label="Save Data")
        
        # results
        if submit_button:
            if len(location) != 0:
                common_locations.append(location)
            
            st.success(f"Good evening, {you}.")
            st.write(f"Location: {location}")
            st.write(f"Type: {type}")
            st.write(f"Level: {level}")
            st.write(f"Notes: {notes}")
            st.write(f"Date: {dt}")
            st.write(f"Time: {tm}")
            st.write(f"Common Locations: {common_locations}")
            st.write(f"Patient: {patient}")

            pain_type = type
            pain_level = level
            pain_location = location
            pain_notes = notes
            pain_date = dt
            pain_time = tm
            pain_common_locations = common_locations
            pain_patient = patient



    if choice == "Track Meds":
        ...
    
    if choice == "About":
        st.markdown("## About Dragonfruit")

    

    

        


if __name__ == "__main__":
    main()