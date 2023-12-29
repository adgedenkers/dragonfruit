-- Terpenes Table
CREATE TABLE terpenes (
    id INT PRIMARY KEY IDENTITY,
    name NVARCHAR(255) NOT NULL,
    iupac_name NVARCHAR(255),
    molecular_formula NVARCHAR(50),
    molecular_weight DECIMAL(10, 2),
    boiling_point DECIMAL(10, 2),
    density DECIMAL(10, 4),
    solubility NVARCHAR(255),
    flavor_profile NVARCHAR(MAX),
    aroma_profile NVARCHAR(MAX),
    effects NVARCHAR(MAX),
    sources NVARCHAR(MAX),
    notes NVARCHAR(MAX)
);

-- Strains Table
CREATE TABLE strains (
    id INT PRIMARY KEY IDENTITY,
    name NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX),
    thc_content DECIMAL(5, 2),
    cbd_content DECIMAL(5, 2),
    indica_sativa_ratio NVARCHAR(50),
    flowering_time VARCHAR(50),
    yield NVARCHAR(50),
    medical_uses NVARCHAR(MAX),
    flavor NVARCHAR(MAX),
    origin NVARCHAR(255)
);

CREATE TABLE strain_effects_links (
    strain_id INT,
    effect_id INT,
    PRIMARY KEY (strain_id, effect_id),
    FOREIGN KEY (strain_id) REFERENCES strains(id),
    FOREIGN KEY (effect_id) REFERENCES effects(id)
);


-- Effects Table
CREATE TABLE effects (
    id INT PRIMARY KEY IDENTITY,
    description NVARCHAR(255) NOT NULL
);

-- FlavorProfiles Table
CREATE TABLE flavor_profiles (
    id INT PRIMARY KEY IDENTITY,
    description NVARCHAR(255) NOT NULL
);

-- AromaProfiles Table
CREATE TABLE aroma_profiles (
    id INT PRIMARY KEY IDENTITY,
    description NVARCHAR(255) NOT NULL
);

-- Linking Tables
CREATE TABLE terpene_strain_links (
    id INT PRIMARY KEY IDENTITY,
    terpene_id INT,
    strain_id INT,
    concentration DECIMAL(10, 4),
    FOREIGN KEY (terpene_id) REFERENCES terpenes(id),
    FOREIGN KEY (strain_id) REFERENCES strains(id)
);

CREATE TABLE strain_effects_links (
    strain_id INT,
    effect_id INT,
    PRIMARY KEY (strain_id, effect_id),
    FOREIGN KEY (strain_id) REFERENCES strains(id),
    FOREIGN KEY (effect_id) REFERENCES effects(id)
);

CREATE TABLE strain_flavor_links (
    strain_id INT,
    flavor_id INT,
    PRIMARY KEY (strain_id, flavor_id),
    FOREIGN KEY (strain_id) REFERENCES strains(id),
    FOREIGN KEY (flavor_id) REFERENCES flavor_profiles(id)
);

CREATE TABLE terpene_flavor_links (
    terpene_id INT,
    flavor_id INT,
    PRIMARY KEY (terpene_id, flavor_id),
    FOREIGN KEY (terpene_id) REFERENCES terpenes(id),
    FOREIGN KEY (flavor_id) REFERENCES flavor_profiles(id)
);

CREATE TABLE terpene_aroma_links (
    terpene_id INT,
    aroma_id INT,
    PRIMARY KEY (terpene_id, aroma_id),
    FOREIGN KEY (terpene_id) REFERENCES terpenes(id),
    FOREIGN KEY (aroma_id) REFERENCES aroma_profiles(id)
);

CREATE TABLE terpene_effect_links (
    terpene_id INT,
    effect_id INT,
    PRIMARY KEY (terpene_id, effect_id),
    FOREIGN KEY (terpene_id) REFERENCES terpenes(id),
    FOREIGN KEY (effect_id) REFERENCES effects(id)
);


INSERT INTO terpenes (name, iupac_name, molecular_formula, molecular_weight, boiling_point, density, solubility, flavor_profile, aroma_profile, effects, sources, notes) 
VALUES
('Myrcene', '7-Methyl-3-methylene-1,6-octadiene', 'C10H16', 136.23, 168.4, 0.792, 'Insoluble in water, soluble in ethanol', 'Earthy, musky, fruity', 'Herbal, Clove-like', 'Relaxation, Sedation', 'Mango, Lemongrass', 'Most common terpene in cannabis, also found in hops'),
('Limonene', '1-Methyl-4-(1-methylethenyl)-cyclohexene', 'C10H16', 136.24, 176.0, 0.841, 'Insoluble in water, soluble in ethanol', 'Citrus', 'Lemon, Orange', 'Mood Elevation, Stress Relief', 'Citrus rinds, Peppermint', 'Second most abundant terpene in cannabis, common in sativa strains'),
('Caryophyllene', '4,11,11-Trimethyl-8-methylenebicyclo[7.2.0]undec-4-ene', 'C15H24', 204.35, 119.0, 0.906, 'Insoluble in water, soluble in ethanol', 'Peppery, spicy', 'Wood, Spice', 'Anti-inflammatory, Analgesic', 'Black pepper, Cloves', 'The only terpene known to interact with the endocannabinoid system'),
('Linalool', '3,7-Dimethyl-1,6-octadien-3-ol', 'C10H18O', 154.25, 198.0, 0.867, 'Insoluble in water, soluble in ethanol', 'Floral', 'Lavender, Sweet', 'Calming, Anti-anxiety', 'Lavender, Birch bark', 'Common in lavender, used for its calming effects'),
('Pinene', 'C10H16', 'C10H16', 136.24, 155.0, 0.860, 'Insoluble in water, soluble in ethanol', 'Pine', 'Pine, Rosemary', 'Alertness, Bronchodilator', 'Pine trees, Rosemary', 'Most abundant terpene in nature, known for its sharp pine aroma'),
('Humulene', 'C15H24', 'C15H24', 204.35, 106.0, 0.889, 'Insoluble in water, soluble in ethanol', 'Earthy, woody', 'Hops, Coriander', 'Anti-inflammatory, Appetite suppressant', 'Hops, Coriander', 'Common in hops and coriander'),
('Terpinolene', 'C10H16', 'C10H16', 136.24, 185.0, 0.860, 'Insoluble in water, soluble in ethanol', 'Piney, floral', 'Apples, Cumin', 'Antioxidant, Sedative', 'Apples, Tea Tree', 'Known for its complex scent, a mix of floral, herbal, and citrus tones'),
('Ocimene', 'C15H24', 'C15H24', 204.35, 100.0, 0.810, 'Insoluble in water, soluble in ethanol', 'Sweet, herbal', 'Mint, Parsley', 'Antiviral, Anti-inflammatory', 'Orchids, Mint', 'Known for its pleasant sweet, herbal scent');


-- Effects
INSERT INTO effects (description) VALUES
('Relaxation'),
('Sedation'),
('Mood Elevation'),
('Stress Relief'),
('Anti-inflammatory'),
('Analgesic'),
('Calming'),
('Anti-anxiety'),
('Alertness'),
('Bronchodilator'),
('Appetite suppressant'),
('Antioxidant'),
('Antiviral');

-- Flavor Profiles
INSERT INTO flavor_profiles (description) VALUES
('Earthy'),
('Musky'),
('Fruity'),
('Citrus'),
('Peppery'),
('Spicy'),
('Floral'),
('Pine'),
('Woody'),
('Sweet'),
('Herbal');

-- Aroma Profiles
INSERT INTO aroma_profiles (description) VALUES
('Herbal'),
('Clove-like'),
('Lemon'),
('Orange'),
('Wood'),
('Spice'),
('Lavender'),
('Sweet'),
('Pine needles'),
('Rosemary'),
('Hops'),
('Coriander'),
('Apples'),
('Cumin'),
('Mint'),
('Parsley'),
('Tea Tree');

-- Linking Myrcene (assuming ID 1) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(1, 1),  -- Relaxation
(1, 2);  -- Sedation

-- Linking Limonene (assuming ID 2) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(2, 3),  -- Mood Elevation
(2, 4);  -- Stress Relief

-- Linking Caryophyllene (assuming ID 3) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(3, 5),  -- Anti-inflammatory
(3, 6);  -- Analgesic

-- Linking Linalool (assuming ID 4) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(4, 7),  -- Calming
(4, 8);  -- Anti-anxiety

-- Linking Pinene (assuming ID 5) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(5, 9),  -- Alertness
(5, 10); -- Bronchodilator

-- Linking Humulene (assuming ID 6) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(6, 5),  -- Anti-inflammatory
(6, 11); -- Appetite suppressant

-- Linking Terpinolene (assuming ID 7) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(7, 12), -- Antioxidant
(7, 7);  -- Calming

-- Linking Ocimene (assuming ID 8) with its effects
INSERT INTO terpene_effect_links (terpene_id, effect_id) VALUES
(8, 13), -- Antiviral
(8, 5);  -- Anti-inflammatory

-- Linking Myrcene (assuming ID 1) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(1, 1),  -- Herbal
(1, 2);  -- Clove-like

-- Linking Limonene (assuming ID 2) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(2, 3),  -- Lemon
(2, 4);  -- Orange

-- Linking Caryophyllene (assuming ID 3) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(3, 5),  -- Wood
(3, 6);  -- Spice

-- Linking Linalool (assuming ID 4) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(4, 7),  -- Lavender
(4, 8);  -- Sweet

-- Linking Pinene (assuming ID 5) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(5, 9),  -- Pine needles
(5, 10); -- Rosemary

-- Linking Humulene (assuming ID 6) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(6, 11), -- Hops
(6, 12); -- Coriander

-- Linking Terpinolene (assuming ID 7) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(7, 13), -- Apples
(7, 14); -- Cumin

-- Linking Ocimene (assuming ID 8) with its aromas
INSERT INTO terpene_aroma_links (terpene_id, aroma_id) VALUES
(8, 15), -- Mint
(8, 16); -- Parsley


-- Linking Myrcene (assuming ID 1) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(1, 1),  -- Earthy
(1, 2),  -- Musky
(1, 3);  -- Fruity

-- Linking Limonene (assuming ID 2) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(2, 4);  -- Citrus

-- Linking Caryophyllene (assuming ID 3) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(3, 5),  -- Peppery
(3, 6);  -- Spicy

-- Linking Linalool (assuming ID 4) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(4, 7);  -- Floral

-- Linking Pinene (assuming ID 5) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(5, 8);  -- Pine

-- Linking Humulene (assuming ID 6) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(6, 1),  -- Earthy
(6, 9);  -- Woody

-- Linking Terpinolene (assuming ID 7) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(7, 10), -- Sweet
(7, 11); -- Herbal

-- Linking Ocimene (assuming ID 8) with its flavors
INSERT INTO terpene_flavor_links (terpene_id, flavor_id) VALUES
(8, 11); -- Herbal


