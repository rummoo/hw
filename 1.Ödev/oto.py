import random
import names
f=open("list1.txt","w")
for i in range(1,41):
	f.write(' %r                   %r                   %r                   %r\n' % (i,names.get_full_name(),random.randint(1,100),random.randint(1,100)))
f.close()

with open('list1.txt', 'r') as f:
    lines = f.readlines()


lines = [line.replace(" '", ' ') for line in lines]
lines = [line.replace("' ", ' ') for line in lines]

with open('list1.txt', 'w') as f:
    f.writelines(lines)
