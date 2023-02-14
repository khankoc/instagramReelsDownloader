from instaloader import Instaloader, Post
import re


L = Instaloader()


def linkdownload(link):
    id_pattern = r"(/p/|/reel/)([a-zA-Z0-9_-]+)/"
    match = re.search(id_pattern, link)

    if match:
        id = match.group(2)
        post = Post.from_shortcode(L.context, id)
        print(f"{post} downloading..")
        L.download_post(post, target="downloads")
    else:
        print("Post ID not found in the link.")
        print("Please provide a link to the function on line 19 !")
    
linkdownload("-PASTE LINK HERE-") 
    




           


    
   

    



