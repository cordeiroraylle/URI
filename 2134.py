pin = list(input().split())
entrada = list(input().split())

cont = 0
i = 0

while cont <len(pin):
  if(pin[cont] == entrada[cont]):
    break
  else:
    i+=1
    cont+=1

if (i == 5):
   print("Y")
else:
   print("N")
