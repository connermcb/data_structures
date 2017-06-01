# -*- coding: utf-8 -*-
"""
In-Order, Pre-Order, Post-Order Traversals
"""



    
    
    
class Tree(object):
    
    def __init__(self, n):
        # list values = keys for self, dictkey left, dictkey right respectively
        self.node_dict = {x:[-1, -1, -1]}
        self.result_in_order = []
        self.result_pre_order = []
        self.result_post_order = []
        
        
    def add_node(self, i, k, l, r):
        self.node_dict[i] = [k, l, r]

                      
    def in_order(self, t):
        if sum(self.node_dict[t][1:3]) == -2:
            return
        key, left, right = self.node_dict[t][:3]
        self.in_order(left)
        self.result_in_order.append(key)
        self.in_order(right)
        
    def pre_order(self, t):
        if sum(self.node_dict[t][1:3]) == -2:
            return       
        key, left, right = self.node_dict[t][:3]
        self.result_pre_order.append(key)
        self.pre_order(left)
        self.pre_order(right)
        
    def post_order(self, t):
        if sum(self.node_dict[t][1:3]) == -2:
            return       
        key, left, right = self.node_dict[t][:3]
        self.post_order(left)
        self.post_order(right)
        self.result_post_order.append(key)
    
    
n=5        
t = Tree(n)


l =[(4, 1, 2), (2, 3, 4), (5, -1, -1), (1, -1, -1), (3, -1, -1)]

for i in range(len(l)):
    k, l, r = each
    t.add_node(i,k,l,r)
    
print(t.node_dict)
    
    
        
    