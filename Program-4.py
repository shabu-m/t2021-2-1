num_list = []
count1=0;count2=0;count3=0;count4=0;count5=0;count6=0;count7=0;count8=0;count9=0;
count = int(input("Enter the total count of elements : "))
for i in range(0,count):
    num_list.append(int(input()))
print("input ")
print(num_list)
for i in range(count):
    if (num_list[i]%2) ==0:
      count1=count2+1
      
for i in range(count):
    if (num_list[i]%3) ==0:
      count1=count3+1
      
for i in range(count):
    if (num_list[i]%4) ==0:
      count1=count4+1
      
for i in range(count):
    if (num_list[i]%5) ==0:
      count1=count5+1
      
for i in range(count):
    if (num_list[i]%6) ==0:
      count1=count6+1
      
for i in range(count):
    if (num_list[i]%7) ==0:
      count1=count7+1
      
for i in range(count):
    if (num_list[i]%8) ==0:
      count1=count8+1
      
for i in range(count):
    if (num_list[i]%9) ==0:
      count1=count9+1
      
print("{1:",count,", 2:",count2,", 3:",count3,", 4:",count4,", 5:",count5,", 6:",count6,", 7:",count7,", 8:",count8,", 9:",count9,"}")
