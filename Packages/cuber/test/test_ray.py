from cuber.actuator.actuator_realization import *
from cuber.runner.rayengine import *
# import ray
import time



runner = RayRunner(address='ray://192.168.1.51:10001')

print(runner)
# ray.init(address='ray://192.168.1.63:10001')

with runner.runner_context:
    @ray.remote
    def f_sleep(x):
        time.sleep(2)
        return x

    def sleep(x):
        time.sleep(2)
        return x


    tmp_x = sleep(4)
    futures = f_sleep.remote(5)
    tmp_x_ray = ray.get(futures)
    print(tmp_x,tmp_x_ray,runner.init_success)

# @ray.remote
# def f_sleep(x):
#     time.sleep(2)
#     return x

# def sleep(x):
#     time.sleep(2)
#     return x

# tmp_x = sleep(6)
# futures = f_sleep.remote(7)
# tmp_x_ray = ray.get(futures)
# print(tmp_x,tmp_x_ray,runner.init_success)


