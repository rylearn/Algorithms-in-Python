def dispatch_dict(operator, x, y):
    func_dict = {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }
    return func_dict.get(operator, lambda: None)()

print(dispatch_dict('add', 4, 5))
print(dispatch_dict('addd', 4, 5))
