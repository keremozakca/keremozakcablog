cumle = input("Bir cümle girin :  ")
unluler = "aeıiouüAEUÜIİOÖ"
unsuzler = "bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"
sayi2 = 0
istenmeyenler = ""
sayi = 0
for karakter in cumle:
  if karakter in unluler:
    sayi = sayi + 1
  elif karakter in unsuzler:
    sayi2 = sayi2 + 1  
  
print(f"Cümledeki ünlü sayısı (hece sayısı) : {sayi} \n",f"Cümledeki ünsüz sayısı : {sayi2} ")    
