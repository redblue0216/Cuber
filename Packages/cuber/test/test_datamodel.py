from cuber.model.mixin import *


def test_func(a):
    print('this is a test function!')
    print(a)


tmp_data = DataModelMixin(name='test_func',params={'a':100},obj=test_func)
tmp_data.obj.__call__(**tmp_data.params)


