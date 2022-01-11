from bson.objectid import ObjectId
import pymongo
from staff import Staff
class Restaurant(Staff):
    def __init__(self) -> None:
        super().__init__()
        self._client=pymongo.MongoClient("mongodb://localhost:27017/")
        self._db=self._client["hotel"]
        self._food=self._db["Food"]
        self.name="Restaurant name"
    def menu(self):
        return {"Pizza":800,"Burger":600,"Pasta":900,"Sandwich":400}

    def viewAllOrders(self):
        print("\nAll Orders")
        # print("Order ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tFood\tServed")
        print("Time Stamp\t\t\tCustomer ID\t\t\tFood\tServed")
        for x in self._food.find():
            print(str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["food"]+"\t"+str(x["served"]))
            # print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["food"]+"\t"+str(x["served"]))

    def serveOrder(self,id):
        print("\n")
        try:
            self._food.update_one({"_id":ObjectId(id)},{"$set":{"served":True}})
            print("Order served")
            food=self._food.find_one({"_id":ObjectId(id)})
            price=self.menu()[food["food"]]
            self.updateBill(food["customer_id"],price)

        except Exception as e:
            print(e)


    def viewPendingOrders(self):
        print("\nPending Orders")
        # print("Order ID\t\t\tTime Stamp\t\t\tCustomer ID\t\t\tFood")
        print("Index\t\tTime Stamp\t\t\tCustomer ID\t\t\tFood")
        index=0
        po=list(self._food.find({"served":False}))
        if len(po)==0:
            print("No pending orders")
        else:
            for x in po:
                # print(str(x["_id"])+"\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["food"])
                print(str(index)+"\t\t"+str(x["timestamp"])+"\t"+x["customer_id"]+"\t"+x["food"])
                index+=1
        return po


