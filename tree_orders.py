# -*- coding: utf-8 -*-
"""
In-Order, Pre-Order, Post-Order Traversals
"""



    
    
    
class Tree(object):
    
    def __init__(self, n):
        # list values = keys for self, left, right, parent respectively
        self.node_dict = {x:[-1, -1, -1, -1] for x in range(n)}
        
        
    def add_node(self, k, l, r):
        self.node_dict[k][:3] = [k, l, r]
        self.node_dict[l][3] = k
        self.node_dict[r][3] = k
                      
        
        
        
        
    
    
    
    
        
    