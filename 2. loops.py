#if
score = int(input("score >> "))
if score >= 90:
    print("Grade : A")
elif 80 <= score < 90:
    print("Grade : B")
elif 70 <= score < 90:
    print("Grade : C")
else:
    print("Grade : F")

#while
num = 0
while True:
    num += 1
    if num % 2 == 1:
        continue
    print(num)
    if num == 20: 
        break 

#for
for word in ["one", "two", "three"]:
    print(word)
for i in range(0, 100, 3):
    print(i)