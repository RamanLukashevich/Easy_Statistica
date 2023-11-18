<img align="right" src=icons/easy_statistica.ico width=80px>

# Easy Statistica

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Easy Statistica is an application for statistical analysis that implements the functions of data analysis, data management, data mining, data visualization using statistical methods. The application is built in Python using the PySide6/Qt toolkit. It uses the Pandas DataFrame class to work with data. For graphics, the application uses the Matplotlib library to visualize data in 2D graphics.

<img align="center" src=examples/screen_1.png width=600px>

You can download your data file in Excel or CSV format or copy the desired data columns from the file into a data table. The application provides the ability to use Ctrl+C and Ctrl+V to copy data from tables into the application table for analysis.

<img align="center" src=examples/screen_2.2.png width=600px>

Analysis tools include 5 sections.

Section "Basic Statistics": assessing the distribution of your data in terms of the normal distribution using several tests, including graphical methods. Also in this section you can set the confidence interval you need to evaluate the data.

<img align="center" src=examples/screen_2.5.png width=600px>
<img align="center" src=examples/screen_2.4.png width=600px>

Section "Statistical criteria": a set of parametric and nonparametric tests to test hypotheses in your data, allowing you to determine whether any observed effect is statistically significant or due to chance.

<img align="center" src=examples/screen_6.png width=600px>

Section "Correlation and Regression": assessing the statistical relationship of variables and the inferred relationships between the dependent variable and independent variables in your data. Several methods are presented to assess the statistical relationship of variables. Linear and logistic (ROC curve) regressions are presented to evaluate the relationships between variables.

<img align="center" src=examples/screen_7.png width=600px>
<img align="center" src=examples/screen_8.png width=600px>

Section "Sample size selection": assessment of the required number of observations for inclusion in the statistical sample based on the sampling error or vice versa.

<img align="center" src=examples/screen_9.png width=600px>

Section "Coefficients": calculation of critical values for the chi-square, Student's (T-test) and Gaussian (Z-test) tests. Calculation based on Poisson distribution.

<img align="center" src=examples/screen_2.6.png width=600px>

Section "Settings": configure the data output for replacing empty cells in data, the number of significant digits.

<img align="center" src=examples/screen_2.7.png width=600px>

section “FAQ”: provides information about the methods and criteria implemented in the analysis tools.

<img align="center" src=examples/screen_2.8.png width=600px>

Section “Reports”: implemented saving your data worksheet (before and after performing the analysis) in the required format, saving analysis results in PDF format, saving graphs and graphs in JPG format.

<img align="center" src=examples/screen_2.9.png width=600px>


### Python libraries used:
* pandas v2.1.3, 
* matplotlib v3.8.1, 
* scipy v1.11.3, 
* sklearn v1.3.2, 
* numpy v1.26.2, 
* statsmodels v0.14.0, 
* openyxl v3.1.2 


## Windows

A Windows standalone binary can be downloaded in [Google drive](https://drive.google.com/drive/folders/19DgtpvFLSrlNvipfKdj9_pGqnq2AWJQG?usp=sharing).


