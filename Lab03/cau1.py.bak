
filename = input('nhap vao file muon luu: ')
new_filename = filename + '.bak'
backup = open(new_filename, 'w') #file de luu
#cach 1:
'''
try:
  file = open(filename) # phai ton tai truoc
  for line in  file:
    backup.write(line)
  backup.close()
  file.close()
  print("Closed?",file.closed)
except IOError:
  print ('File not found')

print ('Done')
#cach 2:
'''
try:
  with open(filename) as file:
    for line in file:
      backup.write(line)
    backup.close()
  print("Closed?",file.closed)
except IOError:
  print ('File not found')