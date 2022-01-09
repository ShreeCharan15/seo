from bson.objectid import ObjectId
import pymongo
class Staff:
    def __init__(self,id=None) -> None:
        self._client=pymongo.MongoClient("mongodb://localhost:27017/")
        self._db=self._client["hotel"]
        self._staff=self._db["Staff"]
        if(id==None):
            self.login()
        else:
            user=self._staff.find_one({"_id":ObjectId(id)})
            self.name=user["name"]
            self.email=user["email"]
            self.phone=user["phone"]
            self.sid=str(user["_id"])
            self.tasks=user["tasks"]
        
    def login(self):
        print("\n")
        while True:
            print("Please enter email id")
            # email=input()
            email="staffa@gmail.com"
            user=self._staff.find_one({"email":email})
            if(user==None):
                print("No suck _staff member found")
                break
            else:
                print("Please enter your password")
                # password=input()
                password="sa"
                if(password==user["password"]):
                    print("Login Successful")
                    self.name=user["name"]
                    self.email=user["email"]
                    self.phone=user["phone"]
                    self.sid=str(user["_id"])
                    self.tasks=user["tasks"]
                    break
                else:
                    print("Login Failed")

    def viewTasks(self):
        print("\nTasks")
        for task in self.tasks:
            print(task)
    def allotTask(self,task):
        self._staff.update_one({"_id":ObjectId(self.sid)},{"$push":{"tasks":task}})
        self.tasks.append(task)
        print("Task Alloted")

    def finishTask(self):
        if(len(self.tasks)>0):
            print(self.tasks)
            while True:
                print("Enter index of finished task: ")
                index=int(input())
                if index==-1:
                    break
                if index>=len(self.tasks):
                    print("Invalid index")
                    continue
                else:
                    self._staff.update_one({"_id":ObjectId(self.sid)},{"$pull":{"tasks":self.tasks[index]}})
                    self.tasks.pop(index)
                    break
        else:
            print("No tasks to finish")
