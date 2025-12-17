

def count_words(text):
    words = text.split()
    return len(words)

def count_car(text):
    words = text.lower()
    count = {}
    for i in words:
        if i not in count:
            count[i] = 1
        else: count[i] += 1

    return count

def sort_on(items):
    return items["num"]



def sort_words(items):
    sorted_list = []
    for key, value in items.items():
        pair = {"char": key, "num": value}
        sorted_list.append(pair)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    





