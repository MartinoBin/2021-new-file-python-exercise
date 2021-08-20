import requests

res=requests.get('http://automatetheboringstuff.com/files/rj.txt')
type(res)

res.status_code==requests.codes.ok
len(res.text)
print(res.text[:250])
