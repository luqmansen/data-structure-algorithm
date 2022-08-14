class Trie:

    def __init__(self):
        self.edges = dict()
        self.is_end = False

    def insert(self, word: str) -> None:
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

    def search(self, word: str) -> bool:
        curr = self

        for c in word:
            if c in curr.edges:
                curr = curr.edges[c]
                continue
            else:
                return False

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self

        for c in prefix:
            if c in curr.edges:
                curr = curr.edges[c]
                continue
            else:
                return False

        return True
