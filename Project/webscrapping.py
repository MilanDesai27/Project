
def main()
from bs4 import BeautifulSoup
from urllib.request import*

website=input("Enter website:")
response=urlopen(website)
html=response.read()

soup=BeautifulSoup(html,"html.parser")

return(website)




