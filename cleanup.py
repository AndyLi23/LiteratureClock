from bs4 import BeautifulSoup
import html
import html2text

if __name__ == '__main__':

    with open("./scrapedbooks/books.txt", "r") as fin:
        l = fin.read().split("\n")
        
        
    good = []

    for i in l:
        print("Cleaning " + i)
        try:
            with open("./scrapedbooks/" + i, "r") as fin:
                t = fin.read()
                with open("./scrapedbooks/" + i, "w+") as fout:
                    fout.write(html2text.html2text(t))
                good.append(i)
        except:
            pass

    with open("./scrapedbooks/books.txt", "w+") as fout:
        fout.write("\n".join(good))
    
        
        