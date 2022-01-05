#要求一：函式與流程控制
def calculate(min, max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30



#要求二：Python 字典與列表
def avg(data):
    sum=0
    for a in range(0,data["count"]):
        sum=sum+data["employees"][a]["salary"]
    print(sum/data["count"])

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


#要求三：找出至少包含兩筆整數的列表 (Python) 中，兩兩數字相乘後的最大值
def maxProduct(nums):
    length=len(nums)
    max=nums[0]*nums[1]
    for a in range(length-1) :
        for b in range(a+1,length):
            total=nums[a]*nums[b]
            if total>max:
                max=total
    print(max)
    
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1,-2,0])  # 得到 2


#要求四：Given an array of integers, show indices of the two numbers such that they add up to a　specific target.
def twoSum(nums, target):
    length=len(nums)
    for a in range(length-1) :
        for b in range(a+1,length):
            if nums[a]+nums[b]==target :
                return [a,b]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#要求五：給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。
def maxZeros(nums):
    length=len(nums)
    sum=0
    total=[]
    for a in range(length) :
        if nums[a]==0 :
            sum+=1
        else : 
            total.append(sum)
            sum=0
    total.append(sum)        
    total.sort(reverse=True)
    print(total[0])

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3


