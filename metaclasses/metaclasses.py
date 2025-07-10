# def commission(f):
#     def w(b, a):
#         if b < a + 1:
#             return "u have no money"
#         return f(b - 1, a)
#     return w

# @commission
# def transaction(b, a):
#     return b - a

# print(transaction(10, 5))
# print(transaction(5, 5))  

# class UnderscoreMeta(type):
#     def __new__(cls, name, bases, ns):
#         for n, v in ns.items():
#             if callable(v) and not n.startswith('_'):
#                 raise ValueError('method not ok')
#         return super().__new__(cls, name, bases, ns)


# class Good(metaclass=UnderscoreMeta):
#     def _foo(self):
#         return 'ok'


# try:
#     class Bad(metaclass=UnderscoreMeta):
#         def _foo(self):
#             return 'ok'
#         def bar(self):
#             return 'nope'
#     print('Bad შექმნილია')
# except ValueError as e:
#     print('ERR:', e)
