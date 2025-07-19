import math as m

def circle_intersect(x1:float , y1:float, r1:float, x2:float, y2:float, r2:float, epsilon=10e-6) -> int:
    distance = m.sqrt((x1-x2)**2+(y1-y2)**2)
    total_radius = r1+r2
    diff = distance-total_radius
    if diff < -epsilon :
        return 1
    elif abs(diff) <= epsilon :
        return 0
    else :
        return -1

def my_min_mid_max(a: int, b: int, c: int) -> str:
    def less_than_or_equal(x: int, y: int) -> bool:
        return x <= y
    if less_than_or_equal(a, b) and less_than_or_equal(a, c):
        if less_than_or_equal(b, c):
            return f"{a} {b} {c}"
        else:
            return f"{a} {c} {b}"
    elif less_than_or_equal(b, a) and less_than_or_equal(b, c):
        if less_than_or_equal(a, c):
            return f"{b} {a} {c}"
        else:
            return f"{b} {c} {a}"
    else:
        if less_than_or_equal(a, b):
            return f"{c} {a} {b}"
        else:
            return f"{c} {b} {a}"

def minute_diff(h1:int, m1:int, p1:str, h2:int, m2:int, p2:str) -> int :
    def if_PM(p:str) -> int :
        if p=="PM" :
            return 12
        elif p=="AM" :
            return 0
    total1 = ((h1+if_PM(p1))*60)+m1
    total2 = ((h2+if_PM(p2))*60)+m2
    return abs(total1-total2)

def calculate_exp_(p:int, c:int) -> int :
    res=0
    while p>0 :
        if c-12>=0 :
            c-=12
            res+=1000
            c+=2
        c+=1
        p-=1
    return res

def calculate_exp(p: int, c: int) -> int:
    if p == 0:
        return 0
    if p == 1:
        if c >= 12:
            return 1000
        else:
            return 0
    if c >= p * 10 + 2:
        return p * 1000
    else:
        P = (p - 1 + c - 1) // 11
        if p > P:
            return P * 1000
        else:
            return p * 1000

def divide_plot(x:int, y:int, z:int, start:str) -> str :
    plots=[x,y,z]
    pos={'A':0, 'B':1, 'C':2}
    idx=pos[start]

    avg=(x+y+2)/2

    ops=[]
    
    def move_to(target:int) :
        nonlocal idx
        if target==idx :
            return
        elif target==idx-1 :
            ops.append("LEFT")
        elif target==idx+1 :
            ops.append("RIGHT")
        elif target<idx :
            while idx>target:
                ops.append("LEFT")
                idx-=1
        elif target>idx :
            while idx<target:
                ops.append("RIGHT")
                idx+=1
            idx=target

    for i in range(2):
        if plots[i] > avg:
            excess = plots[i] - avg
            plots[i] -= excess
            plots[i+1] += excess
            move_to(i)
            ops.append(f"PUSH_RIGHT {excess}")
    
    for i in range(2, 0, -1):
        if plots[i] > avg:
            excess = plots[i] - avg
            plots[i] -= excess
            plots[i-1] += excess
            move_to(i)
            ops.append(f"PUSH_LEFT {excess}")

    return ", ".join(ops)

if __name__ == "__main__":
    # print(circle_intersect(2, 3, 5, 0, 7, 1))
    # print(circle_intersect(0, 0, 2.5, 3, 4, 2.5))
    
    # print(my_min_mid_max(1, 2, 3))

    # print(minute_diff(8, 23, 'AM', 8, 24, 'AM'))
    # print(minute_diff(8, 23, 'AM', 1, 24, 'PM'))
    # print(minute_diff(1, 24, 'PM', 8, 23, 'AM'))
    
    print(calculate_exp(1, 12))
    print(calculate_exp(2, 12))
    print(calculate_exp(2, 22))
    print(calculate_exp(20,1))
    print(calculate_exp(20,11))
    print(calculate_exp(11,12))
    # print(calculate_exp(2,12))
    # print(calculate_exp(1,12))
    # print(calculate_exp(2,22))

    # print(divide_plot(2, 5, 8, 'A'))
    # print(divide_plot(2, 5, 8, 'C'))
    # print(divide_plot(60, 60, 60, 'B'))