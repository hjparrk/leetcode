class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

                node.suggestions.append(product)
                node.suggestions.sort()
                if len(node.suggestions) > 3:
                    node.suggestions.pop()
        
        ans = []
        node = root
        for char in searchWord:
            if char in node.children:
                node = node.children[char]
                ans.append(node.suggestions)
            else:
                node.children = {}
                ans.append([])
        return ans