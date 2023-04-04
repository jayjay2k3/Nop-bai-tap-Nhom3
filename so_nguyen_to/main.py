from src.index import independentFunction

if __name__ == "__main__":
    n = int(input("Nhap gia tri n:"))
    for i in range(2,n):
        if(independentFunction(i)):
            print(f"{i} ")
    

