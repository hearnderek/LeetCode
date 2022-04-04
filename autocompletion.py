from typing import List


class TrieNode:
    def __init__(self, char, parent):
        self.parent = parent
        self.children = dict()
        self.char = char
    
    @staticmethod
    def create_head() -> 'TrieNode':
        return TrieNode(None, None)

    @staticmethod    
    def create_leaf(parent: 'TrieNode') -> 'LeafTrieNode':
        return LeafTrieNode(None, parent)

    def add_word(self, word:str):
        curNode = self
        for c in word:
            if c in curNode.children:
                curNode = curNode.children[c]
            else:
                curNode.children[c] = TrieNode(c, curNode)
                curNode = curNode.children[c]
        curNode.children[None] = TrieNode.create_leaf(curNode)

    def build_words(self) -> List[str]:
        words = list()
        for child in self.children.values():
            for ret in child.build_words():
                words.append(ret)
        return words

class LeafTrieNode(TrieNode):
    def build_words(self) -> List[str]:
        cur = self.parent
        chars = list()
        while cur.parent:
            chars.append(cur.char)
            cur = cur.parent
        return ["".join(reversed(chars))]
            


def build_trie_tree(words: List[str]) -> TrieNode:
    """ returns Trie Tree Head node"""
    head = TrieNode.create_head()
    for word in words:
        head.add_word(word)

    return head

def find_words_that_match(head: TrieNode, prefix: str):
    # go down the tree following prefix
    # Build the rest of the words based on the 
    cur = head

    for c in prefix:
        if c in cur.children:
            cur = cur.children[c]
        else:
            return []
    
    return cur.build_words()


    

def autocomplete_trie(words: List[str], prefix):
    tree = build_trie_tree(words)
    return find_words_that_match(tree, prefix)



def autocomplete(words: List[str], prefix):
    """ return all words that have this prefix """
    ret = list()

    for word in words:
        if word.startswith(prefix):
            ret.append(word)

    return ret


def testAgainst(words, prefix):
    expected = autocomplete(words, prefix)
    r = autocomplete_trie(words, prefix)
    ret = tuple(sorted(r))
    e = tuple(sorted(expected))
    if ret != e:
        print("FAIL:", words, prefix)
        print("Got:", r)
        print("Expected:", e)

def test(words, prefix, expected):
    r = autocomplete(words, prefix)
    ret = tuple(sorted(r))
    e = tuple(sorted(expected))

    if ret != e:
        print("FAIL:", words, prefix)
        print("Got:", r)
        print("Expected:", expected)

if __name__ == '__main__':
    test(["dog", "dark", "cat", "door", "dodge"], "do", ["dog", "door", "dodge"])
    testAgainst(["dog", "dark", "cat", "door", "dodge"], "do")