

class User:
    def __init__(self, user):
        self.username = user.username
        self.first = user.first
        self._id = user.id
        self.email = user.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

    def get_username(self):
        return self.username

    def get_first_name(self):
        return self.first_name


