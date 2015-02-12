import numpy as np
from huffman_tools import *

f = 111111555533366644772828838399497489160274976217496371694271089273612974891629747961289739612893798614791927654981269831297397129837

#f  = lambda a,b: int(100*(a[1]-b[1]))

p = np.random.random(10)*np.arange(10)+0.01
p = p/sum(p)
q = p
#p = sorted([(str(x[0]), x[1]) for x in enumerate(p)], f)
p = sorted(f)

code = { x[0]: '' for x in p}

for k in range(10-1):
    for x in p[0][0]:
        code[x] += '0'
    for x in p[1][0]:
        code[x] += '1'

    p = sorted(p[2:] + [(p[0][0]+p[1][0], p[0][1]+p[1][1])],f)

print q
print code

for i in list(f):
	print (code[i]),