import random

class FactorsX:
        def __init__(self, variables, result):
             self._variables = variables
             self._result = result

class LogicalOperatorFactors:
    def __init__(self, cant_variables):
          self._cant = cant_variables
          self._factors = []

    def add_factors(self, factorX = FactorsX):
        assert len(factorX._variables) == self._cant , "cant of factors it's to much"
        self._factors.append(factorX)

    def get_list_of_factors(self):
         return self._factors
             
class SpLogicalOperator:
    def __init__(self, entries_factors = LogicalOperatorFactors):
        self._entries_factors = entries_factors
        self._lambda = 0.2
        self._weights = self.create_random_weights_umbral()
        self._umbral  = random.random()

    def training(self):
         #Xi * Wi + xii * Wii + S = 0
         cant_factors = len(self._entries_factors.get_list_of_factors())
         no_iteration = 1
         while True:
            percent_rate = 0
            print(f"iteration {no_iteration}")
            #iterations
            for indx, factor in enumerate(self._entries_factors.get_list_of_factors()):
                sum_variables = self.variable_times_weights(factor)
                is_active = sum_variables - self._umbral

                ecuation = ''
                current_umbral = self._umbral
                for index, weight in enumerate(self._weights):
                    ecuation += str(round(weight,2)) + 'X' + str(index) + ' + '

                is_passed = self.verify_result(is_active,factor)
                percent_rate += is_passed
                print(f"{factor._variables}  the ecuation is: {ecuation} (-{round(current_umbral,4)}) = 0, result was {round(is_active,2)}, {'passed ' if is_passed == 1 else 'FAILED'} ")
            print(f"percent of successful of iteration {no_iteration} was {(percent_rate / cant_factors) * 100} ")
            if (percent_rate / cant_factors) * 100 == 100:
                break
            no_iteration += 1

    def verify_result(self,is_active, factor):
        activation = 1 if is_active >= 0 else 0
        if activation != factor._result:
            self.correct_result(factor, activation)
            return 0
        return 1
                         
    def correct_result(self,factor,z):
        #error
        y = factor._result
        e = (y - z)
        #umbral
        diffU = -(self._lambda * e)
        new_u = self._umbral + diffU
        self._umbral = (new_u)
        #weights
        for indx in range(self._entries_factors._cant):
            diff_w = self._lambda * e * factor._variables[indx]
            self._weights[indx] = self._weights[indx] + diff_w
         
                               
    def variable_times_weights(self, factor):
        sum = 0
        for i in range(self._entries_factors._cant):
             sum += factor._variables[i] * self._weights[i]
        return sum
    

    def create_random_weights_umbral(self):
        weights  = []
        for _ in range(self._entries_factors._cant):
            weights.append(random.random())
        return weights