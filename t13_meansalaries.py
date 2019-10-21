# calculate mean salary
weekly_salaries = [1000, 1100, 1200, 2100, 2500]
num_employees = [20, 8, 10, 7, 5]

# Calculate the number of employees and display it as "Total number of employees"
print("Total number of employees:", sum(num_employees))

# Calculate the total amount of salary
total_salaries = 0
for i in range(len(weekly_salaries)):
  total_salaries += weekly_salaries[i] * num_employees[i]

# Display total salaries under "Total salary paid"
print("Total salary paid:", total_salaries)

# Calculate mean weekly salary based on values found in previous equations
print("Mean weekly salary:", total_salaries / sum(num_employees))
