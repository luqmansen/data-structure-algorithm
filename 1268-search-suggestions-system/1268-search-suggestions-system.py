from typing import List


class Trie:
    def __init__(self):
        self.edges = dict()
        self.is_end = False

    def insert(self, word):
        curr = self

        for c in word:
            if c in curr.edges:
                curr = curr.edges[c]
                continue
            else:
                new = Trie()
                curr.edges[c] = new
                curr = new

        curr.is_end = True

    def get_start_with(self, prefix):

        words = []
        current = self

        for c in prefix:
            if c in current.edges:
                current = current.edges[c]
            else:
                return words

        if len(current.edges) > 0:
            self.find(prefix, current, words)
        else:
            if current.is_end:
                words.append(prefix)

        return words

    def find(self, prefix, node, words):

        if node.is_end is True:
            words.append(prefix)

        if node.edges is None:
            return

        for c, n in node.edges.items():
            self.find(prefix + c, n, words)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = Trie()

        for p in products:
            trie.insert(p)

        sug = []

        word = ""
        for c in searchWord:
            word += c
            res = trie.get_start_with(word)
            res = sorted(res)
            sug.append(res[:3])
        
        return sug

if __name__ == '__main__':

    s = Solution()

    s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse")
