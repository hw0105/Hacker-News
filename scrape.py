from bs4 import BeautifulSoup
import requests
import pprint
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    count=input("Number of upvotes: ")
    for idx, item in enumerate(links):
            title = links[idx].getText()  # gets the title of the link
            href = links[idx].get("href")  # gets the link
            vot= subtext[idx].select(".score")
            if len(vot):
                points = int(vot[0].getText().replace(" points", ""))
                if points > int(count):
                    hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)

def requesting_webpages(i):
    # requesting the web page without accessing the browser
    response = requests.get(f"https://news.ycombinator.com/news?p={i}")
    #  parser basically changes one type of data into another
    soup = BeautifulSoup(response.text, 'html.parser')
    #  returns a list of all elements having class storylink
    links = soup.select(".storylink")
    subtext = soup.select(".subtext")
    return links,subtext

def main():
    megalinks,megasubtext=[],[]
    for i in range(0,24):
        links,subtext=requesting_webpages(i)
        megalinks+=links
        megasubtext+=subtext
    news=create_custom_hn(megalinks,megasubtext)
    for i in news:
        print(color.GREEN + i['title'] + color.END)
        print(color.UNDERLINE + color.BLUE + i['link'] + color.END)
        print(color.YELLOW + str(i['votes']) + color.END,end='\n\n')

if __name__=="__main__":
    main()

# pprint.pprint(create_custom_hn(links, votes))
# print(votes[0].getText()) gets the text inside the tags
