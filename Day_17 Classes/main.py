class User:
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0 # this is a default value that is not being passed in when the class is initialized
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Jordan")
user_2 = User("002", "Emilee")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
