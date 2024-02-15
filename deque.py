from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


graph = {
    "you": ["alice", "bob", "charlie"],
    "alice": ["tom", "lisa"],
    "bob": ["tom", "lisa"],
    "charlie": ["tom", "lisa"],
    "tom": [],
    "lisa": [],
}


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller")
                return True
            else:
                search_queue = graph[person]
                searched.append(person)

    return False


search("you")
