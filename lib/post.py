
class Post():
    def __init__(self, id, title, content, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__