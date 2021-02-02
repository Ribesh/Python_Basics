users = {"Ribesh" : 7 , "Samyam": 8 , "Sunila" : 9 , "Gajendra" : 10 }
passwords = {}                                    # Created a new dictionary to store password
         
for username,length in users.items():         # same thing as above but define in loop
        #print(username)
        password = []
        for i in range(0, length):
            password.append(random.choice(string.ascii_letters))
        passwords[username]= "".join(password)          # mapping the key and values to new dictionary
     
              
print(users)
print(passwords)