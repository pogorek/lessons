def decrypt_story():
    story = get_story_string()
    st = CiphertextMessage(story)
    return st.decrypt_message()
