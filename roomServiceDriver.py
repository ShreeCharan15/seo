from roomService import RoomService
rs=RoomService()
choice=0
while choice!=-1:
    print("\nEnter -1 at any stage to exit")
    print("1. View Tasks")
    print("2. Finish Task")
    print("3. View Room Service Requests")
    print("4. Fulfil Room Service Requests")
    choice=int(input())
    if choice==-1:
        break
    elif choice==1:
        rs.viewTasks()
    elif choice==2:
        rs.finishTask()
    elif choice==3:
        rs.viewRequests()
    elif choice==4:
        po=rs.viewRequests()
        if len(po)==0:
            print("Nothing to flfil")
        else:
            while True:
                print("Enter the index of the request you want to fulfil")
                index=int(input())
                if index==-1:
                    break
                elif index>=len(po):
                    print("Please enter a valid index")
                    continue
                else:
                    rs.fulfillRequest(po[index]["_id"])
                    break
    else:
        print("Please enter a valid choice")