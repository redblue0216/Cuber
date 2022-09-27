### 载入程序包
from cuber.actuator.actuator_realization import *
from cuber.runner.rayengine import *
from cuber.manager.dispatch import *
import time



### 创建计算引擎和调度引擎，控制引擎内置于控制器实例中
cuber_runner = RayRunner(address='ray://192.168.1.51:10001')
cuber_scheduler = Scheduler()


### 创建cuber控制器
cuber_controller = Controller(runner=cuber_runner,scheduler=cuber_scheduler)


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

### 使用一级分散API

# ### 运行kahn算法
# kahnclassification_list = cuber_controller.kahnclassification_algorithm()
# print(kahnclassification_list)


# ### 初始化工作队列，使用kahn算法
# init_job_queue_result = cuber_controller.init_job_queue_with_kahn()
# print(len(cuber_controller.scheduler.job_queue),cuber_controller.scheduler.job_queue)


# ### 使用kahn调度算法
# dispath_iter_result = cuber_controller.dispath_algorithm_with_kahn()
# print(dispath_iter_result)


# ### 使用调度算法生成的生成器
# time_start = time.time()
# for tmp_dispath in dispath_iter_result:
#     print('****',tmp_dispath)
#     cuber_controller.execute_algorithm_with_ray(tmp_dispath)
# time_end = time.time()
# print('============================== Parallel function running',time_end - time_start)


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


