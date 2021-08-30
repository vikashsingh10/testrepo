link="https://books.toscrape.com/catalogue/category/books_1/page-{}.html"
tit=[]
store=[]
for x in range(1,51):
    print(x)  
    r=link.format(x)
    res=requests.get(r)
    soup=bs4.BeautifulSoup(res.text,"lxml")
    images=soup.select(".thumbnail")
    print(len(images))
    for y in images:
        title=y["alt"]
        image=y["src"]
        a="https://books.toscrape.com/"
        b=str(image)[9:]
        c=a+b
        print("writing : " + title)
      
print("Completed")
