-- Name: family_tracker_full.sql
-- Description: Complete SQLite Database schema for a family tracking app
-- Author: Adge Denkers / github.com/adgedenkers/
-- Created: 2023-10-05
-- Updated: 2023-10-09
-- (C) 2023 denkers.co
-- Enable Foreign Key Support
PRAGMA foreign_keys = ON;
-- user_profiles Table
CREATE TABLE user_profiles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  userName TEXT NOT NULL UNIQUE,
  namePrefix TEXT,
  nameFirst TEXT NOT NULL,
  nameMiddle TEXT,
  nameLast TEXT NOT NULL,
  nameSuffix TEXT,
  dob TEXT,
  userPassword TEXT,
  email TEXT NOT NULL,
  phone TEXT,
  address TEXT,
  city TEXT,
  state TEXT,
  zip TEXT,
  country TEXT,
  created_at TEXT DEFAULT (
    strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')
  ) NOT NULL FOREIGN KEY (user_id) REFERENCES users(id)
);
-- Insert Statements
INSERT INTO
  user_profiles (
    user_id,
    userName,
    namePrefix,
    nameFirst,
    nameMiddle,
    nameLast,
    dob,
    email,
    phone,
    address,
    city,
    state,
    zip,
    country
  )
VALUES
  (
    1,
    'Adge',
    'Mr.',
    'Adriaan',
    'Harold',
    'Denkers',
    '1977-11-22T08:45:22-0500',
    'adge.denkers@gmail.com',
    '607-226-0710',
    '304 Cosen Road',
    'Oxford',
    'NY',
    '13830',
    'United States'
  ),
  (
    2,
    'Becky',
    'Mrs.',
    'Rebecca',
    'Lydia',
    'Denkers',
    '1978-08-19T14:02:33-0400',
    'rebecca.denkers@gmail.com',
    '607-316-2604',
    '304 Cosen Road',
    'Oxford',
    'NY',
    '13830',
    'United States'
  ),
  (
    3,
    'Fitz',
    'Mr.',
    'Adriaan',
    'Fitzgerald',
    'Denkers',
    '2010-09-08T14:39:11-0400',
    'bonniegamer0812@gmail.com',
    '607-226-3077',
    '304 Cosen Road',
    'Oxford',
    'NY',
    '13830',
    'United States'
  );
-- user_access Table
CREATE TABLE IF NOT EXISTS user_access (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  login_time DATETIME,
  logout_time DATETIME,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- user_medical_info Table
CREATE TABLE IF NOT EXISTS user_medical_info (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  blood_type TEXT,
  allergies TEXT,
  medical_conditions TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- med_groups Table
CREATE TABLE IF NOT EXISTS med_groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  group_name TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- med_group_contents Table
CREATE TABLE IF NOT EXISTS med_group_contents (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_id INTEGER,
  medication_id INTEGER,
  FOREIGN KEY(group_id) REFERENCES med_groups(id),
  FOREIGN KEY(medication_id) REFERENCES meds(id)
);
-- meds Table
CREATE TABLE IF NOT EXISTS meds (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  prescription BOOLEAN DEFAULT 1,
  user_id INTEGER,
  medication_name TEXT,
  dosage TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- user_meds Table
CREATE TABLE IF NOT EXISTS user_meds (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  medication_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id),
  FOREIGN KEY(medication_id) REFERENCES meds(id)
);
-- user_meds_scheduled Table
CREATE TABLE IF NOT EXISTS user_meds_scheduled (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  med_group_id INTEGER,
  time_to_take DATETIME,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id),
  FOREIGN KEY(med_group_id) REFERENCES med_groups(id)
);
-- user_meds_unscheduled Table
CREATE TABLE IF NOT EXISTS user_meds_unscheduled (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  med_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id),
  FOREIGN KEY(med_id) REFERENCES meds(id)
);
-- appointments Table
CREATE TABLE IF NOT EXISTS appointments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  appointment_name TEXT,
  appointment_date DATETIME,
  description TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- reminders Table
CREATE TABLE IF NOT EXISTS reminders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  reminder_name TEXT,
  reminder_date DATETIME,
  description TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- tasks Table
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  task_name TEXT,
  due_date DATETIME,
  status TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);
-- chores Table
CREATE TABLE IF NOT EXISTS chores (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  chore_name TEXT,
  due_date DATETIME,
  status TEXT,
  FOREIGN KEY(user_id) REFERENCES user_profiles(user_id)
);