class User:
    def __init__(self, name):
        self.name = name
        self.isLoggedIn = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].isLoggedIn:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Ahsan")
new_user.isLoggedIn = False

create_blog_post(new_user)
