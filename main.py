#Inviting guests to the party 

name=input("Enter your name: ")
guests=int(input("\n How many Guests you want to invite to party: "))#Asking how many guests you want invite
total=0
if guests<=10: #if you inviting more the 10 guests print To many people
  for i in range(0,guests):
    n=int(input("\n Enter a number:= "))
    gname=input("\n Enter a guests name: ")    
    
    print("\n Dear", gname, "you are invited\n")
  total=total+n
  print("\n Total",total,"guests are invieted to the  party")#total how many guests you invited 
else: #if you are inviting less then 10 ask their name and print thier name you are inveted 
  print("\n Too many people")
  











