import streamlit as st
import string

@st.cache
def dictionary():
    with open('twl06.txt') as word_dictionary:
            word_list = word_dictionary.read().lower().splitlines()
    return set(word_list)

def main():

    global target
    target = st.text_input("The middle letter must the 5th letter entered:", value='', max_chars=9, key=None).lower()

    button = st.button('Compute')

    if button:

        for s in target:
            if s not in string.ascii_lowercase:
                st.warning(f"'{s}' is not a valid letter.")
                st.stop()

        if len(target) != 9:
            st.warning(f'Only {len(target)} letters entered. Requires exactly 9.')
            st.stop()

        global middle
        middle = target[4]
        words = []
        word_dict = dictionary()

        for word in word_dict:
            if check_word(word):
                words.append(word)

        words.sort()

        output = ''
        for word in words:
            if (len(word)) == 9:
                x = word.upper()
            else:
                x = word.lower()
            output += str(x) + ', '

        st.write(f'{len(words)} words: {output[:-2]}')

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
    st.title('Target Game')
    main()
