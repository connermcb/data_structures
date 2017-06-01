#python3
# -*- coding: utf-8 -*-
"""
In-Order, Pre-Order, Post-Order Traversals
"""
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
    
class Tree(object):
    
    def __init__(self, n):
        # list values = keys for self, dictkey left, dictkey right respectively
        self.node_dict = {x:[-1, -1, -1] for x in range(n)}
        self.result_in_order = []
        self.result_pre_order = []
        self.result_post_order = []
               
    def add_node(self, i, k, l, r):
        self.node_dict[i] = [k, l, r]
                     
    def in_order(self, t):
        key, left, right = self.node_dict[t][:3]
        if left != -1:
            self.in_order(left)
        self.result_in_order.append(key)
        if right != -1:
            self.in_order(right)
        
    def pre_order(self, t):     
        key, left, right = self.node_dict[t][:3]
        self.result_pre_order.append(key)
        if left != -1:
            self.pre_order(left)
        if right != -1:
            self.pre_order(right)
        
    def post_order(self, t): 
        key, left, right = self.node_dict[t][:3]
        if left != -1:
            self.post_order(left)
        if right != -1:
            self.post_order(right)
        self.result_post_order.append(key)
    
def main():
    n = int(sys.stdin.readline())
           
    t = Tree(n)
    
    for i in range(n):
        k, l, r = map(int, sys.stdin.readline().split())
        t.add_node(i,k,l,r)
    
    t.in_order(0) 
    print(" ".join(map(str,t.result_in_order)))
    t.pre_order(0)
    print(" ".join(map(str,t.result_pre_order)))
    t.post_order(0)
    print(" ".join(map(str,t.result_post_order)))
        
threading.Thread(target=main).start()
    