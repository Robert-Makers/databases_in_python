from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = [User(row['id'], row['username'], row['email']) for row in rows]
        return users
    
    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        return User(rows[0]['id'], rows[0]['username'], rows[0]['email'])
    
    def add(self, username, email):
        self._connection.execute(
            'INSERT INTO users (username, email) VALUES (%s, %s)',
            [username, email]
        )

    def remove(self, id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s',
            [id]
        )