#1068

while 0<1:
  try:
   
    count=0
    e=input()
    for i in e:

        
      if i == ')':
        count -= 1
        if count < 0:
          print('incorrect')
          break
        else:
          continue

      
        
      elif i == '(':
        count += 1
      
      
    if count > 0:
      print('incorrect')
    elif count < 0:
      continue 
    else:
      print('correct')   




  except EOFError:
    break
