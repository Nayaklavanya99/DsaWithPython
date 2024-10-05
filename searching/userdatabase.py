class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email= email

    def introduce_yourself(self,guest_name):
        print("Hi {}, I'm {}! Contact me at {}".format(guest_name,self.name,self.email))

    def __repr__(self):
        return "User(username='{}', name='{}',email='{}')".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self,user):
        i=0
        while i<len(self.users):
            if self.users[i].username > user.username:
                break
            i+=1
        self.users.insert(i,user)
    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self,user):
        target = self.find(user.username)
        target.name,target.email = user.name, user.email
    def list_all(self):
        return self.users

jane =User("Jane", "janedoe", "1ajanedoe@gmail.com")   
john = User("John", "johndoe", "johndoe@gmail.com")
alice =  User("Alice", "alice123", "alice@example.com")


database = UserDatabase()
database.insert(jane)
database.insert(john)
database.insert(alice)


user = database.find('Alice')
print(user)

database.update(User(username='Alice', name='Alicuu',email='alice@example.com'))
print(database.find('Alice'))

print(database.list_all())