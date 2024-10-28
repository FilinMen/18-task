input_data = open('input.txt','r')
data = input_data.read()
a = int(data)
b = 1
if a > 0:
    for i in range(1,a+1):
        b = b * i
else:
    b = 1
b = str(b)
output_data = open("ouyput.txt","w")
output_data.write(b)
input_data.close()
output_data.close()