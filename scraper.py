from aiohttp import ClientSession
import requests
from bs4 import BeautifulSoup
import asyncio
import time


async def get(k, v, session):
    t1 = time.time()
    url = "http://www.gutenberg.org/files/" + v + "/" + v + "-h/"  + v + "-h.htm"
    r = await session.request(method='GET', url=url)
    with open("./scrapedbooks/" + k + ".txt", "w+") as fin:
       fin.write(str(r.content))
    print(k + ": " + str(time.time()-t1))
        
            
async def main():
    async with ClientSession() as session:
        await asyncio.gather(*[get(k, v, session) for k,v in books.items()])

if __name__ == "__main__":
    books = {}
    soup = BeautifulSoup(requests.get("http://www.gutenberg.org/ebooks/bookshelf/13?start_index=1").content, features="html.parser")
    for j in soup.find_all(attrs={"class": "link"}, href=True):
        if(j.find(attrs={"class": "title"}).get_text().split(" ")[0] != "Sort"):
            books[j.find(attrs={"class": "title"}).get_text()+"?by:"+j.find(attrs={"class": "subtitle"}).get_text()] = j['href'].split("/")[-1]

    with open("./scrapedbooks/books.txt", "w+") as fin:
        fin.write("\n".join(books.keys()))

    print("books collected")
        
    asyncio.run(main())
