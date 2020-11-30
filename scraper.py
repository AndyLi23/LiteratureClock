from aiohttp import ClientSession
import requests
from bs4 import BeautifulSoup
import asyncio
import time

async def get1(i, session):
    t1 = time.time()
    r = await session.get("http://www.gutenberg.org/ebooks/bookshelf/13?start_index=" + str(i * 25 + 1))
    
    soup = BeautifulSoup(await r.text(), features="html.parser")
    for j in soup.find_all(attrs={"class": "link"}, href=True):
        try:
            if(j.find(attrs={"class": "title"}).get_text().split(" ")[0] != "Sort"):
                books[j.find(attrs={"class": "title"}).get_text()+"?by:"+j.find(attrs={"class": "subtitle"}).get_text()] = j['href'].split("/")[-1]
        except:
            pass
            
    print(str(i) + ": " + str(int(time.time()-t1)) + "s")


async def get(k, v, session):
    t1 = time.time()
    url = "http://www.gutenberg.org/files/" + v + "/" + v + "-h/"  + v + "-h.htm"
    r = await session.request(method='GET', url=url)
    
    with open("./scrapedbooks/" + k, "w+") as fin:
        fin.write(await r.text())
        
    print(k + ": " + str(int(time.time()-t1)) + "s")
        
        
async def main1():
    async with ClientSession() as session:
        await asyncio.gather(*[get1(i, session) for i in range(1)])
            
async def main():
    async with ClientSession() as session:
        await asyncio.gather(*[get(k, v, session) for k,v in books.items()])

if __name__ == "__main__":
    print("Collecting books...")
    books = {}
    
    asyncio.run(main1())
    
    with open("./scrapedbooks/books.txt", "w+") as fin:
        fin.write("\n".join(books.keys()))

    print(str(len(books.keys())) + " books collected")
    
    print("Parsing books...")
    asyncio.run(main())
    print(str(len(books.keys())) + " books parsed")

