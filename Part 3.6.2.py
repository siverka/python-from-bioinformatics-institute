import requests

address = 'https://stepic.org/media/attachments/course67/3.6.2/335.txt'
address = address.strip()
response = requests.get(url=address)
lines = response.text.splitlines()
print(len(lines))
