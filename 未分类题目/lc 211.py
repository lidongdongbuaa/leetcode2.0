# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 20:39
# @Author  : LI Dongdong
# @FileName: lc 211.py

class TrieNode:
    def __init__(self):
        self.is_end =False
        self.children = [None] * 26


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # p=self.root
        # n=len(word)
        # for i in range(n):
        #     p=p.children[ord(word[i])-ord('a')]
        #     if p is None:
        #         new_node=TrieNode()
        #         if i ==n-1:
        #             new_node.is_end=True
        #         p=new_node
        #     else:
        #         p=p.children[ord(word[i])-ord('a')]
        #         if i==n-1:
        #             p.is_end=True
        #             return

        p = self.root
        n = len(word)
        for i in range(n):
            if p.children[ord(word[i]) - ord('a')] is None:
                new_node = TrieNode()
                if i == n - 1:
                    new_node.is_end = True
                p.children[ord(word[i]) - ord('a')] = new_node
                p = new_node
            else:
                #在重复插入，比如woord和wor时，此段用上
                p = p.children[ord(word[i]) - ord('a')]
                if i == n - 1:
                    p.is_end = True
                    return

    def dfs(self,i,word,p):
        if i==len(word):
            if p.is_end is True:
                return True
            return False
        if word[i]=='.':
            for j in range(26):
                if p.children[j] and self.dfs(i+1,word,p.children[j]):
                    return True
        else:
            if p.children[ord(word[i])-ord('a')] and self.dfs(i+1,word,p):
                return True
        return False


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        p=self.root
        return self.dfs(0,word,p)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
# if obj.search('bad') is True:
#     print('true')
# else:
#     print('False')

if obj.search('.ad') is True:
    print('true')
else:
    print('False')

if obj.search('b..') is True:
    print('true')
else:
    print('False')