class NaiveBayesSentenceSplitter:

    def __init__(self):
        self.data_path = "data/data_for_naive_bayes.txt"
        self.tag_path = "data/tag_for_naive_bayes.txt"
        self.data = self.read(self.data_path)
        self.tag = self.read(self.tag_path)

    def splitText(self, text):
        words = text.split()
        sentences = []
        sentence_index = 0
        for word in words:
            prob_of_NS, prob_of_S = self.calculatePosterior(word)
            print(prob_of_NS)
            print(prob_of_S)
            if prob_of_NS > prob_of_S:
                if len(sentences) == 0:
                    sentences.append(word)
                else:
                    sentences[-1] = sentences[-1] + " " + word
            else:
                sentences.append(word)
                sentence_index += 1

        return sentences

    def read(self, path):
        some_list = []
        with open(path) as file:
            for line in file:
                for t in line.split():
                    some_list.append(t)
        return some_list

    def calculatePrior(self, tag):
        prior = 0
        for i in range(len(self.tag)):
            if self.tag[i] == tag:
                prior += 1
        return prior / len(self.tag)

    def calculateLikelihood(self, word, word_tag):
        occurance = 1  # laplace smoothing
        num_of_total_words = len(self.data)  # laplace smoothing
        num_of_tag = 0
        joint_occurance = 1  # laplace smoothing
        for w in self.data:
            if w == word:
                occurance += 1
        for t in self.tag:
            if t == word_tag:
                num_of_tag += 1
        for i in range(len(self.data)):
            if self.data[i] == word and self.tag[i] == word_tag:
                joint_occurance += 1
        return joint_occurance / (num_of_tag + num_of_total_words)

    def calculatePosterior(self, word):
        prob_of_being_S = self.calculateLikelihood(word, "NS") * self.calculatePrior("NS")
        prob_of_being_NS = self.calculateLikelihood(word, "S") * self.calculatePrior("S")
        return prob_of_being_NS, prob_of_being_S
