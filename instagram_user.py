class User:
    def __init__(self, posts, followers, following, followers_list):
        self.posts = posts
        self.followers = followers
        self.following = following
        self.followers_list = followers_list

    # GET
    def get_posts(self):
        return self.posts

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def get_followers_list(self):
        return self.followers_list

    # SET
    def set_posts(self, posts):
        self.posts = posts

    def set_followers(self, followers):
        self.followers = followers

    def set_following(self, following):
        self.following = following

    def set_followers_list(self, followers_list):
        self.followers_list = followers_list
