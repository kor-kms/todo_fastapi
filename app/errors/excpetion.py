class UserIdNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "User id not found")


class NotAuthenticated(Exception):
    def __init__(self, *args):
        super().__init__(*args, "User pw wrong")
