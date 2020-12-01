from bs4 import BeautifulSoup
import html
import html2text

with open("./scrapedbooks/books.txt", "r") as fin:
    l = fin.read().split("\n")
    

for i in l:
    try:
        with open("./scrapedbooks/" + i, "r") as fin:
            t = fin.read()
            with open("./scrapedbooks/" + i, "w+") as fout:
                fout.write(html2text.html2text(t))
    except:
        pass


    
        
        