import requests

name = '699991.txt'
address = 'https://stepic.org/media/attachments/course67/3.6.3/'

name = requests.get(url=(address+name)).text
while name[:2] != 'We':
    name = requests.get(url=(address+name)).text
    print(name)

with open("output_3.6.3.txt", "w") as file:
    file.writelines(name)
