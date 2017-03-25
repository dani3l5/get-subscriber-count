import urllib.request

id = input("Channel ID: ")

url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + id + '&key=AIzaSyBU_oWEIULi3-n96vWKETYCMsldYDAlz2M'

data = urllib.request.urlopen(url).read().decode()

split_data = data.split('\n')

colon = 0

subs = ''

for line in split_data:
    if 'subscriberCount' in line:
        for char in line:
            if char == ":":
                colon = 1
            if colon == 1 and char != ':' and char != ' ' and char != '"' and char != ',':
                subs += char
            else:
                pass
    else:
        pass
print("Subscriber Count: " + subs)

