class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
        # from parent
        # self.message_text = text
        # self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        import re

        good_words = load_words(WORDLIST_FILENAME)
        shift_try = 0
        most_words = 0
        winner = 0

        while shift_try < 26:
            current_words = 0
            new_message = self.apply_shift((26 - shift_try))
            new_message_words = re.sub("[^\w]", " ",  new_message).split()
            #print('new_message_words: ', new_message_words)

            for word in new_message_words:
                if is_word(good_words, word):
                    current_words += 1
                    # print("jest")

            if current_words > most_words:
                most_words = current_words
                winner = 26 - shift_try
            shift_try += 1

        return (winner, self.apply_shift((winner)))
