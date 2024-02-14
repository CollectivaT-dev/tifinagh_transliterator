#import unicodedata

dict_lat_to_tifinagh = {
	'a': 'ⴰ',
	'b': 'ⴱ',
	'ɡ': 'ⴳ',
	'd': 'ⴷ',
	'e': 'ⴻ',
	'ǝ': 'ⴻ',
	'f': 'ⴼ',
	'k': 'ⴽ',
	'h': 'ⵀ',
	'ɛ': 'ⵄ',
	'm': 'ⵎ',
	't': 'ⵜ',
	'č': 'ⵞ',
	'ṭ': 'ⵟ',
	's': 'ⵙ',
	'z': 'ⵣ',
	'ṛ': 'ⵕ',
	'ḍ': 'ⴹ',
	'n': 'ⵏ',
	'l': 'ⵍ',
	'r': 'ⵔ',
	'ṣ': 'ⵚ',
	'c': 'ⵛ',
	'j': 'ⵊ',
	'x': 'ⵅ',
	'ḥ': 'ⵃ',
	'w': 'ⵡ',
	'ɣ': 'ⵖ',
	'ʷ': 'ⵯ',
	'ẓ': 'ⵥ',
	'q': 'ⵇ',
	'y': 'ⵢ',
	'i': 'ⵉ',
	'u': 'ⵓ',
	'p': 'ⵒ',
	'v': 'ⵠ',
	'ẓ̌': 'ⵋ'
}

dict_tifinagh_to_lat = dict((v, k) for k, v in dict_lat_to_tifinagh.items())

# dict_tifinagh_to_lat = {
# 	'ⴱ': 'b',
# 	'ⵎ': 'm',
# 	'ⴼ': 'f',
# 	'ⵜ': 't',
# 	'ⴷ': 'd',
# 	'ⵟ': 'ṭ',
# 	'ⵙ': 's',
# 	'ⵣ': 'z',
# 	'ⵕ': 'ṛ',
# 	'ⴹ': 'ḍ',
# 	'ⵏ': 'n',
# 	'ⵍ': 'l',
# 	'ⵔ': 'r',
# 	'ⴳ': 'g',
# 	'ⵚ': 'ṣ',
# 	'ⵛ': 'ch',
# 	'ⵊ': 'j',
# 	'ⵅ': 'kh',
# 	'ⵃ': 'ḥ',
# 	'ⵄ': '3',
# 	'ⵡ': 'w',
# 	'ⵀ': 'h',
# 	'ⵡ': 'w',
# 	'ⴽ': 'k',
# 	'ⵥ': 'ẓ',
# 	'ⵇ': 'q',
# 	'ⵢ': 'y',
# 	'ⴰ': 'a',
# 	'ⵉ': 'i',
# 	'ⵓ': 'u',
# 	'ⴻ': 'ǝ',
#     'ⵠ': 'v',
#     'ⴹ': 'ḍ',
#     'ⴼ': 'f',
#     'ⵄ': 'ɛ',
#     'ⵅ': 'x',
#     'ⵊ': 'j',
#     'ⵋ': '̣ž',
#     'ⵓ': 'u',
#     'ⵒ': 'p',
#     'ⵛ': 'c',
#     'ⵢ': 'y',
#     'ⵣ': 'z',
#     'ⵖ': 'ɣ'}

# dict_lat_to_tifinagh = dict((v, k) for k, v in dict_tifinagh_to_lat.items())


tifinagh_set = ['ⴱ', 'ⵎ', 'ⴼ', 'ⵜ', 'ⴷ', 'ⵟ', 'ⵙ', 'ⵣ', 'ⵕ', 'ⴹ', 'ⵏ', 'ⵍ', 'ⵔ', 'ⴳ', 
				'ⵚ', 'ⵛ', 'ⵊ', 'ⵅ', 'ⵃ', 'ⵄ', 'ⵡ', 'ⵀ', 'ⵡ', 'ⴽ', 'ⵥ', 'ⵇ', 'ⵢ', 'ⴰ', 
				'ⵉ', 'ⵓ', 'ⴻ', 'ⵠ', 'ⴹ', 'ⴼ', 'ⵄ', 'ⵅ', 'ⵊ', 'ⵋ', 'ⵓ', 'ⵒ', 'ⵛ', 'ⵢ', 'ⵣ', 'ⵖ']
    
#catacter igual a su mismo alpha
def transliterator(word, dictionary):
    if len(word) <= 0:
        return "Introduce a word or sentence"
    else:
        word = word.lower()
        new_word = ""
        for l in word:
            w = dictionary.get(l)
            
            if w:
                new_word = new_word + w[0]
            else:
                new_word = new_word + l
        return new_word

def latin_to_tifinagh(word):
	return transliterator(word, dict_lat_to_tifinagh)

def tifinagh_to_latin(word):
	return transliterator(word, dict_tifinagh_to_lat)

