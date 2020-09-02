import socket as s

url = input("What is the website's URL ? : ")

print(f'IP address of {url} is {s.gethostbyname(url)}')
