#ex.2714   
n = int(input())
for i in range(n):
  RA = input()
  if RA[:2] == "RA":
    if len(RA)>=20:
      passw = RA[2:]
      print(int(passw))
    else:
      print("INVALID DATA")
  else:
    print("INVALID DATA")
