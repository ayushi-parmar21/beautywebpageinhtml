n = int(input())
div = int(input())

def FindSumOfRemainders(n, div):
    result=0
    i=0
    while i<=(div):
        divide=i//div
        result+=divide
        i+=1
    return result
result = FindSumOfRemainders(n, div)
print(result)