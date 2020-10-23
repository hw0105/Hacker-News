from bs4 import BeautifulSoup
import requests
import pprint

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

# requesting the web page without accessing the browser
response = requests.get("https://news.ycombinator.com/")
# parser basically changes one type of data into another
soup = BeautifulSoup(response.text, 'html.parser')
# returns a list of all elements having class storylink
links = soup.select(".storylink")
votes = soup.select(".score")
# print(links)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x['votes'], reverse=True)


def create_custom_hn(links, votes):
    hn = []
    count = 0
    for idx, item in enumerate(links):
        if soup.select(".subtext")[idx].select(".score"):
            title = links[idx].getText()  # gets the title of the link
            href = links[idx].get("href")  # gets the link
            vot = int(votes[count].getText().replace(" points", ""))
            if vot > 100:
                hn.append({"title": title, "link": href, "votes": vot})
            count += 1
    return sort_stories_by_votes(hn)


news=create_custom_hn(links,votes)
for i in news:
    print(color.GREEN + i['title'] + color.END)
    # print(i['title'])
    print(color.UNDERLINE + color.BLUE + i['link'] + color.END)
    # print(i['link'])
    print(color.YELLOW + str(i['votes']) + color.END,end='\n\n')
    # print(i['votes'],end="\n\n")

# pprint.pprint(create_custom_hn(links, votes))
# print(votes[0].getText()) gets the text inside the tags
