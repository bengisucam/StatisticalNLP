

class StaticStopWordRemover:

    def __init__(self, word_list, rule_path):
        self.stop_words_path = "data/" + rule_path
        self.sentence_words = word_list
        self.stop_words = self.getStopWords()

    def getStopWords(self):
        words = set()
        with open(self.stop_words_path) as file:
            while line := file.readline().rstrip():
                words.add(line.rstrip())
        return words

    def removeStopWords(self):
        new_sentence = []
        for word in self.sentence_words:
            if word not in self.stop_words:
                new_sentence.append(word)
        return new_sentence



