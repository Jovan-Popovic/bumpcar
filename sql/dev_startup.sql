INSERT INTO base_brand (value) VALUES
('Audi'),  ('BMW'),     ('Fiat'),  ('Ford'),   ('Kia'),
('Mazda'), ('Porsche'), ('Smart'), ('Tesla'),  ('Volvo');

INSERT INTO base_color (value) VALUES
('Black'), ('Blue'),    ('Brown'), ('Gold'),   ('Gray'),
('Green'), ('Orange'),  ('Red'),   ('Silver'), ('White');

INSERT INTO base_condition (value) VALUES
('New'), ('Used');

INSERT INTO base_drivetrain (value) VALUES
('All-wheel drive'), ('Four-wheel drive'), ('Front-wheel drive'), ('Rear-wheel drive');

INSERT INTO base_fueltype (value) VALUES
('Gasoline'), ('Diesel'), ('Biodiesel'), ('Ethanol'),
('Compressed Natural Gas'), ('Liquified Petroleum Gas'), ('Hydrogen'), ('Electric');

INSERT INTO base_geartype (value) VALUES
('Manual transmission'), ('Automatic transmission'),
('Continuously variable transmission'), ('Semi-automatic and dual-clutch transmissions');

INSERT INTO base_vehicletype (value) VALUES
('Car'), ('Motorcycle');

INSERT INTO base_brandmodel (value, brand_id, banner, image1, image2, image3) VALUES
('Model S', 'Tesla', '', '', '', ''), ('Model 3', 'Tesla', '', '', '', ''), ('Model X', 'Tesla', '', '', '', ''), ('Model Y', 'Tesla', '', '', '', '');
