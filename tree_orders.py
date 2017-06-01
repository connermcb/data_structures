# -*- coding: utf-8 -*-
"""
In-Order, Pre-Order, Post-Order Traversals
"""


class Node(object):
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right
        
    def set_parent(self, parent):
        self.parent = parent
        
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_parent(self):
        return self.parent
    
    
    
class Tree(object):
    
    def __init__(self):
        self.node_list = []
        
    
    
    
        
    