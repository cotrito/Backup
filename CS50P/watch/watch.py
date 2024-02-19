import re
import sys


def main():
    print(parse(input("HTML: ")))
    #print(parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'))
    #print(parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'))


def parse(s):
    match = re.search(r'.*src="([a-z]+)(://)(www\.)?([a-z.]+)/([a-z]+)/([a-z0-9]+).*',s,re.IGNORECASE)
    if match :
        return "https://youtu.be/" + match.group(6)

if __name__ == "__main__":
    main()