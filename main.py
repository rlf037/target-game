import streamlit as st

import string

@st.cache
def dictionary():
    with open('twl06.txt') as word_dictionary:
            word_list = word_dictionary.read().lower().splitlines()
    return set(word_list)

def main():

    global target
    target = st.text_input("Target", value='', max_chars=9, key=None).lower()

    for s in target:
        if s not in string.ascii_lowercase:
            st.error(f'{s} is not a valid letter.')

    button = st.button('Find')

    if button:

        global middle
        middle = target[4]

        nine_letter = []
        words = []

        for word in dictionary():
            if check_word(word):
                if len(word) == 9:
                    nine_letter.append(word)
                else:
                    words.append(word)

        st.write(f'{len(words) + len(nine_letter)} words: {words}')
        st.write('')
        st.write(f'9 letter: {nine_letter}')

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
    st.set_page_config(page_title='Target', page_icon='🎯')
    main()