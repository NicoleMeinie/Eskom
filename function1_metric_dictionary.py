def metric_dictionary(lists):

  """ This function takes in a list of integers and returns a dictionary of the mean, median, variance, standard deviation, min and max.
      Answers are rounded to the second decimal 
  """
  lists.sort()

  minimum = round(min(lists),2)
  maximum = round(max(lists),2)
  mean = round(sum(lists)/len(lists),2)

  numerator_list = [(item - mean)**2 for item in lists]
  numerator = sum(numerator_list)
  variance = round(numerator/(len(lists) - 1),2)

  standard_deviation = round(variance**(1/2),2)

  if len(lists) % 2 == 0: 
    p1 = int((len(lists)/2))
    p2 = int((len(lists)/2)-1)
    median = round((lists[p1] + lists[p2])/2,2)

  else:
    median = round(lists[len(lists)//2],2)

  return {'min': minimum, 'max': maximum, 'mean': mean, 'median': median, 'std': standard_deviation, 'var': variance} 
