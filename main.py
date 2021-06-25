import streamlit as st

import os
import sys


word_file = 'twl06.txt'


def main():

    global target
    target = st.text_input("Target", value='_________', max_chars=9, key=None)

    global middle

    button = st.button('Find')

    if button:

        middle = target[4]

        with open(word_file) as word_dictionary:
            word_list = word_dictionary.read().lower().splitlines()

        nine_letter = []
        words = []

        for word in word_list:
            if check_word(word):
                if len(word) == 9:
                    nine_letter.append(word)
                else:
                    words.append(word)

        st.write(words)
        st.write(nine_letter)
        st.write(len(words) + len(nine_letter))

def check_word(w):
    if len(w) < 4:
        return False
    if middle not in w:
        return False

    target_list = list(target)
    char_list = list(w)
    while char_list:
        if char_list[0] in target_list:
            target_list.remove(char_list[0])
            char_list.pop(0)
        else:
            return False
    return True


if __name__ == '__main__':
    st.set_page_config(page_title='Target', page_icon='🏉')
    main()