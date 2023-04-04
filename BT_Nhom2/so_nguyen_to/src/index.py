
import math
# Hàm này không gọi hàm nào khác
def independentFunction(a):
    if(a<2):
        return False
    if(a==2):
        return True
    if(a%2==0):
        return False
    for i in range(3,a-1,2):
        if(a%i==0):
            return False
    return True

# Hàm này gọi hàm foo nên khi test bằng unit test cần phải mock
