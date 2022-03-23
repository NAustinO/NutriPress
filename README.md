<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />

<h3 align="center">NutriPress</h3>

  <p align="center">
    NutriPress allows real-time, molecular-level nutritional data for any food, beverage or meal by understanding that all foods are built on a ratio-based formulation of commodity subingredients. 
    <br />
    <a href="https://github.com/NAustinO/NutriPress"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#demos">View Demo</a>
    ·
    <a href="https://github.com/NAustinO/NutriPress/issues">Report Bug</a>
    ·
    <a href="https://github.com/NAustinO/NutriPress/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#the-problem-with-laboratory-nutritional-analysis">The Problem</a></li>
        <li><a href="#the-problem-with-other-web-based-nutrition-calculators">The Disadvantages of Other Web-Based Nutrition Calculators</a></li>
        <li><a href="#the-nutripress-solution">The NutriPress Solution</a></li>
      </ul>
    </li>
    <li>
      <a href="#demos">Demos</a>
      <ul>
        <li><a href="#adding-custom-ingredient">Adding A Custom Ingredient</a></li>
        <li><a href="#adding-formula">Adding A Formula</a></li>
        <li><a href="#meal-planning">Meal Planning</a></li>
      </ul>
    </li>
    <li><a href="#database-model">Database Model</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `NutriPress`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [PyQt5](https://pypi.org/project/PyQt5/)
* [MySQL](https://www.mysql.com/)
* [MySQL Workbench](https://www.mysql.com/products/workbench/)
* [QtDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html)
* [PyMySQL](https://pypi.org/project/PyMySQL/)

<p align="right">(<a href="#top">back to top</a>)</p>



### The Problem With Laboratory Nutritional Analysis

* Currently, a laboratory analysis of a recipe at NutriData.com costs $900, which does not include the additional $250 to input the information into an FDA compliant nutrition label format. This can be very pricey for quick tweaks 
*  The turnaround time from receiving a lab sample can be 25 business days or more, interrupting workflows tremendously. 
* Often, the level of precision for a lab analysis is overkill, especially for restaurants who just want to display a rough calorie count on their menu or people who just want to get a good idea of how they are eating each day/meal


<p align="right">(<a href="#top">back to top</a>)</p>

### The Problem With Other Web-Based Nutrition Calculators


* Lack of modularity with custom foods items. If the ingredient you are looking to add is not in its database, you would need to use the next closest ingredient. With a database-centric software like Nutrition Assistant, a user can store specific food items, and use those food items in other food items seamlessly. This unlocks potential for using as a longer term nutrition planning application, since you can add a meal as a food item and get day, week or even month nutrition counts. 
* Lack of specificity. Nutrition usually measure their ingredient amounts in error-prone and sometimes density-dependent volume measurements, like cups, or relative terms like '1 medium-sized apple'. For a ballpark analysis, this would be adequate. However, the quantity of a medium-sized apple is ambiguous and lacks the specificity of what type of apple, each likely having a slightly different nutritional profile. Entering the nutritional profile of a specific apple into the Nutrition Assistant becomes a one-time time investment that pays itself in accurate reporting each time the ingredient is used. 

<p align="right">(<a href="#top">back to top</a>)</p>

### The NutriPress Solution

* Modularity. Each ingredient is inputted to build a formula, which builds up to make up a meal. 
* Specifity. Formulas calculations are insulated by inconsistencies because ingredients allow for tightly controllled and normalized nutritional information. 
* Version controls of recipes allows you to trace back to recipes to see what fails, or what was succcessful
* Simultaneous development and nutrition knowledge. For example, users can instantenously see the nutritional impact of substituting a heavy cream with a skim milk, while they are in the kitchen tasting it.


<p align="right">(<a href="#top">back to top</a>)</p>





<!-- GETTING STARTED -->
## Demos

Click the gifs below to see longer version demonstration videos.

### Adding Custom Ingredient

<b>Adding A Custom Ingredient</b>(Click Me)<br>
[![Alt text for your video](https://github.com/NAustinO/Nutrition-Assistant/blob/main/pjrd/static/media/Ingredient%20Demo.gif)](https://youtu.be/7RdvEvMmKS0)
<br><br><br>

### Adding Formula

<b>Adding A Formula</b>(Click Me)<br>
[![Alt text for your video](https://github.com/NAustinO/Nutrition-Assistant/blob/main/pjrd/static/media/Formula%20Demo.gif)](https://youtu.be/r32Fz2kW1Sw)

### Meal Planning
<b>Meal Planning (Eating In-N-Out for Every Meal)</b>(Click Me)<br>
[![Alt text for your video](https://github.com/NAustinO/Nutrition-Assistant/blob/main/pjrd/static/media/Meal%20Plan%20Demo.gif)](https://youtu.be/SckZJl_-Ysc)


<!-- USAGE EXAMPLES -->
## Database Model

![Database Schema Model](https://github.com/NAustinO/Nutrition-Assistant/blob/main/db/schema.png?raw=true)


<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<br>
<b>Possible Optimizations</b>
- Rather than manually inputting the nutrition information in, allow users to copy and paste into a text box and have a scanner read over the input and autofill.  
- Allow a cost/pricing model to be inputted to determine ingredient cost 
- Introduce function where user inputs their nutrition targets, and the program would recommend formulas to meet them
- TBD nutrition label generation


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nick Ozawa - nickaozawa@gmail.com

Project Link: [https://github.com/NAustinO/NutriPress](https://github.com/NAustinO/NutriPress)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Nutrionix](https://github.com/nutritionix/nutrition-label)
* [USDA Food and Nutrient Database for Dietary Studies](https://www.ars.usda.gov/ARSUserFiles/80400530/apps/FNDDS_2017-2018_ACCESS.EXE)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NAustinO/NutriPress.svg?style=for-the-badge
[contributors-url]: https://github.com/NAustinO/NutriPress/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/NAustinO/NutriPress.svg?style=for-the-badge
[forks-url]: https://github.com/NAustinO/NutriPress/network/members
[stars-shield]: https://img.shields.io/github/stars/NAustinO/NutriPress.svg?style=for-the-badge
[stars-url]: https://github.com/NAustinO/NutriPress/stargazers
[issues-shield]: https://img.shields.io/github/issues/NAustinO/NutriPress.svg?style=for-the-badge
[issues-url]: https://github.com/NAustinO/NutriPress/issues
[license-shield]: https://img.shields.io/github/license/NAustinO/NutriPress.svg?style=for-the-badge
[license-url]: https://github.com/NAustinO/NutriPress/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nick-ozawa/
[product-screenshot]: images/screenshot.png
