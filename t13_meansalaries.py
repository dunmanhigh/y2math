# calculate mean salary

weekly_salaries = [1000, 1100, 1200, 2100, 2500]

num_employees = [20, 8, 10, 7, 5]
print("Total number of employees:", sum(num_employees))

total_salaries = 0
for i in range(len(weekly_salaries)):
  total_salaries += weekly_salaries[i] * num_employees[i]
print("Total salary paid:", total_salaries)

print("Mean weekly salary:", total_salaries / sum(num_employees))

# calculate mean salary

weekly_salaries = [2000, 2500, 3000, 3500, 4000]

num_employees = [10, 20, 30, 40, 50]
print("Total number of employees:", sum(num_employees))

total_salaries = 0
for i in range(len(weekly_salaries)):
  total_salaries += weekly_salaries[i] * num_employees[i]
print("Total salary paid:", total_salaries)

print("Mean weekly salary:", total_salaries / sum(num_employees))

