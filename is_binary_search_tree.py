#python3
# -*- coding: utf-8 -*-
"""
Binary Tree or Not
"""

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeChecker(object):
    
    def __init__(self, n):
        # list values = keys for self, dictkey left, dictkey right respectively
        self.node_dict = {x:[-1, -1, -1] for x in range(n)}
        self.in_order_list = []
        self.result = 'CORRECT'

               
    def add_node(self, i, k, l, r):
        self.node_dict[i] = [k, l, r]
                     
    def in_order(self, t):
        key, left, right = self.node_dict[t][:3]
        if left != -1:
            self.in_order(left)
        self.in_order_list.append(key)
        if self.in_order_list[-1] < self.in_order_list[-2]:
            self.result = 'INCORRECT'
            return
        if right != -1:
            self.in_order(right)
            
def main():
    n = int(sys.stdin.readline())
           
    t = TreeChecker(n)
    
    for i in range(n):
        k, l, r = map(int, sys.stdin.readline().split())
        t.add_node(i,k,l,r)
    t.in_order(0) 
    print(t.result)
    
threading.Thread(target=main).start()