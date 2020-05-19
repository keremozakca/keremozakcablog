from random import random
import time

# deneme = 0
# numbercreate = int(random()*100)
# while True:
#   inputnumber = int(input("0 ile 100 arasında bir sayı tahmin et : "))
#   if inputnumber == numbercreate:
#     print(f"Doğru tahmin ettiniz : {numbercreate} .\nTebrikler\n Deneme Sayınız : {deneme}")
#     break
#   elif inputnumber < numbercreate:
#     print("Yukarı Çık")
#     deneme += 1
#     continue
#   elif inputnumber > numbercreate:
#     print("Aşağı in")
#     deneme += 1
#     continue
bosluk=" "

while True:   
  
  bosluk += " "
  
  time.sleep(0.1)
  print(f"{bosluk}KEREM")
  if len(bosluk) == 100:
    break

