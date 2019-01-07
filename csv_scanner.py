import os
import sys
import csv

found=False
count=0;
target_list=['TARGET_STRING_LIST']
for filename in os.listdir("SRC_DST"):
 src="SRC_DST"+filename
 if src!='SPECIAL_CASES':
  with open(src, 'rt') as f:
   reader = csv.reader(f, delimiter=',') 
   for row in reader:
    for field in row:
     for target in target_list:
      if target == field:
       found=True
  if found==True:
   print(src)
   print('Found')
   count=count+1;
  else:
   print(src)
   print('Not Found')
  found=False
print(' ')
print('Done!')
if count==0:
 print('No problem with all')
else:
 print(count,' with problem(s)')
input()


