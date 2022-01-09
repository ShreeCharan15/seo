from bson.objectid import ObjectId
from staff import Staff
class RoomService(Staff):
    def __init__(self, id=None) -> None:
        super().__init__(id=id)
        self._services=self._db["Services"]
    def viewRequests(self):
        reqs=list(self._services.find({"service":"Room Service","fulfilled":False}))
        print("\nRoom Service Requests")
        print("Index\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tService")
        index=0
        for x in reqs:
            print(str(index)+")\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["service"])
            index+=1
        return reqs


    def fulfillRequest(self,id):
        print("\n")
        try:
            self._services.update_one({"_id":ObjectId(id)},{"$set":{"fulfilled":True}})
            print("Request Fulfilled")
        except Exception as e:
            print(e)

