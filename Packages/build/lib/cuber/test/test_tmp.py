def test(method,name = None,data = None,*args,**kwargs):
    if method == 1:
        print(name)
    elif method == 2:
        print(name,data)


test(method=2,name='test',data='data')