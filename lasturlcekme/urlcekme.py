from bing_image_urls import bing_image_urls

urler= bing_image_urls("mamut", limit=100)
dosya = open('lastss.txt', 'w')

for i in urler:
    print(i)
    dosya.write(i+"\n")

#print(urler)
#dosya.write(urler)
#dosya.close()