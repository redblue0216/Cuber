
import yaml
import networkx as nx
import functools
from types import MethodType





class TestScheduler(object):

    def __init__(self,name):
        self.name = name
        self.dag = nx.DiGraph()
        
    # scheduler_name = self.
    ### 数据化类
    class ClassedFunction(object):

        def __init__(self,func): ### 装饰器内取调度器变量名称是技术难点
            self.func = func
            self.testscheduler = 'tmp_scheduler'# self.get_testshceduler()
            exec('{}.dag.add_node(self.func.__name__,data=self.func)'.format(self.testscheduler))
            print('add node {} well done'.format(self.func.__name__))
            functools.wraps(func)(self)
            
        def get_testshceduler(self):
            print('------get cuber config name')
            cuber_yaml = open('cuber_config.yaml')
            cuber_config = yaml.load(stream=cuber_yaml,Loader=yaml.FullLoader)
            testscheduler = cuber_config['cuber_scheduler']
            print('@@@@@@@@',type(testscheduler))
            return testscheduler

        def __call__(self,*args,**kwargs):
            # tmp_scheduler = kwargs['scheduler']
            # tmp_scheduler.dag.add_node(self.func.__name__,data=self.func)
            # print('add node {} well done'.format(self.func.__name__))
            return self.func(*args,**kwargs)
            # return self.__wrapper(*args,**kwargs)

        def __get__(self,instance,cls):
            if instance is None:
                return self
            else:
                return MethodType(self,instance)

        def __rshift__(self,other):
            exec('print({}.dag.nodes)'.format(self.testscheduler))
            print('@@@@@@@@2')
            print(self.func.__name__,other.func.__name__)
            a = self.func.__name__
            b = other.func.__name__
            print('#######')
            exec("{}.dag.add_edge('{}','{}',data='data')".format(self.testscheduler,a,b))
            print('this is a __rshift__ test',self.func.__name__,other.func.__name__)
            

tmp_scheduler = TestScheduler('test')

@tmp_scheduler.ClassedFunction
def test_d(d):
    print('~~~~~~~~d test')
    return d + 4

@tmp_scheduler.ClassedFunction
def test_e(e):
    return e + 5

test_d >> test_e

# print(test_d(1))
print('$$$$$$$$$$$$$$$')
print(tmp_scheduler.dag.nodes)
print('$$$$$$$$$$$$$$$$$')
print(tmp_scheduler.dag.edges)

# tmp_scheduler.dag.
# class outer(object):
#     def __init__(self,name):
#         self.name = name

#     def run_outer(self):
#         print('run outer')

#     class inner(object):
#         def __init__(self,name):
#             self.name = name

#         def run_inner(self):
#             print(outer.name)


# tmp_out = outer('outer')
# tmp_in = tmp_out.inner('inner')
# tmp_in.run_inner()


# ### 通过装饰器技术将目标函数加载进dag
# class Test(object):
    
#     def __init__(self,name):
#         self.name = name
#         self.dag = nx.DiGraph() ### cuber中为scheduler调度管理器
    
#     def decorator(self,func):

#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             result = func(*args,**kwargs)
#             print('decorator starting!')
#             self.dag.add_node(func.__name__,data=func)
#             return result
#         return wrapper


#     def __rshift__(self,other):

#         print('this is a __rshift__ test',self.name,other.name)

# test = Test(name='test')
# a = Test(name='a')
# b = Test(name='b')
# a >> b

# @test.decorator
# def test_a(a):
#     return a + 1

# @test.decorator
# def test_b(b):
#     return b + 2 

# def test_c(c):
#     return c + 3


# # decorator.dag.add_node(test_func.__name__,data=test_func)
# # print('decorator================',test_func(1))
# print('--------',test.dag)


# def __rshift__(self,other):

#     print('this is a __rshift__ test',self.__name__,other.__name__)


# def set_test(self):

#     print('test methodtype')


# test_a.__rshift__ = MethodType(__rshift__,test_a)
# test_b.__rshift__ = MethodType(__rshift__,test_b)
# test_c.set_test = MethodType(set_test,test_c)
# print(test_c.__dict__)
# print(dir(test_c))



