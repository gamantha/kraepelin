import random

class KraepelinService():
    """
    All kraepelin data logic service.
    """

    def prepare_test_data(self, size):
        """
        Prepare all test data
        @param size - size array [x, y]
        return dict
        """
        result = []
        for i in range(int(size[0])):
            temp_arr = []
            for j in range(int(size[1])):
                temp_arr.append(random.randint(1, 10))
            result.append(temp_arr)
        return result

    def asess_test_data(self):
        """
        Asess test result.
        """
        return True
    
    