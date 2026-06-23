class User:
    

    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        print("new user being created ....")

    def follow(self, user):
        user.followers = +1
        self.following = +1

user_1 = User("001","Angela")

#print(user_1.id)


user_2 = User("002", "Jack")

# user_3 = User()  ## NO jalaria por que pedimos dos cosas a la hora de crear un objeto desde la class

