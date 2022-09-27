### 载入程序包
from cuber.actuator.actuator_realization import *


### 创建cuber控制器
cuber_controller = Controller(runner='ray',scheduler='scheduler')


### 注册目标函数到指定cuber控制器
@cuber_controller.register(controller_obj=cuber_controller)
def test_a(a):
    return a + 2

@cuber_controller.register(controller_obj=cuber_controller)
def test_aa(aa):
    return aa + 2

@cuber_controller.register(controller_obj=cuber_controller)
def test_b(b):
    return b + 2

@cuber_controller.register(controller_obj=cuber_controller)
def test_bb(bb):
    return bb + 2

@cuber_controller.register(controller_obj=cuber_controller)
def test_c(c):
    return c + 2

@cuber_controller.register(controller_obj=cuber_controller)
def test_cc(cc):
    return cc + 2

@cuber_controller.register(controller_obj=cuber_controller)
def test_d(d):
    return d + 2


### 注册目标函数依赖关系到指定cuber控制器
test_a >> test_b >> test_c >> test_d
test_aa >> test_b >> test_d
test_bb >> test_c >> test_d
test_cc >> test_d


### 展示节点和边情况
print('~~~~~~',cuber_controller.get_graph_obj())
print('------',cuber_controller.show_nodes())
print('======',cuber_controller.show_edges())


### 展示DAG图情况
# cuber_controller.draw()


### 调用目标函数
tmp_func = cuber_controller.get_function_obj(function_name='test_aa')
print(tmp_func(10))


