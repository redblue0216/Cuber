# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个有限状态机的管理类，主要功能提供对象的状态管理，主要技术基于transitions实现的有限状态机
"""
模块介绍
-------

这是一个有限状态机的管理类，主要功能提供对象的状态管理，主要技术基于transitions实现的有限状态机

设计模式：

    （1）  无 

关键点：    

    （1）FSM
    
主要功能：            

    （1）管理对象状态

使用示例
-------


类说明
------

"""



####### 载入程序包 ##############################################################################
################################################################################################



from transitions import Machine



####### 有限状态机的管理类 #######################################################################
### 功能：                                                                                    ###
### (1) 管理对象状态                                                                           ###
### 技术：                                                                                    ###
### (1) FSM                                                                                  ###
################################################################################################



####### 有限状态机管理类 ############################################################################
###################################################################################################



class FiniteStateMachine(object):
    '''
    类介绍：

        这是一个有限状态机的管理类，主要功能提供对象的状态管理，主要技术基于transitions实现的有限状态机
    '''


    states = ['ready','operating','done']
    transitions = [
        {'trigger':'start','source':'ready','dest':'operating'},
        {'trigger':'exit','source':'operating','dest':'done'}
    ]


    def __init__(self):
        '''
        属性功能：

            定义一个初始化方法，用于创建有限状态机实例

        参数：
            machine (object): 有限状态机实例
        '''

        self.machine = Machine(model = self,
                               states = FiniteStateMachine.states,
                               transitions = FiniteStateMachine.transitions,
                               initial = 'ready')



##################################################################################################
##################################################################################################   


