class Contact:
    def __init__(self, name:str, email:str, phone:str, linkedIn:str=None, github:str=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.linkedIn = linkedIn
        self.github = github