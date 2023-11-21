def magic_calculation(a, b):
    result = 0
    
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except Exception as e:
            print(e)
            raise
        
        result = result + (a ** b) / i
    
    result = result + a + b
    return result