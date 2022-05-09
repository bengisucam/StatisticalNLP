class Stemmer:

    def __init__(self, word):
        self.inflextional_suffix_path = "data/inflextional_suffixes.txt"
        self.derivational_suffix_path = "data/derivational_suffixes.txt"
        self.word = word
        self.inflextional_suffixes = self.getInflectionalSuffixes()
        self.derivational_suffixes = self.getDerivationalSuffixes()
        self.dictionary_words = self.getDictionaryWords()
        self.flag = 1


    def stem(self):
        max_length = 0
        combined = [*self.inflextional_suffixes, *self.derivational_suffixes]
        print(combined)
        w = self.word.lower()
        for suffix_tuple in combined:
            for suffix in suffix_tuple:
                if suffix in w and len(suffix) >= max_length and len(w) >= 2:
                    print("suffix : ", suffix)
                    max_length = len(suffix)
                    print(max_length)
                    start_ind = w.find(suffix,
                                       2)  # start looking for the suffix from the 3rd character since the shorthest word can be 2 chars
                    #w = w[:start_ind]
                    if self.checkIfWordIsInDictionary(w[:start_ind]) is not None:
                        w = w[:start_ind]
                        print("stem : ", w)
                        return w


    def checkIfWordIsInDictionary(self, word):
        if word not in self.dictionary_words:
            if word[:-1] == "b":
                if word[0:len(word)-1] + "p" in self.dictionary_words:
                    return word[0:len(word)-1] + "p"
                else:
                    return None
            elif word[:-1] == "c":
                if word[0:len(word) - 1] + "ç" in self.dictionary_words:
                    return word[0:len(word) - 1] + "ç"
                else:
                    return None
            elif word[:-1] == "d":
                if word[0:len(word) - 1] + "t" in self.dictionary_words:
                    return word[0:len(word) - 1] + "t"
                else:
                    return None
            elif word[:-1] == "g":
                if word[0:len(word) - 1] + "k" in self.dictionary_words:
                    return word[0:len(word) - 1] + "k"
                else:
                    return None
            else:
                return None
        else:
            return word


    def getDictionaryWords(self):
        dictionary_file = "data/" + "turkish_dictionary_words.txt"
        with open(dictionary_file, encoding="utf8") as file:
            words = [line.split()[1] for line in file]
            return words

    def getInflectionalSuffixes(self):
        inflextional_list = []
        with open(self.inflextional_suffix_path, encoding="utf8") as file:
            while line := file.readline().rstrip():
                inflextional_list.append(line.split("|"))
        return inflextional_list

    def getDerivationalSuffixes(self):
        derivational_list = []
        with open(self.derivational_suffix_path, encoding="utf8") as file:
            while line := file.readline().rstrip():
                derivational_list.append(line.split("|"))
        return derivational_list
