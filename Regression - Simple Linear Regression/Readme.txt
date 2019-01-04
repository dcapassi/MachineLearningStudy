This example loads the “Salary_Data” dataset which contains the columns “YearsExperience” (independent variable) and “Salary” (dependant variable).

The goal is to verify if there is correlation between the years of experience and the employee salaries, one quick way to achieve it is using Linear Regression to identify the line which cross the points with more accuracy as possible.

The Python and R of Linear Regression are used, but the same result could be manually calculated using the following equations:

Line Equation: y = ma+b
r = sum(  ( x - avg(x) ) ( y - avg(y) ) ) / sqrt ( sum (x-avg(x)^2 * sum (y-avg(y)^2  )
b = r * (std deviation(y) / std deviation(x))
x = avg(y) - b * avg(x)

