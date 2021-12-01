-- CREATE TABLE meals (
--     meals_id SERIAL PRIMARY KEY NOT NULL,
--     meals_name VARCHAR(50) NOT NULL,
--     meals_description VARCHAR(250) NOT NULL   
-- )
-- SELECT * from meals
-- INSERT INTO meals (
--     meals_id,
--     meals_name,
--     meals_description
-- )
-- VALUES (
--     DEFAULT,
--     "Sushi",
--     "Sushi rice 
--     a bamboo mat 
--     nori 
--     your choice of meat and vegetables
--     toasted sesame seeds and/or chia seeds
--     sriracha chili sauce
--     wasabi + pickled ginger"
-- )

SELECT * FROM meals  
ORDER BY RAND ( )  
LIMIT 1  