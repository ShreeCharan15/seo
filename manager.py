from bson.objectid import ObjectId
import pymongo
class Manager:
    def __init__(self) -> None:
        self._client=pymongo.MongoClient("mongodb://localhost:27017/")
        self._db=self._client["hotel"]
        self._bookings=self._db["Bookings"]
        self._customers=self._db["Customers"]
        self._staff=self._db["Staff"]
        self._food=self._db["Food"]
        self._services=self._db["Services"]
        self.mid=None
        self.name="Manager"

    def listBookings(self):
        bookings=list(self._bookings.find())
        index=0
        print("\nBookings")
        print("Index\t\tCustomer ID\t\t\tDate\t\t\tRoom no")
        for booking in bookings:
            print(str(index)+"\t\t"+booking["customer_id"]+"\t\t"+str(booking["date"])+"\t"+(str(booking["room"]) if booking["room"]!=None else "Not Confirmed"))
            index+=1
        return bookings
    def acceptBooking(self,id,roomNo):
        self._bookings.update_one({"_id":ObjectId(id)},{"$set":{"room":roomNo}})
        print("Room Accepted")
    def rejectBooking(self,id):
        self._bookings.delete_one({"_id":ObjectId(id)})
        print("Room Rejected")
    def listCustomers(self):
        customers=list(self._customers.find())
        print("\nCustomers")
        print("Index\t\tName\t\t\tEmail\t\t\tPhone")
        index=0
        for customer in customers:
            print(str(index)+"\t\t"+customer["name"]+"\t\t\t"+customer["email"]+"\t\t"+str(customer["phone"]))
            index+=1
        return customers
    def listStaff(self):
        staff=list(self._staff.find())
        print("\nStaff")
        print("Index\t\tName\t\tEmail\t\t\tPhone\t\t\tType\t\t\tTasks")
        index=0
        for s in staff:
            print(str(index)+"\t\t"+s["name"]+"\t\t"+s["email"]+"\t"+str(s["phone"])+"\t\t"+str(s["type"])+"\t\t"+str(s["tasks"]))
            index+=1
        return staff
    
    def allotTask(self,id,task):
        self._staff.update_one({"_id":ObjectId(id)},{"$push":{"tasks":task}})
        print("Task Allotted")

    # def addStaff(self,name,email,phone):
    #     self._staff.insert({"name":name,"email":email,"phone":phone,"tasks":[],"password":"sa"})
    #     print("Staff Added")

    

