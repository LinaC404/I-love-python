import requests
import os

def getHTMLTest(url):
    try:
        kv = {"q":"python"}
        r = requests.get(url,params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.request.url)
        print(len(r.text))
        return r.text
    except:
        # r.encoding = r.apparent_encoding
        print(r.status_code)
        return "HTTPError"

# if __name__ == "__main__":
#     url = "https://oldherbaceous.files.wordpress.com/2018/04/le-petit-prince-and-the-rose.jpg"
#     root = "C:\\Users\\Lina Chen\\Desktop\\"
#     path = root + url.split('/')[-1]
#     print(path)
#     try:
#         if not os.path.exists(root):
#             os.mkdir(root)
#         if not os.path.exists(path):
#             r = requests.get(url)
#             with open(path,'wb') as f:
#                 f.write(r.content)
#                 f.close()
#                 print("The image has been downloaded!")
#         else:
#             print("Already existed!")
#     except:
#         print("Error")

if __name__ == "__main__":
    kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    url = "https://whatismyipaddress.com/ip/126.36.145.175"
    r = requests.get(url,headers=kv)
    print(r.request.url)
    print(r.request.headers)
    print(r.status_code)
    print(r.text[-5000:])


