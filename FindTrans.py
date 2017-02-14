import os
import glob
import fnmatch, os
import ast
fid=open('../spkList/final/spkAllFinal','r')
line=fid.readline()
# # NWI=open('../term1to799/nodeWithInterval.dat','r')
# # node=NWI.readline()
# # NLD=open('../term1to799/nodelist1DocTo799Doc.dat','r')
# # node1=NLD.readline()
# # fId=open('../nodeWithTrans.dat','a')
# i=1
# trans1=""
# trans2=""
TranId=open('../Trans/AllTrans','w')


while(line):
	lines=line.split('_')
	ll=lines[1].split('\n')
	print(ll[0])
	print(lines[0])
	if((ll[0]=='03' or ll[0]=='03') and (lines[0]=='263' or lines[0]=='189')):
		print('Not available')
	else:	
		trans=open('../../Hindi/'+ll[0]+'/txt/'+lines[0]+'.txt','r')
		text=trans.readline()
		TranId.write(text)
	line=fid.readline()






# while(line):
	
# 	lines=line.split()
# 	# nodes=node.split()
# 	# nodes1=node1.split()
# 	# #print i
# 	print nodes[0]
# 	# print lines[0]
# 	# print nodes[3]
# 	# print lines[3]
# 	lines1=lines[0].split("_")
# 	lines2=lines[3].split("_")
# 	#filePath='home/lokendra/Documents/Hindi_db'+lines1
# 	if(i!=51):
# 		Tid1=open('/home/lokendra/Documents/Hindi_db/'+lines1[1]+'/wrd/'+lines1[0]+'.wrd','r')
# 		Tid2=open('/home/lokendra/Documents/Hindi_db/'+lines2[1]+'/wrd/'+lines2[0]+'.wrd','r')
# 		wrd1=Tid1.readline()
# 		while(Tid1.readline()):

# 			#wrd2=Tid2.readline()
# 			wrds1=wrd1.split()
# 			#wrds2=wrd2.split()
# 			#flag=1
# 			while((int(lines[1])<=int(wrds1[0])) or (int(lines[2])>=int(wrds1[1])) ):

# 				if((int(lines[1])<= int(wrds1[0])) and (int(lines[2])>= int(wrds1[1]))):
# 					trans1=trans1+wrds1[2]

# 			wrd1=Tid1.readline()
# 		wrd2=Tid2.readline()
# 		while(Tid2.readline()):

# 			#wrd2=Tid2.readline()
# 			wrds2=wrd2.split()
# 			#wrds2=wrd2.split()
# 			#flag=1
# 			while((int(lines[4])<=int(wrds2[0])) or (int(lines[5])>=int(wrds2[1])) ):

# 				if((int(lines[4])<= int(wrds2[0])) and (int(lines[5])>= int(wrds2[1]))):
# 					trans2=trans2+wrds2[2]

# 			wrd1=Tid1.readline()
# 		fId.write(trans1)



				
				

		

# 		print Tid.readline()
# 	i=i+1
# 	line=fid.readline()


# #for filename in glob.glob('/home/lokendra/Documents/Hindi_db/**/**/*.wrd'):
# #			print(filename)
# 			#f=open(filename,'r')
# 			#print f.readline()
# 			#f1=open('someinfo','a')
# 			#f1.write(f.read())