import random
import webbrowser

web_sites = ['hackernews', 'facebook', 'netflix', 'amazon', 'leetcode', 'youtube']

def openRandomWebsite():
   site = random.choice(web_sites)

   url = f'http://www.{site}.com'
   print(f"Opening: {url}")

   webbrowser.open(url)

openRandomWebsite();