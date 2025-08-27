def count_words(result):
        return result.split()

def count_chars(text):
	char_count = {}
       
	for chars in text.lower():
		if chars in char_count:
			char_count[chars] += 1
		else:
			char_count[chars] = 1
	return char_count

def sort_on(item):
    return item["num"]

def build_sorted(counts):
    result = []
    for ch, n in counts.items():
        if ch.isalpha():
            result.append({"char": ch, "num": n})
    result.sort(key=sort_on, reverse=True)
    return result
