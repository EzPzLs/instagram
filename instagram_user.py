class User:
    def __init__(self, posts, followers, following, followers_list):
        self.posts = posts
        self.followers = followers
        self.following = following
        self.followers_list = followers_list
        self.new_followers_list = []
        self.lost_followers_list = []

    # GET
    def get_posts(self):
        return self.posts

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def get_followers_list(self):
        return self.followers_list

    def get_new_followers_list(self):
        return self.new_followers_list

    def get_lost_followers_list(self):
        return self.lost_followers_list

    # SET
    def set_posts(self, posts):
        self.posts = posts

    def set_followers(self, followers):
        self.followers = followers

    def set_following(self, following):
        self.following = following

    def set_followers_list(self, followers_list):
        self.followers_list = followers_list

    def set_new_followers_list(self, new_followers_list):
        self.new_followers_list = new_followers_list

    def set_lost_followers_list(self, lost_followers_list):
        self.lost_followers_list = lost_followers_list

    #######

    def new_follower(self, follower):
        self.new_followers_list.append(follower)
        self.followers_list.append(follower)

    def lost_follower(self, follower):
        self.lost_followers_list.append(follower)
        self.followers_list.remove(follower)
