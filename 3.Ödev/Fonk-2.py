from math import exp
import numpy as np
df=open('output.txt','w')
for i in np.arange(0,100,0.01):
    y = (i*i)*((exp(i)-exp(-i))/2)
    df.write('        %r        %r\n' % (i,y))
df.close()
