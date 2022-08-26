from typing import Counter


def reorderedPowerOf2(n):
        """
        :type n: int
        :rtype: bool
        """
        c = Counter([int(el) for el in str(n)])

        n, i = 0,0 
        while n<10**9:
            n = 2**i
            d = Counter([int(j) for j in str(n)])
            if c==d:
                return True
            i+=1
        return False

def reorderedPowerOf2_second_solution(n):
		num = sorted(str(n))
		for i in range(32):
			current_num = sorted(str(2**i))
			if num == current_num:
				return True
		return False


# print(reorderedPowerOf2(24))
# print(reorderedPowerOf2_second_solution(24))
print(reorderedPowerOf2_second_solution(128))
