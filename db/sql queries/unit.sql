
INSERT IGNORE INTO unit 
(unit_id, unit_name, unit_symbol, unit_class, conversion_factor, conversion_offset, converts_to)
VALUES
(1, 'gram', 'g', 'mass', 1, 0, 'gram'), 
(2, 'milligram', 'mg', 'mass', .001, 0, 'gram'), 
(3, 'Kilocalorie', 'kcal', 'energy', 4814, 0, 'gram'),
(4, 'mcg', 'µg', 'mass', .000001, 0, 'gram'),
(5, 'mcg DFE', 'µg', 'mass', .000001, 0, 'gram'),
(6, 'mcg RAE', 'µg', 'mass', .000001, 0, 'gram'),
(7, 'kilogram', 'kg', 'mass', 1000, 0, 'gram'),
(8, 'pound', 'lb', 'mass', 453.59237, 0, 'gram'),
(9, 'ounce', 'oz', 'mass', 28.3495, 0, 'gram')


