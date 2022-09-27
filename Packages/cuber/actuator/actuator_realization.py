# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个集成学习计算图控制类，主要功能提供计算图DAG的管理，计算引擎管理和调度管理。主要技术基于Networkx的DAG技术，基于Ray的计算环境，装饰器技术和运算符重载
"""
模块介绍
-------

这是一个集成学习计算图控制类，主要功能提供计算图DAG的管理，计算引擎管理和调度管理。主要技术基于Networkx的DAG技术，基于Ray的计算环境，装饰器技术和运算符重载

设计模式：

    （1）  无 

关键点：    

    （1）装饰器
    
    （2）运算符重载

主要功能：            

    （1）计算图管理

    （2）计算引擎管理

    （3）调度管理

使用示例
-------


类说明
------

"""



####### 载入程序包 ##############################################################################
################################################################################################



import matplotlib.pyplot as plt
import networkx as nx
import ray
import functools
from types import MethodType
from cuber.actuator.actuator_meta import * 



####### 集成学习计算图控制实现类 ##################################################################
### 功能：                                                                                    ###
### (1) 计算图管理                                                                            ###
### (2) 计算引擎管理                                                                          ###
### (3) 调度管理                                                                              ###
### 技术：                                                                                    ###
### (1) 装饰器                                                                                ###
### (2) 运算符重载                                                                            ###
################################################################################################



####### 集成学习计算图控制实现类 ##################################################################
#################################################################################################



class Controller(metaclass = ControllerMeta):
    '''
    类介绍：

        这是一个集成学习计算图控制类，主要功能提供计算图DAG的管理，计算引擎管理和调度管理。主要技术基于Networkx的DAG技术，基于Ray的计算环境，装饰器技术和运算符重载
    '''


    def __init__(self,runner,scheduler):
        '''
        属性功能：

            定义一个初始属性方法，主要用于创建控制对象时加载计算引擎和调度引擎

        参数：
            dag (object): DAG图管理对象
            runner (object): 计算引擎对象
            scheduler (object): 调度引擎对象 
        '''

        self.runner = runner
        self.scheduler = scheduler


    def add_node(self,method='single',node_name=None,data_obj=None,data_dict_list=None,*args,**kwargs):
        '''
        方法功能：

            定义一个添加节点的方法

        参数：
            node_name (str): 节点名称
            data_obj (obj): 节点数据对象
            method (str): 添加方式
            data_dict_list (list): 数据字典列表

        返回:
            result (str): 返回结果文本
        '''

        if method == 'single':
            self.manager.obj.add_node(node_name,data=data_obj)
        elif method == 'batch':
            self.manager.obj.add_nodes_from(data_dict_list)
        result = 'Algorithm node add well done!'
        print(result)
        return result


    def add_edge(self,method='single',start_node_name=None,end_node_name=None,data_obj=None,data_dict_list=None,*args,**kwargs):
        '''
        方法功能：

            定义一个添加边的方法

        参数:
            start_node_name (str): 开始节点名称
            end_node_name (str): 结束节点名称
            data_obj (object): 节点数据对象
            method (str): 添加方式
            data_dict_list (list): 数据字典列表
        返回:
            result (str): 返回结果文本
        '''

        if method == 'single':
            self.manager.obj.add_edge(start_node_name,end_node_name,data=data_obj,*args,**kwargs)
        elif method == 'batch':
            self.manager.obj.add_edges_from(data_dict_list)
        result = 'Algorithm edge add well done!'
        print(result)
        return result


    def modify_node(self,node_name=None,data_obj=None,*args,**kwargs):
        '''
        方法功能：

            定义一个修改节点的方法

        参数:
            node_name (str): 节点名称
            data_obj (object): 节点数据对象

        返回：
            result (str): 返回结果文本
        '''

        self.manager.obj.nodes[node_name]['data'] = data_obj
        result = 'Algorithm node modify well done!'
        print(result)


    def modify_edge(self,start_node_name=None,end_node_name=None,data_obj=None,*args,**kwargs):
        '''
        方法功能：

            定义一个修改边的方法

        参数:
            start_node_name (str): 开始节点名称
            end_node_name (str): 结束节点名称
            data_obj (object): 节点数据对象

        返回：
            result (str): 返回结果文本
        '''

        self.manager.obj.edges[start_node_name,end_node_name]['data'] = data_obj
        result = 'Algorothm edge modify well done!'
        print(result)


    def remove_node(self,method='single',node_name=None,nodes_name_list=None,*args,**kwargs):
        '''
        方法功能：

            定义一个删除节点的方法

        参数：
            method (str): 删除方式
            node_name (str): 节点名称
            nodes_name_list (list): 节点名称列表

        返回：
            result (str): 返回结果文本
        '''

        if method == 'single':
            self.manager.obj.remove_node(node_name)
        elif method == 'batch':
            self.manager.obj.remove_nodes_from(nodes_name_list)
        result = 'Algorithm node remove well done!'
        print(result)
        

    def remove_edge(self,method='single',start_node_name=None,end_node_name=None,edges_name_list=None,*args,**kwargs):
        '''
        方法功能：

            定义一个删除边的方法

        参数：
            method (str): 删除方式
            edge_name (str): 边名称
            edges_name_list (list): 边名称列表

        返回：
            result (str): 返回结果文本
        '''

        if method == 'single':
            self.manager.obj.remove_edge(start_node_name,end_node_name)
        elif method == 'batch':
            self.manager.obj.remove_edges_from(edges_name_list)
        result = 'Algorithm edge remove well done!'
        print(result)


    def query_node(self,node_name=None,*args,**kwargs):
        '''
        方法功能：

            定义一个查询图节点的方法

        参数：
            node_name (str): 节点名称

        返回：
            data_dict (dict): 数据字典
        '''

        data_dict = self.manager.obj.nodes[node_name]
        print('Algorithm node query well done!')
        return data_dict


    def query_edge(self,start_node_name=None,end_node_name=None,*args,**kwargs):
        '''
        方法功能：

            定义一个查询图边的方法

        参数：
            start_node_name (str): 开始节点名称
            end_node_name (str): 结束节点名称

        返回：
            data_dict (str): 数据字典
        '''

        data_dict = self.manager.obj.edges[start_node_name,end_node_name]
        print('Algorithm edge query well done!')
        return data_dict


    def get_node_neighbor(self,node_name=None,direction=None,*args,**kwargs):
        '''
        方法功能：

            定义一个访问目标节点邻居节点的方法

        参数：
            node_name (str): 节点名称
            direction (str): 访问方向

        返回：
            nodes_list (list): 节点列表
        '''

        if direction == 'backward':
            nodes_list = list(self.manager.obj.successors(n=node_name))
        elif direction == 'forward':
            nodes_list = list(self.manager.obj.predecessors(n=node_name))
        print('Algorithm get node neighbor well done!')
        return nodes_list 


    def get_edge_neighbor(self,node_name=None,direction=None,*args,**kwargs):
        '''
        方法功能：

            定义一个访问目标节点邻居边的方法

        参数：
            node_name (str): 节点名称
            direction (str): 访问方向

        返回：
            edges_list (list): 边列表
        '''

        if direction == 'backward':
            edges_list = list(self.manager.obj.out_edges(nbunch=node_name))
        elif direction == 'forward':
            edges_list = list (self.manager.obj.in_edges(nbunch=node_name))
        print('Algorithm get edge neighbor well done!')
        return edges_list


    def get_node_attributes(self,node_name=None,attr_name=None,*args,**kwargs):
        '''
        方法功能：

            定义一个获取节点属性的方法
        
        参数：
            node_name (str): 节点名称
            attr_name (str): 属性名称

        返回：
            atrr_data (object): 属性数据
        '''

        attr_data= self.manager.obj.nodes[node_name][attr_name]
        print('Algorithm node get attributes well done!')
        return attr_data


    def get_edge_attributes(self,start_node_name=None,end_node_name=None,attr_name=None,*args,**kwargs):
        '''
        方法功能：

            定义一个获取边属性的方法

        参数：
            start_node_name (str): 开始节点名称
            end_node_name (str): 结束节点名称
            attr_name (str): 属性名称

        返回：
            attr_data (object): 属性数据
        '''

        attr_data = self.manager.obj.edges[start_node_name,end_node_name][attr_name]
        print('Algorithm edge get attributes well done!')
        return attr_data


    def get_function_obj(self,function_name):
        '''
        方法功能：

            定义一个获取函数对象的方法

        参数：
            function_name (str): 函数名称

        返回：
            function_obj (object): 函数对象
        '''

        function_obj = self.manager.obj.nodes[function_name]['data']
        print('Algorithm function object get well done!')
        return function_obj


    def show_nodes(self):
        '''
        方法功能：

            定义一个展示图管理器的节点情况的方法

        参数：
            无

        返回：
            show_nodes_list (List): 展示节点列表
        '''

        show_nodes_list = self.manager.obj.nodes
        print('Algorithm show nodes well done!')
        return show_nodes_list


    def show_edges(self):
        '''
        方法功能：

            定义一个展示图管理器的边情况的方法

        参数：
            无

        返回：
            show_edges_list (List): 展示边列表
        '''

        show_edges_list = self.manager.obj.edges
        print('Algorithm show edges well done!')
        return show_edges_list


    def get_graph_obj(self):
        '''
        方法功能：

            定义一个获取图对象的方法

        参数：
            无

        返回：
            graph_obj (object): 图对象，基于networkx技术
        '''

        graph_obj = self.manager.obj
        print('Algorithm get graph object well done!')
        return graph_obj


    def toposort_algorithm(self):
        '''
        方法功能：

            定义一个拓扑排序的方法

        参数：
            无

        返回：
            toposort_list (list): 拓扑排序列表
        '''

        toposort_list = list(nx.topological_sort(self.manager.obj))        
        print('Algorithm toposort well done!')
        return toposort_list


    def kahnclassification_algorithm(self):
        '''
        方法功能：

            定义一个DAG图分层算法

        参数：
            无

        返回：
            kahnclassification_list
        '''
        
        ### 运行kahn分级算法得到运行节点优先级分层
        kahnclassification_list = list(nx.topological_generations(self.manager.obj))
        print('Algorithm kahn run well done!')
        return kahnclassification_list


    def draw(self):
        '''
        方法功能：

            定义一个展示图例的方法

        参数：
            无

        返回：
            无
        '''

        nx.draw(self.manager.obj,with_labels=True)
        plt.draw()
        plt.show()


    def register(self,controller_obj):
        '''
        方法功能：

            定义一个注册函数的装饰器方法，使用带参数的装饰器函数技术。

        参数：
            controller_obj (object): 控制器对象

        返回：
            decorate (function): 装饰器函数对象
        '''


        def decorate(func):
            '''
            方法功能：

                定义一个装饰器函数

            参数：
                func (function): 目标装饰函数

            返回：
                extand_func (object): 扩展后的函数对象
            '''



            class Extand(object):
                '''
                类介绍：

                    这是一个注册函数类，主要用于将目标函数注册到图管理器中
                '''

                
                def __init__(self,func):
                    '''
                    属性功能：

                        定义一个初始化注册函数类的方法，主要用于将函数注册到图管理器中

                    参数：
                        func (object): 函数对象
                    '''

                    ### 将目标函数放入extand属性中
                    self.func = func
                    ### 获取目标函数名称和对象
                    tmp_node_name = func.__name__
                    tmp_data_obj = func
                    ### 将目标函数注册到控制器上
                    controller_obj.add_node(method='single',
                                            node_name=tmp_node_name,
                                            data_obj=tmp_data_obj)
                    # print(controller_obj.manager.obj)
                    # print(controller_obj.manager.obj.nodes)
                    ### 引用目标函数属性
                    functools.wraps(func)(self)
                    print('Algorithm {} node added to the graph manager well done!'.format(self.func.__name__))


                def __call__(self,*args,**kwargs):
                    '''
                    方法功能：

                        重载一个实例调用的魔法方法

                    参数：
                        无

                    返回：
                        函数运行结果
                    '''

                    return self.func(*args,**kwargs)


                def __get__(self,instance,cls):
                    '''
                    方法功能：

                        重载一个函数实例创建获得方法

                    参数：
                        instance (object): 所属实例
                        cls (object): 所属类

                    返回：
                        self (object): 函数对象实例本身
                    '''

                    if instance is None:
                        return self
                    else:
                        return MethodType(self,instance)


                def __rshift__(self,other):
                    '''
                    方法功能：

                        重载一个右移位运算符，主要用于添加算法节点的边，构建算法依赖关系。

                    参数：
                        self (object): 自身函数对象实例
                        other (object): 另一个函数对象实例

                    返回：
                        other (object): 另一个函数对象实例，为了连续使用rshift操作符，只能将结束节点依次传递
                    '''

                    tmp_start_node_name = self.func.__name__
                    tmp_end_node_name = other.func.__name__
                    controller_obj.add_edge(method='single',
                                           start_node_name=tmp_start_node_name,
                                           end_node_name=tmp_end_node_name,
                                           data_obj='{} to {}'.format(tmp_start_node_name,tmp_end_node_name))
                    print('Algorithm edge {} to {} added to the graph well done!'.format(tmp_start_node_name,tmp_end_node_name))
                    return other



            ### 使用Extand扩展目标函数对象，并返回扩展后的目标函数对象
            extand_func = Extand(func=func)

            return extand_func

        return decorate

    ### 以下方法分为初始化任务队列、调度、执行三大类，后续的总执行方法具体由初始化任务队列、调度和执行各个小函数的对应版本组合而成
    def init_job_queue_with_kahn(self):
        '''
        方法功能：

            定义一个初始化优先级调度队列的方法,使用kahn算法

        参数：
            无

        返回：
            result (str): 返回结果文本
        '''

        ### 运行kahn分级算法得到运行节点优先级分层
        kahnclassification_list = self.kahnclassification_algorithm()
        ### 将嵌套list中的二级元素依据优先级加入到shceduler中，使用list迭代器
        for tmp_kahn_item in kahnclassification_list:
            self.scheduler.job_queue.append(tmp_kahn_item)
        result = 'Init job queue well done!'
        print(result)
        return result


    def dispath_algorithm_with_kahn(self):
        '''
        方法功能：

            定义一个使用Kahn算法的调度方法，此处使用yield技术返回一个生成器

        参数：
            无

        返回：
            无
        '''

        iter_num = len(self.scheduler.job_queue)
        for i in range(0,iter_num,1):
            run_list = self.scheduler.job_queue.popleft()
            print('Algorithm run task {} generate well done!'.format(run_list))
            yield run_list
        

    def execute_algorithm_with_ray(self,run_list):
        '''
        方法功能：

            定义一个使用ray计算引擎的执行方法,包括收集参数，执行，推送结果三大步骤

        参数：
            run_list (list): 单个运行任务列表

        返回：
            无
        '''

        ### 根据run_list中的执行名称获取函数对象
        run_obj_list = [self.get_function_obj(function_name=tmp_run) for tmp_run in run_list]
        ### 为了循环调用ray，一定不要开启ray运行上下文环境
        # with self.runner.runner_context:
        ### 注册函数到ray
        ray_remote_list = []
        for tmp_run_obj in run_obj_list:
            ray_remote_list.append(ray.remote(tmp_run_obj))
        ### 根据函数对象，收集参数
        ### 此处参数收集需要放到实际运行函数中，从参数的存储器上取得。(参数收集需要自己在函数中编码实现)
        ### 返回异步调用器
        ray_future_list = [tmp_ray.remote() for tmp_ray in ray_remote_list]
        ### 执行函数对象
        ray_result = ray.get(ray_future_list)
        result = 'Algorithm DAG execute well done!'
        print(result)
        ### 根据函数对象，推送结果
        ### 此处结果推送也是需要放到实际运行函数中，推送到数据存储端上。(数据存储需要自己在函数中编码实现)
        return result


    def execute(self,init_method='kahn',dispath_method='kahn',exec_method='ray'):
        '''
        方法功能：

            定义一个执行算法DAG的方法

        参数：
            cuber_controller (object): 目标控制器,此处就为实例本身self
            init_method (str): 初始化方法
            dispath_method (str): 调度方法
            exec_method (str): 运行方法

        返回：
            result (str): 返回结果文本
        '''

        ### 目标控制器,此处就为实例本身self
        cuber_controller = self
        ### 初始化工作队列
        if init_method == 'kahn':
            init_job_queue_result = cuber_controller.init_job_queue_with_kahn()
            print('init method {} execute well done!'.format(init_method))
        else:
            print('Other init methods are developing!')
        ### 使用Kahn调度算法
        if dispath_method == 'kahn':
            dispath_iter_result = cuber_controller.dispath_algorithm_with_kahn()
            print('dispath method {} execute well done!'.format(dispath_method))
        else:
            print('Other dispath methods are developing!')
        ### 使用调度算法生成的生成器
        if exec_method == 'ray':
            for tmp_dispath in dispath_iter_result:
                cuber_controller.execute_algorithm_with_ray(tmp_dispath)
            print('exec method {} execute well done!'.format(exec_method))
        else:
            print('Other exec methods are developing!')
        result = 'Algorithm DAG run well done!'
        print(result)
        return result



######################################################################################################################################
######################################################################################################################################


