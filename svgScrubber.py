
#!/usr/local/bin/python

import re
re.DOTALL

f = open('filesToScrub/index.html', 'r')

fileS = f.read()
svgs2 = re.split('</svg>.*?<svg version=', fileS, flags=re.DOTALL)

print len(svgs2)

n = 0 
for i in svgs2:
	i = '<svg version=' + i + '</svg>'
	writeFile = open('svgs/'+str(n)+'.svg','w+')
	writeFile.write(i)
	n+=1