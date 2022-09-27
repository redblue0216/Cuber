import networkx as nx
from cuber.model.mixin import *


def test_func(a):
    print('this is a test function!')
    print(a)
    return a


tmp_data = DataModelMixin(name='test_func',params={'a':100},obj=test_func)
dag = nx.DiGraph()
dag.add_node('test',data=tmp_data)
tmp_obj = dag.nodes['test']['data'].obj
tmp_obj.__call__(123)
print(type(tmp_obj))

