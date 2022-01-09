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
        bookings=self._bookings.find()
        for booking in bookings:
            print(booking["name"]+" "+booking["email"]+" "+str(booking["phone"])+" "+booking["date"]+" "+(booking["room"] if booking["room"]!=None else "Not Confirmed"))
        return bookings
    def acceptBooking(self,id,roomNo):
        self._bookings.update_one({"_id":ObjectId(id)},{"$set":{"room":roomNo}})
        print("Room Accepted")
    def rejectBooking(self,id):
        self._bookings.delete_one({"_id":ObjectId(id)})
        print("Room Rejected")
    def listCustomers(self):
        customers=self._customers.find()
        for customer in customers:
            print(customer["name"]+" "+customer["email"]+" "+str(customer["phone"]))
        return customers
    def viewStaff(self):
        staff=self._staff.find()
        for s in staff:
            print(s["name"]+" "+s["email"]+" "+str(s["phone"]))
        return staff
    
    def allotTask(self,id,task):
        self._staff.update_one({"_id":ObjectId(id)},{"$push":{"task":task}})
        print("Task Allotted")

    # def addStaff(self,name,email,phone):
    #     self._staff.insert({"name":name,"email":email,"phone":phone,"tasks":[],"password":"sa"})
    #     print("Staff Added")

    

