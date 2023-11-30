from lib.user_repository import UserRepository
from lib.user import User

'''
I can retrieve a list of all users
'''
def test_return_all_users(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = UserRepository(db_connection)
    users = repo.all()
    assert users == [
        User(1, 'mikeyP', 'mike_p@gmail.com'),
        User(2, 'melC', 'melmel@gmail.com'),
        User(3, 'melB', 'sporty@gmail.com'),
        User(4, 'viccy', 'posh_v@gmail.com')
    ]

'''
I can retrieve user info by searching with user_id
'''
def test_search_user_by_id(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = UserRepository(db_connection)
    user = repo.find(2)
    assert user == User(2, 'melC', 'melmel@gmail.com')

'''
Using repo.add
I can add a new user to the database
'''
def test_add_new_user(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = UserRepository(db_connection)
    repo.add('jb01', 'joe_j@jonas.com')
    users = repo.all()
    assert users == [
        User(1, 'mikeyP', 'mike_p@gmail.com'),
        User(2, 'melC', 'melmel@gmail.com'),
        User(3, 'melB', 'sporty@gmail.com'),
        User(4, 'viccy', 'posh_v@gmail.com'),
        User(5, 'jb01', 'joe_j@jonas.com')
    ]

'''
Given I have a user id
I can use repo.remove to delete the user from the database
'''
def test_remove_user_by_id(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = UserRepository(db_connection)
    repo.remove(3)
    users = repo.all()
    assert users == [
        User(1, 'mikeyP', 'mike_p@gmail.com'),
        User(2, 'melC', 'melmel@gmail.com'),
        User(4, 'viccy', 'posh_v@gmail.com')
    ]