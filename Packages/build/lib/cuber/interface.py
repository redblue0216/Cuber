# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个集成学习cuber接口类，主要功能提供cuber功能接入
"""
模块介绍
-------

这是一个集成学习cuber接口类，主要功能提供cuber功能接入

设计模式：

    （1）  无 

关键点：    

    （1）无

主要功能：            

    （1）cuber功能接入

使用示例
-------


类说明
------

"""



####### 载入程序包 ##############################################################################
################################################################################################



from cuber.actuator.actuator_realization import *
from cuber.runner.rayengine import *
from cuber.manager.dispatch import *



####### cuber功能接口类 ###########################################################################
### 功能：                                                                                     ###
### （1）cuber功能接入                                                                          ###
##################################################################################################



####### cuber功能接口类 ############################################################################
###################################################################################################



class Cube(object):
    '''
    类介绍：

        这是一个cuber的接口类，主要用于功能接入，是cuber的第三级API
    '''


    def __init__(self,
                 cuber_runner=None,
                 cuber_runner_address=None,
                 cuber_scheduler=None,
                 *args,**kwargs):
        '''
        属性功能：

            定义一个初始化方法，用于创建cuber控制引擎，并向其加载计算引擎和调度引擎

        参数：
            cuber_runner (str): cuber计算引擎名称
            cuber_runner_address (str): cuber计算引擎地址,eg.'ray://192.168.1.51:10001'
            cuber_scheduler (str): cuber调度引擎名称
        '''
        
        if cuber_runner == 'ray':
            self.cuber_runner = RayRunner(address=cuber_runner_address)
        else:
            print('No cuber runer!')
        if cuber_scheduler == 'kahn':
            self.cuber_scheduler = Scheduler()
        else:
            print('No cuber scheduler!')
        self.cuber_controller = Controller(runner=self.cuber_runner,scheduler=self.cuber_scheduler)

    
    def get_cuber_controller(self):
        '''
        方法功能:

            定义一个获得cuber控制器的方法

        参数：
            无

        返回：
            cuber_controller (object): cuber控制器对象实例
        '''

        cuber_controller = self.cuber_controller
        return cuber_controller



#############################################################################################################
#############################################################################################################


