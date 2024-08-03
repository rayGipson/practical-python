# pcost.py
#
# Exercise 1.27

import sys 

def portfolio_cost(filename):
  total_cost = 0.0

  if len(sys.argv) == 2:
     filename = sys.argv[1]
  else:
     filename = '/Users/ray/Documents/machine_learning_engineer/practical-python/practical-python/work/Data/portfolio.csv'

  with open(filename, 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price
  print('Total cost', total_cost)

cost = portfolio_cost('filename')