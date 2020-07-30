# lossless compression : according to pattern of object
# lossy compression:  used in audio, image where change or compress doesn't have big apperance

import gzip

text = " lossless compression : according to pattern of objec  lossy compression:  used in audio image where change or compress doesnt have big apperance lossless compression :according to pattern of objec  lossy compression:  used in audio, image where change or compress doesn"
with gzip.open('./comp.txt', 'rb') as f:
    #f.write(text.encode('utf-8'))
    print(f.read())
