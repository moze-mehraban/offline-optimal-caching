from sys import flags


slut=int(input())
data=list(map(int,input().split()))
cache=[]
for i in range( len(data)):
    #print(cache )
    if data[i] not in [ j[0] for j in cache]:
        if len(cache)<slut:
            cache.append((data[i],i))
        else:
            l1=[]
            for k in cache:
                if k[0] not in data[i:]:
                    l1.append(k)
            if len(l1)>0:
                l1=sorted(l1,key=lambda tup: tup[1])
                tmp=cache.pop(cache.index(l1[0]));
                print(tmp[0],end=" ")
                cache.append((data[i],i))
            else:
                l2=[]
                for k in cache:
                    l2.append((k[0],data[i:].index(k[0])))
                l2=sorted(l2,key=lambda tup: tup[1],reverse=True)
                
                tmp=cache.pop([y[0] for y in cache].index(l2[0][0]));
                print(tmp[0],end=" ")
                cache.append((data[i],i))
