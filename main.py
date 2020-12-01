import timetostring

with open("./scrapedbooks/books.txt", "r") as fin:
    l = fin.read().split("\n")
    

for i in l:
    with open("./scrapedbooks/" + i, "r") as fin:
        t1 = fin.read()
        t = t1.lower()
        for j in timetostring.timetostring(3, True):
            if t.find(j) != -1:
                temp = t.find(j)
                ts = t1.split(" ")
                
                a = -1
                ind = 0
                
                for k in ts:
                    a += 1 + len(k)
                    if(a > temp):
                        break
                    ind += 1
                    
                print(ts[ind])



    