# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 18:09
# @Author  : LI Dongdong
# @FileName: lc 208.py

class TrieNode:
    def __init__(self):
        # 是否构成一个完成的单词
        self.is_end = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #代替了每一步中都要建立根节点的步骤
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ##############网络方法##############
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

    def search(self,word:str) -> bool:
        """""
        Returns if the word is in the trie
        """""
        p=self.root
        #判断word每个字母都在trie里
        for c in word:
            #children里保存节点，相当于有节点有属性children，children为list，list里保存下级节点
            #p在更新
            p=p.children[ord(c)-ord('a')]
            if p is None:
                return False
        #判断word的最后一个字母在tie中有结尾属性，即不会出现word=app，tie中是appl，从而报true的错误
        if p.is_end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p=self.root
        for c in prefix:
            p=p.children[ord(c)-ord('a')]
            if p is None:
                return False
        return True




obj = Trie()
obj.insert('woord')
obj.insert('wod')
obj.insert('aod')
obj.search('wooe')