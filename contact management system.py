contacts={ }
while True:
    print("\n contact management system")
    print("1.Add Contact") 
    print("2.Search Contact") 
    print("3.Update Contact") 
    print("4.Delete Contact") 
    print("5.Display Contacts") 
    print("6.Exit") 
    choice=int(input("Enter Choice : ")) 
    if choice==1:
        name=input("enter name: ")
        phone=int(input("enter phone: "))
        contacts[name]=phone
        print("contact added successfully")
    elif choice==2:
        name=input("enter name: ")
        if name in contacts:
            print("phone :",contacts[name])
        else:
            print("contact not found")
    elif choice==3:
        name=input("enter name: ")
        if name in contacts:
            phone=int(input("enter new phone: "))
            contacts[name]=phone
            print("update successfully")
    elif choice==4:
        name=input("enter name: ")
        if name in contacts:
            del contacts[name]
            print("delete contact")
        else:
            print("contact not found")
    elif choice==5:
         print("\n contacts list")
         for name,phone in contacts.items():
             print(name,"\t",phone)
    elif choice==6:
        print("thankyou")
        break
    else:
        print("invalid choice")
            
            
    
            
    
