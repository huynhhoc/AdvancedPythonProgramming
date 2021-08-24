from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    listStory = story.readlines()
    print(listStory[2])
print('done')
