# Create basic plots using Matplotlib

import matplotlib.pyplot as plt

# Line plot
years = [2010, 2011, 2012, 2013, 2014]
sales = [100, 150, 200, 250, 300]
plt.plot(years, sales, label='Sales Trend', color='blue', marker='o')
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Bar Chart
categories = ["electronics", "clothing", "groceries", "furniture"]
revenue = [5000, 3000, 4000, 2000]
plt.bar(categories, revenue, color=['red', 'green', 'blue', 'orange'])
plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.show()

# Scatter Plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 60, 70, 80, 90]
plt.scatter(hours_studied, exam_scores, color='purple')
plt.title('Exam Scores vs Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.show()