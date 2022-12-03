class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user = User(name="Ahsan", age=22)
user2 = User(name="Ali", age=22)

user.follow(user2)

print(user.followers)
print(user.following)
print(user2.followers)
print(user2.following)
