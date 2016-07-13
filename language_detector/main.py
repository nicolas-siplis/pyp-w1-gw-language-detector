"""This is the entry point of the program."""
# coding=utf-8
from .languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    spanish, german, english = [set(LANGUAGES[x]['common_words']) for x in range(3)]
    language_list = [spanish, german, english]
    set_text = set(text.split())
    
    sp_inters, ge_inters, en_inters = [set_text.intersection(lang) for lang in language_list]
    intersections = [sp_inters, ge_inters, en_inters]
    idx = intersections.index(max(intersections))
    
    return LANGUAGES[idx]['name']