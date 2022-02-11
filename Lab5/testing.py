import matplotlib.pyplot as pyplot
pyplot.bar([1, 4, 7], [10, 20, 30], color = 'blue')
pyplot.bar([2, 5, 8], [20, 30, 40], color = 'red')
pyplot.xticks([1, 4, 7], ['CS 177', 'CS 180', 'CS 190'])
pyplot.title('A Bar Chart with X-ticks')
pyplot.xlabel('x-axis label')
pyplot.ylabel('y-axis label')
pyplot.show()
