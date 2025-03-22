from finder import Finder

def main():
    finder = Finder()
    topics = finder.getData()
    finder.find(topics)

main()