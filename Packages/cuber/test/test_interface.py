### 载入程序包
from cuber.interface import Cube
import time


### cuber实例创建
cuber = Cube(cuber_runner='ray',
             cuber_runner_address='ray://192.168.1.51:10001',
             cuber_scheduler='kahn')


### 创建cuber控制器
cuber_controller = cuber.get_cuber_controller()


### 注册目标函数到指定cuber控制器
@cuber_controller.register(controller_obj=cuber_controller)
def test_a():
    time.sleep(10)
    print(2)
    return 'a'

@cuber_controller.register(controller_obj=cuber_controller)
def test_aa():
    time.sleep(10)
    print(2)
    return 'aa'

@cuber_controller.register(controller_obj=cuber_controller)
def test_b():
    time.sleep(10)
    print(2)
    return 'b'

@cuber_controller.register(controller_obj=cuber_controller)
def test_bb():
    time.sleep(10)
    print(2)
    return 'bb'

@cuber_controller.register(controller_obj=cuber_controller)
def test_c():
    time.sleep(10)
    print(2)
    return 'c'

@cuber_controller.register(controller_obj=cuber_controller)
def test_cc():
    time.sleep(10)
    print(2)
    return 'cc'

@cuber_controller.register(controller_obj=cuber_controller)
def test_d():
    time.sleep(10)
    return 'd'


### 注册目标函数依赖关系到指定cuber控制器
test_a >> test_b >> test_c >> test_d
test_aa >> test_b >> test_d
test_bb >> test_c >> test_d
test_cc >> test_d


### 展示节点和边情况
print('~~~~~~',cuber_controller.get_graph_obj())
print('------',cuber_controller.show_nodes())
print('======',cuber_controller.show_edges())


### 使用二级统一API
time_start = time.time()
exec_result = cuber_controller.execute()
time_end = time.time()
print('============================== Parallel function running',time_end - time_start)


### 串行函数运行
time_start = time.time()
test_a()
test_aa()
test_bb()
test_cc()
test_b()
test_c()
test_d()
time_end = time.time()
print('============================== Serial function operation',time_end - time_start)


