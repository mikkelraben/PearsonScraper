import requests
import time

payload={}
headers = {
  'Host': 'plus.pearson.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'DNT': '1',
  'Connection': 'keep-alive',
  'Cookie': 'INSERT_COOKIE_HERE',
  'Upgrade-Insecure-Requests': '1',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-GPC': '1',
  'TE': 'trailers'
}



# get all pages between 1 and 1000
for i in range(2,1308):
    url = "https://plus.pearson.com/eplayer/pdfassets/prod1/174015/1623868b-9693-402b-8788-588975d88e11/pages/page{}?password=&accessToken=null&formMode=true".format(i)
    
    response = requests.request("GET", url, headers=headers, data=payload)

    output = "./output/page{}.png".format(i)

    #output the response as a file
    f = open(output, "wb")
    f.write(response.content)
    f.close()
    time.sleep(1)





