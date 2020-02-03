def five_number_summary(lists):

"""This function takes in a list of integers and returns a dictionary of the five number summary. 
   Answers are rounded to the nearest second decimal.
"""   
  lists.sort()

  minimum = round(min(lists),2)
  maximum = round(max(lists),2)
  mean = round(sum(lists)/len(lists),2)

  if len(lists) % 2 == 0: 

    p1 = int((len(lists)/2))
    p2 = int((len(lists)/2)-1)
    median = round((lists[p1] + lists[p2])/2,2)

    q1 = round((lists[(len(lists)+1)//4] + lists[(len(lists)+1)//4 + 1])/2,2)

    q3 = round((lists[3*(len(lists)+1)//4] + lists[(3*(len(lists)+1)//4)) + 1])/2,2)

   else:
     
    median = round(lists[len(lists)//2],2)

    q1 = 


    return {'max': maximum, 'q2': q2, 'median': median, 'q3': q3, 'min': minumum} 
