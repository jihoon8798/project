
# coding: utf-8

# In[6]:


import os
import numpy as np
import codecs
Stable1=[]
Stable2=[]
Stable3=[]
Wtable1=[]
Wtable2=[]
Wtable3=[]
arrS1='C:/Users/SDP/SDP/HJ/acceldata/Sdata5/Hyeong/'
arrS2='C:/Users/SDP/SDP/HJ/acceldata/Sdata5/Min/'
arrS3='C:/Users/SDP/SDP/HJ/acceldata/Sdata5/Heng/'
arrW1='C:/Users/SDP/SDP/HJ/acceldata/Wdata5/Hyeong/'
arrW2='C:/Users/SDP/SDP/HJ/acceldata/Wdata5/Min/'
arrW3='C:/Users/SDP/SDP/HJ/acceldata/Wdata5/Heng/'
for i in range (9937):#9937 
    file_name = arrS1+str(i).zfill(5)+'.txt'
    file_name2= arrW1+str(i).zfill(5)+'.txt'
    fS = open(file_name,'r',-1,encoding = 'UTF8')
    fL = open(file_name2,'r',-1,encoding ='UTF8')
    line = fS.read()
    line2= fL.read()
    Slist=[]
    Wlist=[]
    Slist= line.split('\n')
    Wlist= line2.split('\n')
    del Slist[len(Slist)-1]#마지막 두개 제거
    del Slist[len(Slist)-1]
    del Wlist[len(Wlist)-1]
    del Wlist[len(Wlist)-1]
    
    
    Stable1.append(Slist)
    Wtable1.append(Wlist)
    fS.close()
    fL.close()
for i in range (26228):#26228 
    file_name = arrS2+str(i).zfill(5)+'.txt'
    file_name2= arrW2+str(i).zfill(5)+'.txt'
    fS = open(file_name,'r',-1,encoding = 'UTF8')
    fL = open(file_name2,'r',-1,encoding ='UTF8')
    line = fS.read()
    line2= fL.read()
    Slist=[]
    Wlist=[]
    Slist= line.split('\n')
    Wlist= line2.split('\n')
    del Slist[len(Slist)-1]#마지막 두개 제거
    del Slist[len(Slist)-1]
    del Wlist[len(Wlist)-1]
    del Wlist[len(Wlist)-1]
    
    Stable2.append(Slist)
    Wtable2.append(Wlist)
    fS.close()
    fL.close()
for i in range (13706):#13706
    file_name = arrS3+str(i).zfill(5)+'.txt'
    file_name2= arrW3+str(i).zfill(5)+'.txt'
    fS = open(file_name,'r',-1,encoding = 'UTF8')
    fL = open(file_name2,'r',-1,encoding ='UTF8')
    line = fS.read()
    line2= fL.read()
    Slist=[]
    Wlist=[]
    Slist= line.split('\n')
    Wlist= line2.split('\n')
    del Slist[len(Slist)-1]#마지막 두개 제거
    del Slist[len(Slist)-1]
    del Wlist[len(Wlist)-1]
    del Wlist[len(Wlist)-1]
    
    Stable3.append(Slist)
    Wtable3.append(Wlist)
    fS.close()
    fL.close() 


# In[7]:


TopWordHy=[]
TopWordMin=[]
TopWordHe=[]
for i in range(9937):#9937
    TW=[0]*10 #top word
    TS=[0]*10 #top similar
    if( i == 9807):
        continue; # 잘못패치되는 경우 에러
    for j in range(len(Stable1[i])):#한 문장 단어개수 10개 추리기
        if( Stable1[i][j]< '1'):
            for k in range(10):#소팅시키는작업 
                if(str(TS[k])<Stable1[i][j]):#만약 더 큰숫자가 나타난다면
                    for l in range(10 - k):# 맨뒤부터 차례대로 앞숫자 댕겨와서
                        if(k<9):
                            TW[9-l]= TW[8-l]
                            TS[9-l]= TS[8-l]#순서대로 워드 밀어주는 방법
                    TW[k]=Wtable1[i][j]
                    TS[k]=Stable1[i][j]
                    break;#한번 걸리면 바로 브레이크걸어준다 
    #print(TW)
    TopWordHy.append(TW)# 다추리면 10* len으로  리스트화
    
for i in range(26228):#26228
    if ( i == 10597):
        continue;
    elif(i == 17361):
        continue;
    TW=[0]*10 #top word
    TS=[0]*10 #top similar
    for j in range(len(Stable2[i])):
        if( Stable2[i][j]< '1'):
            for k in range(10):
                if(str(TS[k])<Stable2[i][j]):
                    for l in range(10 - k):
                        if(k<9):
                            TW[9-l]= TW[8-l]
                            TS[9-l]= TS[8-l] 
                    TW[k]=Wtable2[i][j]
                    TS[k]=Stable2[i][j]
                    break;
    TopWordMin.append(TW)
for i in range(13706):#13706
    if(i== 10686):
        continue;
    elif(i== 12937):
        continue;    
    TW=[0]*10 #top word
    TS=[0]*10 #top similar
    for j in range(len(Stable3[i])):
        if( Stable3[i][j]< '1'):
            for k in range(10):
                if(str(TS[k])<Stable3[i][j]):
                    for l in range(10 - k):
                        if(k<9):
                            TW[9-l]= TW[8-l]
                            TS[9-l]= TS[8-l] 
                    TW[k]=Wtable3[i][j]
                    TS[k]=Stable3[i][j]
                    break;
    TopWordHe.append(TW)


# In[8]:


print("잘못패치 형사")
for i in range(9936):
    for j in range(10):
        if(TopWordHy[i][j]== 0):
            print(i)
print("잘못패치 민사")
for i in range(26226):
    for j in range(10):
        if(TopWordMin[i][j]== 0):
            print(i)
print("잘못패치 행정")
for i in range(13704):
    for j in range(10):
        if(TopWordHe[i][j]== 0):
            print(i)


# In[9]:


ar1='C:/Users/SDP/SDP/HJ/CNN/Top10Data/TopWord_1.20_0.80/Hyeong/'
ar2='C:/Users/SDP/SDP/HJ/CNN/Top10Data/TopWord_1.20_0.80/Min/'
ar3='C:/Users/SDP/SDP/HJ/CNN/Top10Data/TopWord_1.20_0.80/Heng/'
i=0
print("형사")
for i in range (9936):#9936
    filename= ar1+str(i).zfill(5)+'.txt'
    output = open(filename,'w',-1,encoding = 'UTF8')
    for j in range(len(TopWordHy[i])):
        output.write(TopWordHy[i][j]+'\n')#output file에다 저장
    output.close()
print("민사")
for i in range (26226):#26226
    filename= ar2+str(i).zfill(5)+'.txt'
    output = open(filename,'w',-1,encoding = 'UTF8')
    for j in range(len(TopWordMin[i])):        
        output.write(TopWordMin[i][j]+'\n')
    output.close()
print("행정")
for i in range (13704):#13704
    filename= ar3+str(i).zfill(5)+'.txt'
    output = open(filename,'w',-1,encoding = 'UTF8')   
    for j in range(len(TopWordHe[i])):        
        output.write(TopWordHe[i][j]+'\n')
    output.close()


# In[1]:


print(len(text))

