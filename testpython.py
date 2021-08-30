#I am creating my first python code which will claw data from website 
|------|
#First we need to import some required libraries 
import requests
import bs4
#Our main code here 
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
        # print(c)
        # url=c
        # print(url)
        # print(title)
     
        '''with open(title.replace("/","-") + ".jpg","wb") as f:
          im=requests.get(c)
          f.write(im.content)'''
        print("writing : " + title)
        store.append(c)
# store
print("Completed")
