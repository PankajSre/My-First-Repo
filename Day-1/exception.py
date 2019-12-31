
try:
   fh = open('test.txt','a')

   data = input('Enter your Details : ')
   fh.write(data)
   for line in fh:
       print(line)
   myData = fh.readline()
except:
    print('Check your File Name')
    
finally:
    print('This will execute always!!!')
    fh.close()


