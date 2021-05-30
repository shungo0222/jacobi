class Jacobi(object):
    """
    Class of Jacobi
    Solve "ax = b"

    Parameters
    ----------
    a : list
        the coefficient matrix
    b : list
        the right side of equatinos
    initial_value : int
        the initial value of x
    threshold : float
        the allowable error
    """

    def __init__(self, a, b, initial_value=0, threshold=1e-3):
        self.a = a
        self.b = b
        self.threshold = threshold
        self.x = [initial_value] * len(b)
        self.length = len(b)
    
    def calculate(self, detail=False):
        count = 0
        while True:
            count += 1
            for i in range(self.length):
                right_side_sum = 0
                for j in range(self.length):
                    if i != j:
                        right_side_sum += -self.a[i][j] * self.x[j]
                right_side_sum += self.b[i]
                tmp = self.x[i]
                self.x[i] = right_side_sum / self.a[i][i]

                if i == 0:
                    max_error = abs(self.x[i] - tmp)
                else:
                    max_error = max(max_error, abs(self.x[i] - tmp))
            
            if detail:
                print('-'*5, 'count'+str(count), '-'*5)
                print('x =', *self.x)
            
            if max_error <= self.threshold:
                break
    
    def get_ans(self):
        return self.x