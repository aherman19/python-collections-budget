import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

spending_categories = []

#Populate spending category list from the expenses list
for expense in expenses.list:
    spending_categories.append(expense.category)

#Count which categories had the most purchases
spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

categories,count = zip(*top5)

fig, ax = plt.subplots()
ax.bar(categories,count)
ax.set_title('# of Purchases by Category')
plt.show()