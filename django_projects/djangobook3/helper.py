from main.models import Post
from django.contrib.auth.models import User

try:
    user = User.objects.get(id=1)

    post = Post(
        title="test post 1",
        slug="test-post-1",
        body="test body 1",
        author = user
    )
    post.save()

    post2 = Post(
        title="test post 2",
        slug="test-post-2",
        body="test body 2",
        author = user
    )
    post2.save()

    post3 = Post(
        title="test post 3",
        slug="test-post-3",
        body="test body 3",
        author = user
    )
    post3.save()

    post4 = Post(
        title="test post 4",
        slug="test-post-4",
        body="test body 4",
        author = user
    )
    post4.save()

    post5 = Post(
        title="test post 5",
        slug="test-post-5",
        body="test body 5",
        author = user
    )
    post5.save()

    post6 = Post(
        title="test post 6",
        slug="test-post-6",
        body="test body 6",
        author = user
    )
    post6.save()

    print("Successfully inserted data")
    print(Post.objects.all())

except Exception as e:
    print(e)
    print("Trouble!!!")
    
