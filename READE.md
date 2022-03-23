# Nutrition Assistant
PURPOSE 
<h3>Background</h3>
-  This program seeks to replicate the nutritional and database aspects of ESHA Genesis R&D software. Genesis R&D is a food formulation & labeling software that is used widely among consumer food product manufacturers, restaurants, dietitians, and other nutrition conscious professionals. At its core, Genesis R&D's functionality includes enabling users to create Nutrition Facts panels, virtually formulate foods, analyze the nutrition content of recipes, and adjust ingredeints over without sending samples of the recipe to a lab on each change. At the current time, the Nutrition Assistnat is not able ot generate a formatted Nutrition Facts Panel. 

<h4>The problem with laboratory nutrition analysis</h4>

- Currently, a laboratory analysis of a recipe at NutriData.com costs $900, which does not include the additional $250 to input the information into an FDA compliant nutrition label format. This can be very pricey for quick tweaks 
- The turnaround time from receiving a lab sample can be 25 business days or more, interrupting workflows tremendously. 
- Often, the level of precision for a lab analysis is overkill, especially for restaurants who just want to display a rough calorie count on their menu or people who just want to get a good idea of how they are eating each day/meal

<b>There are many web-based nutrition calculators that work, but they have a few fundamental disadvantages: </b>
- Lack of modularity with custom foods items. If the ingredient you are looking to add is not in its database, you would need to use the next closest ingredient. With a database-centric software like Nutrition Assistant, a user can store specific food items, and use those food items in other food items seamlessly. This unlocks potential for using as a longer term nutrition planning application, since you can add a meal as a food item and get day, week or even month nutrition counts. 
- Lack of specificity. Nutrition usually measure their ingredient amounts in error-prone and sometimes density-dependent volume measurements, like cups, or relative terms like '1 medium-sized apple'. For a ballpark analysis, this would be adequate. However, the quantity of a medium-sized apple is ambiguous and lacks the specificity of what type of apple, each likely having a slightly different nutritional profile. Entering the nutritional profile of a specific apple into the Nutrition Assistant becomes a one-time time investment that pays itself in accurate reporting each time the ingredient is used. 

<b>Advantages of a nutrition software like the Nutrition Assistant </b>
- Version controls of recipes allows you to trace back to recipes to see what fails, or what was succcessful
- Simultaneous development and nutrition knowledge. For example, users can instantenously see the nutritional impact of substituting a heavy cream with a skim milk, while they are in the kitchen tasting it.
- Modular 

<b>Possible Optimizations</b>
- Rather than manually inputting the nutrition information in, allow users to copy and paste into a text box and have a scanner read over the input and autofill.  
- Allow a cost/pricing model to be inputted to determine ingredient cost 
- Introduce function where user inputs their nutrition targets, and the program would recommend formulas to meet them
- TBD nutrition label generation


DEMOS
<br>
Click the gifs below to see a demonstration video. 
<br><br><br>
<b>Adding A Custom Ingredient</b>(Click Me)<br>
[![Alt text for your video](https://github.com/NAustinO/Nutrition-Assistant/blob/main/pjrd/static/media/Ingredient%20Demo.gif)](https://youtu.be/7RdvEvMmKS0)
<br><br><br>
<b>Adding A Formula</b>(Click Me)<br>
[![Alt text for your video](https://github.com/NAustinO/Nutrition-Assistant/blob/main/pjrd/static/media/Formula%20Demo.gif)](https://youtu.be/r32Fz2kW1Sw)
<br><br><br>
<b>Meal Planning (Eating In-N-Out for every Meal)</b>(Click Me)<br>
[![Alt text for your video](https://github.com/NAustinO/Nutrition-Assistant/blob/main/pjrd/static/media/Meal%20Plan%20Demo.gif)](https://youtu.be/SckZJl_-Ysc)



FRAMEWORKS/TOOLS
- PYSIDE/QT
- QT Designer for UI development
- PyMySQL for SQL client 
- MySQL Workbench


SCHEMA
![Database Schema Model](https://github.com/NAustinO/Nutrition-Assistant/blob/main/db/schema.png?raw=true)


RESOURCE ACKNOWLEDGEMENTS
- Nutrition Label jQuery Plugin courtesy of Nutrionix 
Copyright (c) 2010-2017 Nutritionix, LLC. http://www.nutritionix.com
https://github.com/nutritionix/nutrition-label
- Preloaded ingredient data taken from the USDA Food and Nutrient Database for Dietary Studies (FNDDS)
U.S. Department of Agriculture, Agricultural Research Service. 2020. USDA Food and Nutrient Database for Dietary Studies 2017-2018. Food Surveys Research Group Home Page, http://www.ars.usda.gov/nea/bhnrc/fsrg
https://www.ars.usda.gov/ARSUserFiles/80400530/apps/FNDDS_2017-2018_ACCESS.EXE

