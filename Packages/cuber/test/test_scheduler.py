
from cuber.actuator.actuator_realization import *
import networkx as nx


controller = Controller(runner='ray',scheduler='scheduler')


### add_node测试
controller.add_node(method='single',node_name='test_a',data_obj='data_a')
print(controller.manager.obj.nodes,controller.manager.obj)
controller.add_node(method='batch',data_dict_list=[('test_b',{'data_obj':'data_b'}),
                                                   ('test_c',{'data_obj':'data_c'}),
                                                   ('test_d',{'data_obj':'data_d'}),
                                                   ('test_aa',{'data_obj':'data_aa'})])
print(controller.manager.obj.nodes,controller.manager.obj)


### add_edge测试
controller.add_edge(method='single',start_node_name='test_a',end_node_name='test_b',data_obj='data_a_b')
print(controller.manager.obj.edges,controller.manager.obj)
controller.add_edge(method='batch',data_dict_list=[('test_b','test_c',{'data_obj':'data_b_c'}),
                                                   ('test_c','test_d',{'data_obj':'data_c_d'}),
                                                   ('test_a','test_c',{'data_obj':'data_a_c'}),
                                                   ('test_b','test_aa',{'data_obj':'data_b_aa'}),
                                                   ('test_aa','test_d',{'data_obj':'data_aa_d'})])
print(controller.manager.obj.nodes,controller.manager.obj)


### modify_node测试
print(controller.manager.obj.nodes['test_a']['data'])
controller.modify_node(node_name='test_a',data_obj='data_e')
print(controller.manager.obj.nodes['test_a']['data'])


### modify_edge测试
print(controller.manager.obj.edges['test_a','test_b'])
controller.modify_edge(start_node_name='test_a',end_node_name='test_b',data_obj='data_a_b_e')
print(controller.manager.obj.edges['test_a','test_b'])


# ### remove_node测试
# print(controller.manager.obj.nodes)
# # controller.remove_node(method='single',node_name='test_d')
# controller.remove_node(method='batch',nodes_name_list=['test_d'])
# print(controller.manager.obj.nodes)


# ### remove_edge测试
# print(controller.manager.obj.edges)
# # controller.remove_edge(method='single',start_node_name='test_b',end_node_name='test_c')
# controller.remove_edge(method='batch',edges_name_list=[('test_b','test_c')])
# print(controller.manager.obj.edges)


### query_node测试
node_query_result = controller.query_node(node_name='test_a')
print(node_query_result)


### query_edge测试
edge_query_result = controller.query_edge(start_node_name='test_a',end_node_name='test_b')
print(edge_query_result)


### get_node_neighbor测试
nodes_list = controller.get_node_neighbor(node_name='test_b',direction='forward')
print(nodes_list)


### get_edge_neighbor测试
edges_list = controller.get_edge_neighbor(node_name='test_b',direction='forward')
print(edges_list)


### get_node_attributes测试
node_attr_data = controller.get_node_attributes(node_name='test_a',attr_name='data')
print(node_attr_data)


### get_edge_attributes测试
edge_attr_data = controller.get_edge_attributes(start_node_name='test_a',end_node_name='test_b',attr_name='data')
print(edge_attr_data)

### toposort_algorithm测试
toposort_list = controller.toposort_algorithm()
print(toposort_list)


### kahnclassification_list测试
kahnclassification_list = controller.kahnclassification_algorithm()
print(kahnclassification_list)


# ### graph_draw测试
# controller.draw()