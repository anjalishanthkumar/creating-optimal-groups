# program to generate nearest house for group study
import random
import math
import numpy as np
import pylab as pl

#plotting the points
pl.xlabel('x_axsis')
pl.ylabel('y_axsis')
pl.title('closest and far points')

pl.xlim(0, 80)
pl.ylim(0, 80)

count_re=0# var to stop recursion

#genrating cordinates
cor=[]
size=100 #num of cordinates
for i in range(size):
	cor.append( (random.randint(1,50) , random.randint(1,50)) )
"""size=15 #num of cordinates
cor=[(2,3),(2,5),(1,6),(1,9),(3,6),(5,5),(5,9),(7,6),(9,4),(13,3),(11,6),(9,9),(12,10),(10,12),(6,13)]
#cor=[(33,11,),(41,2),(29,39),(43,30),(19,20)]
"""
for x,y in cor:
	pl.plot(x, y, 'mo')
"""
#display cordinates
print"Cordinates are"
for x,y in cor:
	print "(",x,",",y,")"
"""

#genrating initial central points
#num_cp=3 #num of central points can read as input also
num_cp=int(input("enter num of groups/central points:"))


cp=[]
to=size-1
nu=random.sample(range(0,to),num_cp)# 0 and 'to' (i.e 14) are the array positions of cor
for i in nu:
	cp.append(cor[i])

#cp=[(2,3),(2,5),(11,6)]
"""
print"Initial central points are "
for x,y in cp:
	print "(",x,",",y,")"
"""
#row and col to generate two dimensioanl list
row=num_cp
col=size-num_cp

def central_points(g):
	#calculating new central points
	new_cp=[]
	for r in range(row):
		j=0
		sumx=0
		sumy=0
		for c in range(len(g[r])):
			sumx=sumx+g[r][c][j]
			sumy=sumy+g[r][c][j+1]
		if(len(g[r])):# when g[0] or g[1] etc has no cordinates(that cor does not becomes central point at all,one or more central points will be missing)
			sumx=sumx/len(g[r])
			sumy=sumy/len(g[r])
			new_cp.append((sumx,sumy))
	
	#print "new cp",new_cp
	return new_cp

def grouping(l2):
	dis=l2[0]
	vg=l2[1]
	g=[[] * col for i in range(row)]
		
	"""for r in range(row):
		for c in range(col): 
			print "(",r,",",c,")",vdis[r][c]"""

	#arranging groups(poping elements)
	for c in range(col):
		temp=[]
		for r in range(row):
			temp.append(dis[r][c])
		small=temp[0]
		pos=0
		i=0
 		#print temp
		for val in temp[1:len(temp)]:
			i=i+1
			if(small>=val):
				small=val
				pos=i
		#print small
		#print pos,",",c
		v=vg[pos][c]
		g[pos].insert(c,vg[pos][c])

	#display group elements
	"""
	for r in range(row):
		print "groups:"
		for c in range(col):
			print "(",r,",",c,")",g[r][c]
	"""
	return g
	

def dis_cal(new_cor):
	#distance calculating()
	
	dis = [[] * col for i in range(row)]
	vg=[[] * col for i in range(row)]
	#print len(dis[1])

	j=0
	for p in range(len(cp)):
		#print "x2 ...y2 are"
		for i in range(len(new_cor)):
			#print "(",cp[p][j],",",cp[p][j+1],")","and","(",new_cor[i][j],",",new_cor[i][j+1],")"
			#print "(x1,y1)","=","(",cp[p][j],",",cp[p][j+1],")"
			#print "(x2,y2)","=","(",new_cor[i][j],",",new_cor[i][j+1],")"
			m=math.sqrt( math.pow((new_cor[i][j]-cp[p][j]),2) + math.pow((new_cor[i][j+1]-cp[p][j+1]),2) )
			dis[p].insert(i,m)
			vg[p].insert(i,new_cor[i])
	

	
	return [dis,vg]

#just getting the cor for distance cal		
def getting():  
	#getting cordinates to perform dis cal
	#print "next"
	new_cor=[]
	for x2,y2 in cor:
		none=1 # not a central can peform dis cal
		for x1,y1 in cp:
			if((x1!=x2) or (y1!=y2)):
				none=1
				#print "not same"
			else:
				none=0
				#print "(",x1,",",y1,")","and","(",x2,",",y2,")"
				break
		if(none):
			#print "cordintes for dis cal"
			#print "(",x1,",",y1,")","and","(",x2,",",y2,")"
			new_cor.append((x2,y2))	
	return new_cor

#redoing calculation again
def final_cp(new_cp,g,count_re):
	#print count_re
	if(count_re==100):
		print " we get a:( RuntimeError: maximum recursion depth exceeded)"
		print "pervious central points and groups are:"
		for i in range(len(cp)):
			print "central points are:",cp[i]
			print "group",i+1,":"
			print g[i]
		k=0
		x=[]
		y=[]
		for i in range(len(cp)):
				#print "x=",cp[i][k],"y=",cp[i][k+1]
				x.append(cp[i][k])
				y.append(cp[i][k+1])
				pl.plot(cp[i][k],cp[i][k+1],'rD')
				for j in range(len(g[i])):
					#print "x=",g[i][j][k],"y=",g[i][j][k+1]
					x.append(g[i][j][k])
					y.append(g[i][j][k+1])
				#plotting line
				pl.plot(x,y,'g')
				x=[]
				y=[]
		pl.show()				
		exit(1)
	redo=0
	if(len(new_cp)==len(cp)):
		for i in range(len(new_cp)):
			if(cp[i]!=new_cp[i]):
				redo=1
				break
		if(redo):
			#print "call loops again"
			new_cor=getting()
       			l2=dis_cal(new_cor)
			g=grouping(l2)
			new_cp=central_points(g)
   			count_re=count_re+1
 			final_cp(new_cp,g,count_re)
		else:
			print "Final central points and groups are:"
			for i in range(len(new_cp)):
				print "central points are:",new_cp[i]
				print "group",i+1,":"
				print g[i]
			k=0
			x=[]
			y=[]
			for i in range(len(new_cp)):
				#print "x=",new_cp[i][k],"y=",new_cp[i][k+1]
				x.append(new_cp[i][k])
				y.append(new_cp[i][k+1])
				pl.plot(cp[i][k],cp[i][k+1],'ks')
				for j in range(len(g[i])):
					#print "x=",g[i][j][k],"y=",g[i][j][k+1]
					x.append(g[i][j][k])
					y.append(g[i][j][k+1])
				#plotting line
				pl.plot(x,y,'b')
				x=[]
				y=[]
 			pl.show()	
			
	else:
		#print "call loops again with random cp generation"
		for k in range(num_cp-1):
			del cp[k]
		del cp[0]
		num=random.sample(range(0,14),num_cp)
		for i in num:
			cp.append(cor[i])
		new_cor=getting()
       		l2=dis_cal(new_cor)
		g=grouping(l2)
		new_cp=central_points(g)
   		count_re=count_re+1
 		final_cp(new_cp,g,count_re)


def main():
	global cp
	new_cor=getting()
        l2=dis_cal(new_cor)
	g=grouping(l2)
	new_cp=central_points(g)
 	final_cp(new_cp,g,count_re)
	#print cp
	#print new_cp
	
main()








		
		


