def words_count():
    words = [w.lower() for w in input().split()]
    d = {w: words.count(w) for w in words}
    for k, v in d.items():
        print(k, v)

words_count()
#text = "a aa abC aa ac abc bcd a"
