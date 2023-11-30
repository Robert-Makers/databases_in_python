from lib.post import Post

'''
post contructs with id, title, content and user_id parameters
'''
def test_post_construct():
    post = Post(1, 'Day one', 'here we go', 1)
    assert post.id == 1
    assert post.title == 'Day one'
    assert post.content == 'here we go'
    assert post.user_id == 1

'''
Given a post
I can return a formatted string
'''
def test_format_post():
    post = Post(1, 'Day one', 'here we go', 1)
    assert str(post) == 'Post(1, Day one, here we go, 1)'

'''
Given two posts
I can compare them to see if they are equal
'''
def test_post_equality():
    post_01 = Post(1, 'Day one', 'here we go', 1)
    post_02 = Post(1, 'Day one', 'here we go', 1)
    assert post_02 == post_01