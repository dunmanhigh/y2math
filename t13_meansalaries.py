# calculate mean salary

weekly_salaries = [1000, 1100, 1200, 2100, 2500]

num_employees = [20, 8, 10, 7, 5]
print("Total number of employees:", sum(num_employees))

total_salaries = 0
for i in range(len(weekly_salaries)):
  total_salaries += weekly_salaries[i] * num_employees[i]
print("Total salary paid:", total_salaries)

print("Mean weekly salary:", total_salaries / sum(num_employees))

amount paid weekly= (1000*20)+(1100*8)+(1200*10)+(2100*7)+(2500*5)
total amount= 68000

Mean weekly salary= total amount/total employees
Mean weekly salary= 68000/50= 1360
