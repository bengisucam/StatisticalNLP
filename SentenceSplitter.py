import logging
import regex


class SentenceSplitter:

    def __init__(self, text):
        self.rule_path = "data/non_breaking_prefixes_tr.txt"
        self.text = text

    def splitText(self):
        # check if text is null
        if not self.text:
            logging.warning("Please provide a non-empty text")
            return []
        if self.text:
            print("text dolu")

        # Sentence markes such as "?", "!" that are not period, followed by sentence starter
        multiple_dots_replaced = regex.sub(r'\.+', ".", self.text)
        compiler = regex.compile(r'([A-Z][^\.!?]*[\.!?])', regex.M)
        sentences = compiler.findall(multiple_dots_replaced)
        return sentences

    def getNonBreakingPrefixes(self):
        non_breaking_list = []
        with open(self.rule_path) as file:
            while line := file.readline().rstrip():
                if line.split()[0] == "#":
                    non_breaking_list.append(line.split()[1:])
                else:
                    non_breaking_list.append(line.split()[0])
        return non_breaking_list
