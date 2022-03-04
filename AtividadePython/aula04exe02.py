produto = float(input('Digite o valor do produto'))
Pag = str(input('qual a forma de pagamento?'))
if Pag=='debito': 
   print ('o valor do produto é' ,produto-produto*0.10)
elif Pag=='cred':
   print('o valor do produto é',produto-produto*0.05 )
elif Pag=='credx':
      print('o valor do produto é ',produto)
elif Pag=='credy':
     print('o valor do produot é',produto+produto*0.10)
else: 
    print('')