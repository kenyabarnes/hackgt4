'''
Created on Sep 22, 2017

@author: josh
'''


   
Top=17
Bottom=2
res=0
temp=True
hold=1
while(temp):
    #print res
    if(Top-Bottom>=0):
        Top=Top-Bottom
        res=res+hold
        if(Top==0):
            break
    else:
        hold=hold*.1
        Top=Top*10

print res
        