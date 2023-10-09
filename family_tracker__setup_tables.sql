-- Name: family_tracker.sql
-- Description: SQLite Database schema for a family tracking app
-- Author: Adge Denkers / github.com/adgedenkers/
-- Created: 2023-10-05
-- Updated: 2023-10-08
-- (C) 2023 denkers.co

-- Enable Foreign Key Support
PRAGMA foreign_keys = ON;

CREATE TABLE user_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Unique identifier for each user profile
    userName VARCHAR(255) NOT NULL UNIQUE,  -- User's username (non-null and unique)
    namePrefix VARCHAR(255),                -- User's name prefix (e.g., Mr., Mrs.)
    nameFirst VARCHAR(255) NOT NULL,        -- User's first name (non-null)
    nameMiddle VARCHAR(255),                -- User's middle name
    nameLast VARCHAR(255) NOT NULL,         -- User's last name (non-null)
    nameSuffix VARCHAR(255),                -- User's name suffix
    dob TEXT,                               -- User's date and time of birth (stored as text)
    userPassword VARCHAR(255),              -- User's password (hashed)
    email VARCHAR(255) NOT NULL,            -- User's email (non-null)
    phone VARCHAR(10),                      -- User's phone number
    address VARCHAR(255),                   -- User's address
    city VARCHAR(255),                      -- User's city
    state VARCHAR(2),                       -- User's state
    zip VARCHAR(5),                         -- User's zip code
    country VARCHAR(255),                   -- User's country
    created_at TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')) NOT NULL -- Timestamp for when the profile was created
);

-- Insert family data into the user_profiles table
INSERT INTO user_profiles (userName, namePrefix, nameFirst, nameMiddle, nameLast, dob, email, phone, address, city, state, zip, country) VALUES
('Adge', 'Mr.', 'Adriaan', 'Harold', 'Denkers', '1977-11-22 08:45:22.123-0500', 'adge.denkers@gmail.com', '607-226-0710', '304 Cosen Road', 'Oxford', 'NY', '13830', 'United States'),
('Becky', 'Mrs.', 'Rebecca', 'Lydia', 'Denkers', '1978-08-19 14:02:33.123-0400', 'rebecca.denkers@gmail.com', '607-316-2604', '304 Cosen Road', 'Oxford', 'NY', '13830', 'United States'),
('Fitz', 'Mr.', 'Adriaan', 'Fitzgerald', 'Denkers', '2010-09-008 14:39:11.123-0400', 'bonniegamer0812@gmail.com', '607-226-3077', '304 Cosen Road', 'Oxford', 'NY', '13830', 'United States');


-- Create the user_access table
CREATE TABLE IF NOT EXISTS user_access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user_profiles(id),
    website_username VARCHAR(255),
    website_password VARCHAR(255),
    url VARCHAR(255),
    active INTEGER DEFAULT 1,
    quick_find_word VARCHAR(255)
);

-- Insert initial records into the table
INSERT INTO user_access (user_id, website_username, website_password, url, active, quick_find_word) VALUES
(1, "bonniegamer0812@gmail.com", "pePgir-tifhoc-9hummo", "https://students.arbitersports.com/registrations/12365092/edit?vue=true", 1, "oxford/oxac/sports");



-- Create Medical Table for User's Basic Medical Data
CREATE TABLE IF NOT EXISTS user_medical_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user_profiles(id),
    blood_type VARCHAR(5),
);


INSERT INTO TABLE user_medical_info (user_id, blood_type) VALUES (1, "O+"), (2, "A+"), (3, "");



-- Create Medication Groups Table
CREATE TABLE IF NOT EXISTS med_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user_profiles(id),
    group_name TEXT,
    schedule TEXT,
    time_of_day TEXT
);

-- Create Medication Group Contents Table
CREATE TABLE IF NOT EXISTS med_group_contents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER REFERENCES med_groups(id),
    medication_id INTEGER REFERENCES meds(id)
);

-- Create User Medications Table
CREATE TABLE IF NOT EXISTS user_meds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user_profiles(id),
    medication_id INTEGER REFERENCES meds(id)
    dosage REAL
);

-- Create Medications Table
CREATE TABLE IF NOT EXISTS meds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prescription BOOLEAN DEFAULT 1,
    user_id INTEGER REFERENCES user_profiles(id),
    NDC TEXT,
    medication TEXT,
    brand_name TEXT,
    strength REAL,
    units TEXT,
    format TEXT,
    FOREIGN KEY (user_id) REFERENCES user_profiles(id)
);

-- Create User Meds Scheduled Table
CREATE TABLE IF NOT EXISTS user_meds_scheduled (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user_profiles(id),
    med_group_id INTEGER,
    taken_at TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_profiles(id),
    FOREIGN KEY (med_group_id) REFERENCES med_groups(id)
);

-- Create User Meds Unscheduled Table
CREATE TABLE IF NOT EXISTS user_meds_unscheduled (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user_profiles(id),
    med_id INTEGER,
    dosage REAL,
    units TEXT,
    reason TEXT,
    taken_at TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_profiles(id),
    FOREIGN KEY (med_id) REFERENCES meds(id)
);
