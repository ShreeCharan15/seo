from clubhouse import ClubHouse
ch=ClubHouse()
choice=0
while choice!=-1:
    print("\nEnter -1 at any stage to exit")
    print("1. View Pending Orders")
    print("2. Serve Order")
    print("3. View All Orders")
    choice=int(input())
    if choice==-1:
        break
    elif choice==1:
        ch.viewPendingRequests()
    elif choice==2:
        po=ch.viewPendingRequests()
        if len(po)==0:
            print("Nothing to serve")
        else:
            while True:
                print("Enter the index of the order you want to serve")
                index=int(input())
                if index==-1:
                    break
                elif index>=len(po):
                    print("Please enter a valid index")
                    continue
                else:
                    ch.fulfilRequest(po[index]["_id"])
                    break
    elif choice==3:
        ch.viewAllRequests()
    else:
        print("Please enter a valid choice")