#from hnh.util import get_max_score
#
#def test_label():
#    p = [
#        {'label': 'hot dog', 'score':0.5},
#        {'label': 'not hot dog', 'score':0.4}
#    ]
#
#    r = get_max_score(p)
#
#    assert r == "hot dog"

from hnh.util import get_max_label, get_max_label2, get_max_label3

def test_max_p_label():
    p = [
        {'label': 'hot dog', 'score': 0.5},
        {'label': 'not hot dog', 'score': 0.4}
    ]

    assert get_max_label(p)== "hot dog"
    assert get_max_label2(p)== "hot dog"
    assert get_max_label3(p)== "hot dog"
