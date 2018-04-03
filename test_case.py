#coding:utf-8
class Node:
    '''data节点保存的数据next保存下一个节点对象'''
    def __init__(self,data,pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)


class