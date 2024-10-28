inputdata = open('input.txt','r')
data = inputdata.read()
a = int(data)
b = 1
for i in range(1,a+1):
    b = b * i
b = str(b)
outputdata = open("ouyput.txt","w")
outputdata.write(b)
inputdata.close()
outputdata.close()