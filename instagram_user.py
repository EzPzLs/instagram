class User:
    def __init__(self, posts, followers, following):
        self.posts = posts
        self.followers = followers
        self.following = following

    def get_posts(self):
        return self.posts

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def set_posts(self, posts):
        self.posts = posts

    def set_followers(self, followers):
        self.followers = followers

    def set_following(self, following):
        self.following = following
