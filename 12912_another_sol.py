# %%
def solution(a, b):
    if a<=b:
        return sum(i for i in range(a,b+1))
    return sum(i for i in range(b,a+1))

# %%
solution(4,2)

# %%
solution(3,3)

# %%
def solution(a,b):
    return (abs(a-b)+1)*(a+b)//2

# %%
solution(4,2)

# %%



