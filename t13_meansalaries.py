# calculate mean salary

weekly_salaries = [1000, 1100, 1200, 2100, 2500]
num_employees = [20, 8, 10, 7, 5]

# Calculate the sum of employees and store under "Total number of employees"
print("Total number of employees:", sum(num_employees))

# Calculate total salaries and store under "Total salary paid"
total_salaries = 0
for i in range(len(weekly_salaries)):
  total_salaries += weekly_salaries[i] * num_employees[i]
print("Total salary paid:", total_salaries)

# Calculate mean weekly salary
print("Mean weekly salary:", total_salaries / sum(num_employees))
