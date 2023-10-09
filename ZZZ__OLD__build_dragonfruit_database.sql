CREATE TABLE
    people (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        user_id INT NOT NULL,                           -- foreign key to users table
        full_name VARCHAR(255),                         -- full name of the user, as used in official documents and reports
        name VARCHAR(255),                              -- name of the user, as used in informal settings
        email VARCHAR(255),                             -- email address of the user
        FOREIGN KEY (user_id) REFERENCES users(id)
    )

CREATE TABLE 
    medications (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        medication VARCHAR(100),                        -- our common name for this medication
        generic_name VARCHAR(255),                      -- the generic name for this medication
        brand_name VARCHAR(255),                        -- the brand name for this medication
        description VARCHAR(255),                       -- a description of this medication
    )

CREATE TABLE
    medication_stubs (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
        stub VARCHAR(100) NOT NULL,                     -- text-based unique identifier, easy to read and understand 
        medication_id INT NOT NULL,                     -- foreign key to medications table
        medication_dosage_id INT NOT NULL,              -- foreign key to medication_dosages table
        FOREIGN KEY (medication_id) REFERENCES medications(id),
        FOREIGN KEY (medication_dosage_id) REFERENCES medication_dosages(id)
    )

CREATE TABLE
    medication_availability (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        medication_id INT NOT NULL,                     -- foreign key to medications table
        medication_availability VARCHAR(255),           -- how the medication is available - prescription, otc, etc.
        FOREIGN KEY (medication_id) REFERENCES medications(id)
    )

CREATE TABLE
    medication_dosages (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        medication_id INT NOT NULL,                     -- foreign key to medications table
        dosage VARCHAR(255),                            -- the dosage of the medication
        dosage_unit VARCHAR(255),                       -- the unit of the dosage
        dosage_frequency VARCHAR(255),                  -- how often the dosage is taken
        dosage_duration FLOAT,                          -- number of hours between dosages
        FOREIGN KEY (medication_id) REFERENCES medications(id)
    )

CREATE TABLE
    medication_side_effects (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        medication_id INT NOT NULL,                     -- foreign key to medications table
        side_effect_id INT NOT NULL,                    -- foreign key to side_effects table
        FOREIGN KEY (medication_id) REFERENCES medications(id),
        FOREIGN KEY (side_effect_id) REFERENCES side_effects(id)
    )

CREATE TABLE
    side_effects (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        side_effect VARCHAR(255),                       -- the side effect
        additional_information VARCHAR(255),            -- additional information about the side effect
        seriousness VARCHAR(255),                       -- how serious the side effect is
        duration VARCHAR(255),                          -- how long the side effect lasts
        overdose_warning INT                            -- whether or not this side effect is a warning sign of overdose
    )

CREATE TABLE
    prescriptions (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        medication_stub_id INT NOT NULL,                -- foreign key to medication_stubs table
        physician_id INT NOT NULL,                      -- foreign key to physicians table
    )

CREATE VIEW
    list_of_medication_stubs_w_medication_info (
        SELECT
            s.stub,                                     -- [medication_stubs].[stub]                            -- our unique identifier for this stub
            m.medication,                               -- [medications].[medication]                           -- our common name for this medication
            m.generic_name,                             -- [medications].[generic_name]                         -- the generic name for this medication
            m.brand_name,                               -- [medications].[brand_name]                           -- the brand name for this medication
            m.medication_availability,                  -- [medication_availability].[medication_availability]  -- how the medication is available - prescription, otc, etc.
            d.dosage,                                   -- [medication_dosages].[dosage]                        -- the dosage of the medication
            d.dosage_unit,                              -- [medication_dosages].[dosage_unit]                   -- the unit of the dosage
            d.dosage_frequency,                         -- [medication_dosages].[dosage_frequency]              -- how often the dosage is taken
            d.dosage_duration                           -- [medication_dosages].[dosage_duration]               -- number of hours between dosages
        FROM medication_stubs s 
            INNER JOIN medications m ON s.medication_id = m.id
            INNER JOIN medication_dosages d ON s.medication_dosage_id = d.id
    )
    


CREATE TABLE
    physicians (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        name_first VARCHAR(255),                        -- first name of the physician
        name_last VARCHAR(255),                         -- last name of the physician
        name_middle VARCHAR(255),                       -- middle name of the physician
        name_suffix VARCHAR(255),                       -- suffix of the physician
        specialty_id VARCHAR(255),                      -- the specialty of the physician
        address VARCHAR(255),                           -- the address of the physician
        city VARCHAR(255),                              -- the city of the physician
        state VARCHAR(255),                             -- the state of the physician
        zip_code VARCHAR(255),                          -- the zip code of the physician
        phone VARCHAR(255),                             -- the phone number of the physician
        fax VARCHAR(255),                               -- the fax number of the physician
        email VARCHAR(255),                             -- the email address of the physician
        website VARCHAR(255),                           -- the website of the physician
        FOREIGN KEY (specialty_id) REFERENCES medical_speciality(id)
    )

CREATE TABLE
    patient_physicians (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        person_id INT NOT NULL,                         -- foreign key to people table
        physician_id INT NOT NULL,                      -- foreign key to physicians table
        date_started DATE NULL,                         -- the date the patient started seeing this physician
        date_stopped DATE NULL,                         -- the date the patient stopped seeing this physician
        currently_seeing INT NOT NULL DEFAULT 0,        -- whether or not the patient is currently seeing this physician
        comments VARCHAR(255),                          -- any comments about this physician
        FOREIGN KEY (person_id) REFERENCES people(id),
        FOREIGN KEY (physician_id) REFERENCES physicians(id)
    )

CREATE TABLE
    medical_speciality (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        specialty VARCHAR(255),                         -- the specialty of the physician
        description VARCHAR(255),                       -- a description of the specialty
    )

CREATE TABLE
    diagnosed_conditions (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        person_id INT NOT NULL,                         -- foreign key to people table
        condition_id INT NOT NULL,                      -- foreign key to conditions table
        FOREIGN KEY (person_id) REFERENCES people(id),
        FOREIGN KEY (condition_id) REFERENCES conditions(id)
    )

CREATE TABLE
    diagnosis_details (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        diagnosed_condition_id INT NOT NULL,            -- foreign key to diagnosed_conditions table
        diagnosing_physician_id INT NOT NULL,           -- foreign key to physicians table
        diagnosis VARCHAR(255),                         -- the diagnosis
        diagnosis_code VARCHAR(255),                    -- the diagnosis code
        FOREIGN KEY (diagnosed_condition_id) REFERENCES diagnosed_conditions(id),
        FOREIGN KEY (person_id) REFERENCES people(id),
        FOREIGN KEY (physician_id) REFERENCES physicians(id)
    )

CREATE TABLE
    conditions (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        condition VARCHAR(255),                         -- the condition
        description VARCHAR(255),                       -- a description of the condition
        additional_information VARCHAR(255)             -- additional information about the condition
    )

CREATE TABLE
    physician_conditions(
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        physician_id INT NOT NULL,                      -- foreign key to physicians table
        condition_id INT NOT NULL,                      -- foreign key to conditions table
        FOREIGN KEY (physician_id) REFERENCES physicians(id),
        FOREIGN KEY (condition_id) REFERENCES conditions(id)
    )

CREATE TABLE
    condition_side_effects (
        id INT NOT NULL PRIMARY KEY IDENTITY(1,1),      -- unique, primary key
        condition_id INT NOT NULL,                      -- foreign key to conditions table
        side_effect_id INT NOT NULL,                    -- foreign key to side_effects table
        FOREIGN KEY (condition_id) REFERENCES conditions(id),
        FOREIGN KEY (side_effect_id) REFERENCES side_effects(id)
    )
    