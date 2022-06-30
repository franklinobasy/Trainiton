from typing import Any, Callable, Tuple, Union
import numpy as np


class Optimize:
        '''A class that helps optimize output to a function


        '''
        def __init__(self, func: Callable[[list], Union[float, int]], input: Union[list, tuple], spaces: list, output: Union[float, int]) -> None:
                '''Initialize object

                func: model or function to optimize. Requires a single list type arg
                input: Arg to the function. List or tuple type
                spaces: search space. A list of tuple element where each tuple contains a lower limit and an upper limit.
                output: initial func output. This is the value that is meant to be optimize.
                '''

                assert len(input) == len(spaces), "input and spaces must be iterables of equal length"

                self.func = func
                self.input = input #np.reshape(np.array(input), (1, -1))
                self.spaces = spaces
                self.output= output

        

        def maximize(self) -> Tuple[list, Union[int, float]]:
                '''This method finds the inputs that maximizes func
                '''

                n = len(self.input)
                
                for i in range(n):
                        temp = self.input.copy()
                        sp = self.spaces[i]
                        if not sp:
                                input[i] = temp[i]
                                continue
                        else:
                                up = sp[0]
                                down = sp[1]
                                search_space = np.linspace(up, down, 1000)
                                for j in search_space:
                                        temp[i] = j
                                        new_ouput = self.func(temp)
                                        if new_ouput > self.output:
                                                self.output = new_ouput
                                                self.input[i] = j
                                                break

                return self.input, self.output


if __name__ == '__main__':
        def f(l):
                x1 = l[0]
                x2 = l[1]
                x3 = l[2]
                x4 = l[3]
                x5 = l[4]
                return 2*x1 + 3*x2 - x3 + x4 ** 2 - x5

        input = [5, 2, 3, 0.6, -8]
        spaces = [None, (1, 4), None, (0, 1), None]
        output = 15

        p = Optimize(f, input, spaces, output)
        print(p.maximize())

                


