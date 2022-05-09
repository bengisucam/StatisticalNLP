from SentenceSplitter import SentenceSplitter
from StaticStopWordsRemover import StaticStopWordRemover
from DynamicStopWordsRemover import DynamicStopWordRemover
from ReadDataset import Reader
from Stemmer import Stemmer
from NaiveBayesSentenceSplitter import NaiveBayesSentenceSplitter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    splitter = SentenceSplitter('Bugün kaçta geleceksin? Ben de ona göre hazırlanayım. Belki gelmem... (Veya '
                                'gelirim.)"Gelmeyebilirim." Avukat hanımın adı Ayşe.')
    splitted = splitter.splitText()
    print(splitted)

    list_of_words = ["bugün", "kaç", "gibi", "benim", "dokuz", "ile"]
    staticRemover = StaticStopWordRemover(list_of_words, "nltk_turkish_stop_words.txt")
    removed = staticRemover.removeStopWords()
    print(removed)

    reader = Reader("tr_boun-ud-train.conllu")
    dataset = reader.readDataset()
    print(dataset[:10])

    dynamicRemover = DynamicStopWordRemover(dataset, list_of_words)
    idf_values_and_words = dynamicRemover.calculate_IDF()
    dynamic_removed = dynamicRemover.removeStopWords()
    dynamic_stop_words = dynamicRemover.createStopWordsList()
    print(idf_values_and_words)
    print(dynamic_stop_words)
    print(removed)

    word_list = ["çocuklardanmış", "şekerliksiz", "kalemliklerdendir", "geldiler", "varmışlardır", ""]
    #word_list = ["varmış"]
    for w in word_list:
        stemmer = Stemmer(w)
        stemmer.stem()

    dictionary_file = "data/" + "turkish_dictionary_words.txt"
    with open(dictionary_file, encoding="utf8") as file:
        words = [line.split()[1] for line in file]
        print(words)

    text_to_be_splitted = "Bugün bir gün. Yemek verildi. İstanbul güzeldir."
    naive_splitter = NaiveBayesSentenceSplitter()
    sentences = naive_splitter.splitText(text_to_be_splitted)
    print(sentences)

    print(dynamic_stop_words)





