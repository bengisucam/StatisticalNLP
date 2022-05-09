import operator

from sklearn.feature_extraction.text import TfidfVectorizer


class DynamicStopWordRemover:

    def __init__(self, docs, word_list):
        self.docs = docs
        self.word_list = word_list
        self.stop_words = self.createStopWordsList()

    def calculate_IDF(self):
        tf_idf_vectorizer = TfidfVectorizer()
        scores = tf_idf_vectorizer.fit_transform(self.docs)
        feature_names = tf_idf_vectorizer.get_feature_names_out()
        idf_values = dict(zip(feature_names, tf_idf_vectorizer.idf_))
        sorted_tuples = sorted(idf_values.items(), key=operator.itemgetter(1))
        return sorted_tuples[:120]

    def createStopWordsList(self):
        sw = []
        for t in self.calculate_IDF():
            sw.append(t[0])
        return sw

    def removeStopWords(self):
        new_sentence = []
        for word in self.word_list:
            if word not in self.stop_words:
                new_sentence.append(word)
        return new_sentence
