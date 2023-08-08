import json
class Storage:
    users = []
    fileName = 'authentication.txt'

    def add(self, obj):
        Storage.users.append(obj)
        self.save()


    def find(self, obj):
        for user in Storage.users:
            if user['email'] == obj['email']:
                return user

    def save(self):
        file = open(Storage.fileName, 'w')
        json.dump(Storage.users, file)
        file.close()
        

    def reload(self):
        file = open(Storage.fileName , 'r')
        Storage.users = json.load(file)
        file.close()
