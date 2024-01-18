class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.word = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        current = self.word[self.index]
        self.index += 1
        return current


my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)



def sentence_func(sentence):
    for word in sentence.split():
        yield word

my_sentence1 = sentence_func('This is a test')

for word in my_sentence1:
    print(word)