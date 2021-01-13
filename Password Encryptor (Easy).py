
password = input("Enter password here : ")

pwd_in_list = []

pwd_encrypted = ""

i = 0
for char in password:
    pwd_in_list.append("")
    pwd_in_list[i] = pwd_in_list[i] + chr( 126 - (ord(char) - 33) )
    pwd_encrypted = pwd_encrypted + pwd_in_list[i]
    i+=1

print("Your encrypted password is : " + pwd_encrypted)