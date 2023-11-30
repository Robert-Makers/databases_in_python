from lib.user import User

'''
user constructs with email and username parameters
'''
def test_user_construct():
    user = User(1, 'myuser', 'myemail@email.com')
    assert user.id == 1
    assert user.username == 'myuser'
    assert user.email == 'myemail@email.com'

'''
Given a user
I can return a formatted string of user details
'''
def test_format_post():
    user = User(1, 'myuser', 'myemail@email.com')
    assert str(user) == 'User(1, myuser, myemail@email.com)'

'''
Given two posts
I can compare them to see if they are equal
'''
def test_post_equality():
    user_01 = User(1, 'myuser', 'myemail@email.com')
    user_02 = User(1, 'myuser', 'myemail@email.com')
    assert user_01 == user_02