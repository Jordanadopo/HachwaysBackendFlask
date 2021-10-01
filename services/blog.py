
import requests


class Blog():

    def __init__(self):
        self.baseurl="https://api.hatchways.io/assessment/blog/posts?tag="

    #Return posts by tag
    def get_posts(self, tags_string: str, sortBy:str="", direction:str=""):
        posts = []
        tags=tags_string.split(',')
        #call function to fech hatchways posts data
        for tag in tags:
            # get posts by tag
            fetched = self.fetchposts(tag)['posts']
            #add post to posts to return if not in
            for post in fetched:
                if post not in posts:
                    posts.append(post)
        
        # Sort in-place based on desired (parameters) criteria
        is_reverse = True if direction == "desc" else False
        # posts.sort(key=lambda x: x[sort_by], reverse=is_reverse)
        posts = sorted(posts, key=lambda x: x[sortBy], reverse=is_reverse)


        return posts

    
    def fetchposts(self,tag):
        url=self.baseurl+tag
        data= requests.get(url).json()
        print([tag, data])
        return data

        
        