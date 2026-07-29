"""n = int(input().strip()) 
if not (n%2 ==0): 
  print("Weird") 
else: 
    if n in range(2 ,6): 
        print("Not Weird") 
        
    if n in range(6,21): 
        print("Weird") 
    if (n>20): 
        print("Not Weird")"""

if __name__ == '__main__':
    for _ in range(int(input())):
        nested_list=[[],[]]
        name = input()
        score = float(input())
        nested_list.append(name)
        nested_list.append(score)
        print(nested_list)