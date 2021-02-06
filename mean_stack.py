import numpy as np

def read_data(csv_filename):
  data = np.loadtxt(csv_filename, delimiter=',')
  return data
def mean_datasets(datasets):
  np_dataset = []
  mean_dataset = []
  for dataset in datasets:
    if len(mean_dataset) == 0:
      mean_dataset = np.array(read_data(dataset))
    else:
      data = np.array(read_data(dataset))
      for i, row in enumerate(data):
        mean_dataset[i] = data[i] + mean_dataset[i]
  mean_dataset = mean_dataset / len(datasets)    
  return mean_dataset
      
      
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
