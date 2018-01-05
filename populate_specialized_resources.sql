--Water
INSERT INTO water(rid, wtype, wbrand) 
VALUES (1, 'Bottled Water', 'Dasani');
INSERT INTO water(rid, wtype, wbrand) 
VALUES (39, 'Gallon', 'Dasani');
INSERT INTO water(rid, wtype, wbrand) 
VALUES (40, 'Bottled Water', 'Nice');
INSERT INTO water(rid, wtype, wbrand) 
VALUES (44, 'Bottled Water', 'Aquafina');
INSERT INTO water(rid, wtype, wbrand) 
VALUES (55, 'Bottled Water', 'Aquafina');
--Heavy equipment
INSERT INTO heavy_equipment(rid, hetype, hebrand, hesize, heweight, hemodel)
VALUES (2, 'Forklift', 'Toyota', 'small', '10000 lb', 'MD123');
INSERT INTO heavy_equipment(rid, hetype, hebrand, hesize, heweight, hemodel)
VALUES (10, 'Cement Mixer', 'Toyota', 'medium', '5000 lb', 'CM123');
INSERT INTO heavy_equipment(rid, hetype, hebrand, hesize, heweight, hemodel)
VALUES (15, 'Bulldozer', 'Caterpillar', 'large', '50000 lb', 'BD123');
INSERT INTO heavy_equipment(rid, hetype, hebrand, hesize, heweight, hemodel)
VALUES (16, 'Digger', 'Caterpillar', 'large', '500000 lb', 'DD123');
INSERT INTO heavy_equipment(rid, hetype, hebrand, hesize, heweight, hemodel)
VALUES (54, 'Digger', 'Caterpillar', 'small', '50000 lb', 'DD123');
--Fuel
INSERT INTO fuel(rid, fltype, floctane, flbrand) 
VALUES (3, 'Premium', 92, 'Puma');
INSERT INTO fuel(rid, fltype, floctane, flbrand) 
VALUES (23, 'Regular', 87, 'Puma');
INSERT INTO fuel(rid, fltype, floctane, flbrand) 
VALUES (36, 'Regular', 87, 'Puma');
INSERT INTO fuel(rid, fltype, floctane, flbrand) 
VALUES (36, 'Diesel', 15, 'Puma');
INSERT INTO fuel(rid, fltype, floctane, flbrand) 
VALUES (46, 'Regular', 87, 'Puma');
--Batteries
INSERT INTO batteries(rid, btype, bsize, bbrand) 
VALUES (4, 'C', 12,'Energizer');
INSERT INTO batteries(rid, btype, bsize, bbrand) 
VALUES (5, 'AA', 24, 'Energizer');
INSERT INTO batteries(rid, btype, bsize, bbrand) 
VALUES (13, 'AAA', 24, 'Duracel');
INSERT INTO batteries(rid, btype, bsize, bbrand) 
VALUES (38, 'D', 12, 'Duracel');
INSERT INTO batteries(rid, btype, bsize, bbrand) 
VALUES (43, 'AA', 8, 'Duracel');
--Clothes
INSERT INTO clothes(rid, cgender, cbrand, cmaterial) 
VALUES (6, 'Male', 'Hanes', 'Cotton');
INSERT INTO clothes(rid, cgender, cbrand, cmaterial) 
VALUES (26, 'Female', 'Hanes', 'Cotton');
INSERT INTO clothes(rid, cgender, cbrand, cmaterial) 
VALUES (27, 'Unisex', 'Hanes', 'Cotton');
INSERT INTO clothes(rid, cgender, cbrand, cmaterial) 
VALUES (29, 'Unisex', 'Relevo Por La Vida', 'Cotton');
INSERT INTO clothes(rid, cgender, cbrand, cmaterial) 
VALUES (48, 'Baby', 'Hanes', 'Cotton');
--ice
INSERT INTO ice(rid, isize) VALUES (7,'small');
INSERT INTO ice(rid, isize) VALUES (9,'medium');
INSERT INTO ice(rid, isize) VALUES (19,'medium');
INSERT INTO ice(rid, isize) VALUES (30,'large');
INSERT INTO ice(rid, isize) VALUES (52,'large');
--Medication
INSERT INTO medication(rid, mtype, mamount, mdose, mbrand) 
VALUES (8, 'Pills', '100 pills', '80 mg', 'Bayer');
INSERT INTO medication(rid, mtype, mamount, mdose, mbrand) 
VALUES (17, 'Pills', '54 pills', '200 mg', 'Panadol');
INSERT INTO medication(rid, mtype, mamount, mdose, mbrand) 
VALUES (18, 'Syrup', '5 oz', '2 tb', 'CureMe');
INSERT INTO medication(rid, mtype, mamount, mdose, mbrand) 
VALUES (18, 'Pills', '24 capsules', '100 mg', 'CureMe');
INSERT INTO medication(rid, mtype, mamount, mdose, mbrand) 
VALUES (51, 'Pills', '24 capsules', '200 mg', 'Advil');
--Food
INSERT INTO food(rid, ftype, fbrand, famount, fexp_date)
VALUES (11, 'Canned Food', 'Chef Boyardee', '15oz', '25-12-2019');
INSERT INTO food(rid, ftype, fbrand, famount, fexp_date)
VALUES (12, 'Dry Food', 'General Mills', '11oz', '21-03-2018');
INSERT INTO food(rid, ftype, fbrand, famount, fexp_date)
VALUES (12, 'Baby Food', 'Gerber', '2oz', '25-05-2018');
INSERT INTO food(rid, ftype, fbrand, famount, fexp_date)
VALUES (37, 'Canned Food', 'Chef Boyardee', '15oz', '25-12-2019');
INSERT INTO food(rid, ftype, fbrand, famount, fexp_date)
VALUES (37, 'Dry Food', 'Military Food', '15oz', '25-12-2019');
--Power Generators
INSERT INTO power_generators(rid, pgbrand, pgwatts, pggas)
VALUES (21, 'Caterpillar', 3000, 'Gas');
INSERT INTO power_generators(rid, pgbrand, pgwatts, pggas)
VALUES (22, 'Honda', 6200, 'Gasoline');
INSERT INTO power_generators(rid, pgbrand, pgwatts, pggas)
VALUES (32, 'Honda', 2400, 'Gasoline');
INSERT INTO power_generators(rid, pgbrand, pgwatts, pggas)
VALUES (35, 'Champion', 4700, 'Diesel');
INSERT INTO power_generators(rid, pgbrand, pgwatts, pggas)
VALUES (47, 'Champion', 2100, 'Gasoline');
--Tools
INSERT INTO tools(rid, ttype, tbrand) VALUES (24, 'Nails', 'Iron Head');
INSERT INTO tools(rid, ttype, tbrand) VALUES (28, 'Hammer', 'Craftman');
INSERT INTO tools(rid, ttype, tbrand) VALUES (34, 'Screwdriver', 'Craftman');
INSERT INTO tools(rid, ttype, tbrand) VALUES (41, 'Screwdriver', 'Craftman');
INSERT INTO tools(rid, ttype, tbrand) VALUES (49, 'Wrench', 'Craftman');
--Medical Devices
INSERT INTO medical_devices(rid, mdtype, mdbrand, mdpower_type, mdprecision)
VALUES (31, 'Glucose Meter', 'Sejoy', 'Battery', 0.0001);
INSERT INTO medical_devices(rid, mdtype, mdbrand, mdpower_type, mdprecision)
VALUES (33, 'Glucose Meter', 'Sejoy', 'Battery', 0.0001);
INSERT INTO medical_devices(rid, mdtype, mdbrand, mdpower_type, mdprecision)
VALUES (33, 'Syringe', 'Sejoy', 'None', 0);
INSERT INTO medical_devices(rid, mdtype, mdbrand, mdpower_type, mdprecision)
VALUES (50, 'Glucose Meter', 'Sejoy', 'Battery', 0.0001);