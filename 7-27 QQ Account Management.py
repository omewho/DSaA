n = int(input())
    
accpw = dict()
for i in range(n):
    aString = input()
    aList = aString.split()
    #print(aList)
    temp_account = aList[1]
    temp_pw = aList[2]
    
    if aList[0] is 'L':
        #print(aList[0])
        
        if temp_account in accpw.keys() and accpw[temp_account] == temp_pw:
            print("Log in Successful")
        elif temp_account not in accpw.keys():
            print("ERROR: Account Not Exist")
        elif temp_account in accpw.keys() and accpw[temp_account] != temp_pw:
            print("ERROR: Wrong Password")
    elif aList[0] is 'R':
       if temp_account not in accpw.keys():
          accpw[temp_account] = temp_pw
          print("Register Successful")
       else:
           print("ERROR: Account Number Already Exists")
