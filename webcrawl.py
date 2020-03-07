import bs4
'''it is used to fetch the page's html code'''
import urllib.request as url
''' it is used to send the request and get the response'''

path = 'https://www.amazon.in/dp/B07DJD1RTM?pf_rd_r=5AEEXNXMJNKYYBX0BT3N&pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e'

httpresponse = url.urlopen(path)

pagedata = bs4.BeautifulSoup(httpresponse,'lxml')
'''lxml -library xml- parser library''' 

itemName = pagedata.find('span',id='productTitle')
itemName = itemName.text
itemName = itemName.strip(' \n')
'''itemName = itemName.replace('\n','')
itemName = itemName.replace('  ','')
'''

print('item name',itemName)
div = pagedata.find('div',id='feature-bullets')
spanlist = div.findAll('span', class_ = 'a-list-item')
c = 1
for i in spanlist:
    i = i.text
    i = i.strip(' \n\t ')
    print(c,'. ',i)
    c+=1
