import requests
try:
    res = requests.get("https://www.tuoitre1.vn/")
    print (res.status_code) #doc file, ket noi trang web,...
    
except requests.exceptions.ConnectionError:
    print ("loi ket noi")
except IOError:
    print ("loi doc file")
finally:
    print ('done')
