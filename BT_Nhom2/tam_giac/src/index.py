
# Hàm này không gọi hàm nào khác
def independentFunction(a,b,c):
    if(a+b<=c):
        return False
    if(a+c<=b):
        return False
    if(b+c<=a):
        return False
    return (True)

# Hàm này gọi hàm foo nên khi test bằng unit test cần phải mock
