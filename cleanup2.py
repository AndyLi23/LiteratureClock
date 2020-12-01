with open("./scrapedbooks/books.txt", "r") as fin:
        l = fin.read().split("\n")
        
        
for i in l:
    print("Cleaning " + i)
    with open("./scrapedbooks/" + i, "r") as fin:
        t = fin.read()
        while "  " in t:
            t.replace("  ", " ")
            
        while "**" in t:
            t.replace("**", "")
            
        while "#" in t:
            t.replace("#", "")
            
        with open("./scrapedbooks/" + i, "w+") as fout:
            fout.write(t)
