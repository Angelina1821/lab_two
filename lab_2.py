def hannoi(n, odin, tri, prom):
    if n == 1:
        print('Переместить диск с', odin, 'на', tri)
        return
    hannoi(n-1, odin, prom, tri)
    print('Переместить диск с', odin, 'на', tri)
    hannoi(n-1, prom, tri, odin)

hannoi(5, 1, 3, 2)