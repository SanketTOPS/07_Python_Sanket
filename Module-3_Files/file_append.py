fl=open("hello.txt","a")

id=input("Enter ID:")
name=input("Enter Name:")
city=input("Enter City:")

fl.write(f"Student ID:{id}\nStudent Name:{name}\nStudent City:{city}\n")