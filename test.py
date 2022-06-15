import util
import pytest


trans = lambda x: util.transliterator(x, 2)


first_test = [("aman", "ⴰⵎⴰⵏ"),
				  ("gmi!", "ⴳⵎⵉ!"),
				  ("bṭṭu", "ⴱⵟⵟⵓ"),
				  ("da", "ⴷⴰ"),
				  ("ḍar", "ⴹⴰⵔ"),
				  ("tammǝmt", "ⵜⴰⵎⵎⴻⵎⵜ"),
				  ("fus", "ⴼⵓⵙ"),
				  ("krz!", "ⴽⵔⵣ!"),
                  ("ha-t-id", "ⵀⴰ-ⵜ-ⵉⴷ"),
				  ("ḥbu!", "ⵃⴱⵓ!"),
				  ("ɛmmi", "ⵄⵎⵎⵉ"),
				  ("xamuc", "ⵅⴰⵎⵓⵛ"),
				  ("qmmc!", "ⵇⵎⵎⵛ!"),
				  ("imi", "ⵉⵎⵉ"),
				  ("jju!", "ⵊⵊⵓ!"),
                  ("̣ž", "ⵋ"),
				  ("laẓ", "ⵍⴰⵥ"),
				  ("mddn", "ⵎⴷⴷⵏ"),
				  ("nkr!", "ⵏⴽⵔ!"),
				  ("Pulunya", "ⵒⵓⵍⵓⵏⵢⴰ"),
				  ("ɣanim", "ⵖⴰⵏⵉⵎ"),]

@pytest.mark.parametrize(('x', 'y'), first_test)
def test_vosotros(x, y):
    pytest.assume(trans(x) == y)

