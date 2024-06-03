"""
Program: Lab1.1
Author: Ifa Namee
Date: 9/1/2023
purpose: Wage calculater program.
"""
# Define variables
usual_time = 40
overtime = 10
wage = 15.34
overtime_wage = 23.01  # 15.34 * 1.5

# Display the total wage
print('Your gross pay is $', (usual_time * wage)
      + (overtime * overtime_wage), '.')
