import numpy as np

def calculate(list):
#check if list has correct number of digits
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  else:
  
#convert list into multidimensional arrays
    size = 3 #elements per row
    chunks = [list[i:i+3] 
              for i in range(0, len(list), size)] # divide list into smaller lists of 3
    matrix = np.array(chunks).reshape(3,3) #make a 3x3 array

    #column-wise computations
    mean_column = []
    var_column = []
    sd_column = []
    max_column = []
    min_column = []
    sum_column =[]

    for c in range(matrix.shape[1]):
      mean_column.append(matrix[:, c].mean())
      var_column.append(matrix[:, c].var())
      sd_column.append(matrix[:, c].std())
      max_column.append(matrix[:, c].max())
      min_column.append(matrix[:, c].min())
      sum_column.append(matrix[:, c].sum())

    #row-wise computations
    mean_row = []
    var_row = []
    sd_row = []
    max_row = []
    min_row = []
    sum_row =[]
  
    for r in range(0,3):
      mean_row.append(matrix[r].mean())
      var_row.append(matrix[r].var())
      sd_row.append(matrix[r].std())
      max_row.append(matrix[r].max())
      min_row.append(matrix[r].min())
      sum_row.append(matrix[r].sum())

    #flattened computations
    mean_flat = matrix.mean()
    var_flat = matrix.var()
    sd_flat = matrix.std()
    max_flat = matrix.max()
    min_flat = matrix.min()
    sum_flat = matrix.sum()

    #compiling into a dictionary
    mean = [mean_column, mean_row, mean_flat]
    variance = [var_column, var_row, var_flat]
    standard_deviation = [sd_column, sd_row, sd_flat]
    max = [max_column, max_row, max_flat]
    min = [min_column, min_row, min_flat]
    sum = [sum_column, sum_row, sum_flat]

    results = {
      "mean" : mean,
      "variance": variance,
      "standard deviation": standard_deviation,
      "max": max,
      "min": min,
      "sum": sum
    }

  return results