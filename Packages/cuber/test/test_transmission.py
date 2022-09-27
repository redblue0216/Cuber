import networkx as nx
import functools
from inspect import signature


### 通过装饰器技术将目标函数加载进dag
class Decorator(object):
    
    def __init__(self,name):
        self.name = name
        self.dag = nx.DiGraph() ### cuber中为scheduler调度管理器
    
    def test(self,func):
        @functools.wraps(func)
        def tested(*args,**kwargs):
            result = func(*args,**kwargs)
            print('decorator starting!')
            self.dag.add_node(func.__name__,data=func)
            return result
        return tested

decorator = Decorator(name='test')

@decorator.test
def test_a(a):
    return a

print('decorator================',decorator.dag.nodes)

def test_b(b):
    return b + 1

def test_c(c):
    return c + 1

def test_d(b,c):
    return b + c

def test_e(e):
    return e + 10


dag = nx.DiGraph()
### 单点添加
dag.add_node('test_a',data=test_a)
dag.add_node('test_b',data=test_b)
dag.add_node('test_c',data=test_c)
dag.add_node('test_d',data=test_d)
print('~~~~~~~~~~~~~~~~',dag.nodes)
tmp = dag.nodes['test_a']
print('^^^^^',tmp)
print('########',dag.nodes['test_a']['data'])
dag.nodes['test_a']['data'] = test_e
print('########',dag.nodes['test_a']['data'])
### 批量节点添加
# dag.add_nodes_from([
#     ('test_a',{'data':test_a}),
#     ('test_b',{'data':test_b}),
#     ('test_c',{'data':test_c})
# ])
### 单边添加
# dag.add_edge('test_a','test_b',data='a_b')
# dag.add_edge('test_b','test_c',data='b_c')
### 批量边添加
dag.add_edges_from([
                ('test_a','test_b',{'data':'a_b'}), 
                ('test_b','test_d',{'data':'b_d'}),
                ('test_a','test_c',{'data':'a_c'}),
                ('test_c','test_d',{'data':'c_d'})])
print(dag.edges['test_a','test_b']['data'])
dag.edges['test_a','test_b']['data'] = 'a_b_00'
print('@@@@@@@',dag.edges['test_a','test_b']['data'])
### 拓扑排序
toposort = list(nx.topological_sort(dag))
print(toposort)
### 获取临近节点
node_list_pre = dag.predecessors(n='test_c')
node_list_back = dag.successors(n='test_c')
print(list(node_list_pre),list(node_list_back))
### 获取临近边
edge_list_pre = dag.in_edges(nbunch='test_c')
edge_list_back = dag.out_edges(nbunch='test_c')
print(list(edge_list_pre),list(edge_list_back))
### 获取临近边上的数据
node_data_input = dag.edges[list(edge_list_pre)[0]]['data']
print(node_data_input)
def inplace_func(data):
    return data
def execute(dag,init_data):
    # ### 执行顺序首部加入占位函数
    # dag.add_node('inplace_func',data=inplace_func)
    toposort = list(nx.topological_sort(dag))
    # toposort.insert(0,'inplace_func')
    print(toposort)
    for tmp_node_name in toposort:
        print('---',tmp_node_name)
        ### 获取运行节点
        tmp_func = dag.nodes[tmp_node_name]['data']
        ### 进行参数收集,使用inspect-signature技术
        tmp_inspect = signature(tmp_func)
        tmp_params_list = list(tmp_inspect.parameters.keys())
        # print(tmp_params_list[0],type(tmp_params_list[0]))
        # ### 获取前一个边
        # tmp_edge_list_pre = dag.in_edges(nbunch=tmp_node_name)
        # ### 获取前一个边的数据
        # tmp_predata = dag.edges[list(tmp_edge_list_pre)[0]]['data']
        # ### 执行当前函数
        # tmp_backdata = tmp_func.__call__(tmp_predata)
        # ### 获取后一个边
        # tmp_edge_list_back = dag.out_edges(nbunch=tmp_node_name)
        # ### 放入后一个边的数据
        # dag.edges[list(tmp_edge_list_back)[0]]['data'] = tmp_backdata
    return dag

final_dag = execute(dag=dag,init_data=10)


### 运行加载的函数
import pandas as pd
df = pd.DataFrame()
df['tmp'] = [1,2,3]
df['tmp_a'] = [4,5,6]
tmp_result = eval('df')
print(tmp_result)
###
exec('tmp_{} = 200'.format('b'))
print(tmp_b)
### 获取函数名称
print(test_a.__name__)




