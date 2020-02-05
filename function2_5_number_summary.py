def five_number_summary(lists):

    lists.sort()

    minimum = round(min(lists),2)
    maximum = round(max(lists),2)
    mean = round(sum(lists)/len(lists),2)

    if len(lists) % 2 == 0: 

      p1 = int((len(lists)/2))
      p2 = int((len(lists)/2)-1)
      median = round((lists[p1] + lists[p2])/2,2)

      top_half = lists[:len(lists)//2]
      bottom_half = lists[len(lists)//2:]

      print(bottom_half)
      print(top_half)

      q1 = (top_half[len(top_half)//2] + top_half[(len(top_half)//2) -1])/2
      q3 = (bottom_half[len(bottom_half)//2] + bottom_half[(len(bottom_half)//2) -1 ])/2

    else:
      median = round(lists[len(lists)//2],2)
    
      top_half = lists[:len(lists)//2+1]
      bottom_half = lists[(len(lists)//2)+1:]
      
      if top_half % 2 == 0:
        q1 = round((top_half[len(lists)//2] + top_half[(len(lists)//2) - 1])/2,2)
        q3 = round((bottom_half[len(lists)//2] + bottom_half[(len(lists)//2)-1])/2,2)
        
      else:
        q1 = round(top_half[len(lists)//2],2)
        q3 = round(bottom_half[len(lists)//2],2)

    return {'max': maximum, 'q1': q1, 'median': median, 'q3': q3, 'min': minimum} 
