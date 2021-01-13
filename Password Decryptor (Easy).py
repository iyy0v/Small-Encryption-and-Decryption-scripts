
password = input("Enter the encrypted password here : ")

pwd_in_list = []

pwd_decrypted = ""

i = 0
for char in password:
    pwd_in_list.append("")
    pwd_in_list[i] = pwd_in_list[i] + chr( 33 + (126 - ord(char)) )
    pwd_decrypted = pwd_decrypted + pwd_in_list[i]
    i+=1

print(pwd_decrypted)