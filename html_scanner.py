import os
import sys
import shutil
from bs4 import BeautifulSoup
countok=0
countpass=0
for filename in os.listdir("SOURCE_DST"):
 dst="OUTPUT_DST"+filename
 src="SOURCE_DST"+filename
 htmlfile = open(src, 'r', encoding='utf-8')
 htmlhandle=htmlfile.read()
 if htmlhandle.find('TAGET_STRING')!=-1:
  print('Now dealing:')
  print(src)
  shutil.copyfile(src, dst)
  countok=countok+1
 else:
  print('No problem: ')
  print(src)
  countpass=countpass+1
 htmlfile.close()
print('Files with problems:')
print(countok)
print('Files without problems:')
print(countpass)
print('Total files dealed')
print(countok+countpass)
input()
