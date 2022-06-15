#import unicodedata

dictionary = {
	'ⴱ': 'b',
	'ⵎ': 'm',
	'ⴼ': 'f',
	'ⵜ': 't',
	'ⴷ': 'd',
	'ⵟ': 'ṭ',
	'ⵙ': 's',
	'ⵣ': 'z',
	'ⵕ': 'ṛ',
	'ⴹ': 'ḍ',
	'ⵏ': 'n',
	'ⵍ': 'l',
	'ⵔ': 'r',
	'ⴳ': 'g',
	'ⵚ': 'ṣ',
	'ⵛ': 'ch',
	'ⵊ': 'j',
	'ⵅ': 'kh',
	'ⵃ': 'ḥ',
	'ⵄ': '3',
	'ⵡ': 'w',
	'ⵀ': 'h',
	'ⵡ': 'w',
	'ⴽ': 'k',
	'ⵥ': 'ẓ',
	'ⵇ': 'q',
	'ⵢ': 'y',
	'ⴰ': 'a',
	'ⵉ': 'i',
	'ⵓ': 'u',
	'ⴻ': 'ǝ',
    'ⵠ': 'v',
    'ⴹ': 'ḍ',
    'ⴼ': 'f',
    'ⵄ': 'ɛ',
    'ⵅ': 'x',
    'ⵊ': 'j',
    'ⵋ': '̣ž',
    'ⵓ': 'u',
    'ⵒ': 'p',
    'ⵛ': 'c',
    'ⵢ': 'y',
    'ⵣ': 'z',
    'ⵖ': 'ɣ',
	' ': ' ',
	',': ',',
    '!': '!',
	'.': '.',
	':': ':'}
    
#catacter igual a su mismo alpha
def transliterator(word,src):
    if len(word) <= 0:
        return "Introduce a word or sentence"
    else:
        word = word.lower()
        new_word = ""
        for l in word:
            if src == 1:
                w = dictionary.get(l)
            else:
                dict_items=dictionary.items()
                w=[key for key,value in dict_items if value==l]
            if len(w) != 0:
                new_word = new_word + w[0]
            else:
                new_word = new_word + l
        return new_word