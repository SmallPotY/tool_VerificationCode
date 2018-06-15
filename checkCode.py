# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:48:08 2018

@author: SmallPot
"""

from PIL import Image
import requests
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def code(codeurl):
    
    valcode = requests.get(codeurl)
    
    f = open('checkCode.jpg', 'wb')
    # 将response的二进制内容写入到文件中
    f.write(valcode.content)
    # 关闭文件流对象.
    f.close()
    
    im = Image.open('checkCode.jpg')
    text = pytesseract.image_to_string(im)
    return text

