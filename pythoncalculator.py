
dongu = 0
print ("HESAP MAKİNESİNE \n HOŞ GELDİNİZ")
print ("YAPILABİLECEK İŞLEMLER\n","TOPLAMA : + \n","ÇIKARMA : - \n","ÇARPMA : * \n","BÖLME : / \n","ÜS ALMA : ** (1.sayı Taban 2.sayı kuvvettir) \n","BÖLÜMÜNDEN KALAN ALMA : # \n","Aritmetik Ortalama Alma : ? \n","Hesap makinesi kapatma : ! \n")
while (dongu <= 20):
 sayi1 = input("1.Sayıyı Girin : ")
 sayi2 = input("2.Sayıyı Girin : ")
 islem = str(input("Yapılacak İşlemi Girin : "))
 if islem == "+":
   print ("Sonuç : ",int(sayi1)+int(sayi2))
   dongu = dongu + 1
   continue
 elif islem == "-":
   print ("Sonuç : ",int(sayi1)-int(sayi2))
   dongu = dongu + 1
   continue
 elif islem == "*":
   print ("Sonuç : ",int(sayi1)*int(sayi2))
   dongu = dongu + 1
   continue
 elif islem == "/":
   print ("Sonuç : ",int(sayi1)/int(sayi2))
   dongu = dongu + 1
   continue
 elif islem == "**":
   print ("Sonuç : ",int(sayi1) ** int(sayi2))
   dongu = dongu + 1
   continue
 elif islem == "#":
   print ("Sonuç : ",int(sayi1) % int(sayi2)) 
   dongu = dongu + 1
   continue    
 elif islem == "?":
   print ("Sonuç : ",(int(sayi1)+int(sayi2))/2)
   dongu = dongu + 1
   continue
 elif islem == "!":
   print("Toplandı. Sonuç : ",int(sayi1)+int(sayi2),"\n")
   print("Hesap makinesi kapatıldı. Görüşmek üzere ...")
   break
 elif sayi1==":" and sayi2==")" and islem=="++":
   print("Toplandı. Sonuç : :)   . Her zaman gülümseme toplayın . Gülümsemeyi yüzünüzden hiç eksik etmeyin.")  
 else:
   print("Lütfen geçerli bir işlem giriniz")  
   dongu = dongu + 1
   continue
