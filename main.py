from jacobi import Jacobi

def main():
    # 50x + 2y + z = 69.4
    # -x + 20y - 2z = 45.91
    # 5x + y + 10z = 26.99
    
    a = [[50, 2, 1], [-1, 20, -2], [5, 1, 10]]
    b = [69.4, 45.91, 26.99]
    
    jacobi = Jacobi(a, b)
    jacobi.calculate(True)
    x, y, z = jacobi.get_ans()
    print('Answer')
    print(f'x = {x}, y = {y}, z = {z}')
    
    print('Check')
    print('50x + 2y + z =', 50*x + 2*y + z)
    print('-x + 20y - 2z =', -x + 20*y - 2*z)
    print('5x + y + 10z =', 5*x + y + 10*z)

if __name__ == '__main__':
    main()