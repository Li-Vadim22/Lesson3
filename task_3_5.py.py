'''
5 Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        	Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
'''''


from random  import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def some_jokes(n, repeat=False): # возвращаем случайные шутки, не повторяющиеся


    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no,adv,adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return  list_of_j


print(some_jokes(3, True))