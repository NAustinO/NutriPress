SELECT food_nutrient.nutrient_id, nutrient.nutrient_name, SUM(food_nutrient.nutrient_weight_g_per_100g)
FROM food
LEFT JOIN food_nutrient ON food_nutrient.food_id = food.food_id
LEFT JOIN nutrient ON nutrient.nutrient_id = food_nutrient.nutrient_id
WHERE food.food_id = 11100000
AND nutrient.nutrient_id IN (203, 204, 205, 208, 291, 269, 659)
GROUP BY nutrient_id


