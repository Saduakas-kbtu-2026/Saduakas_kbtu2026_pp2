#601
n = int(input())
nums = list(map(int, input().split()))

squares = map(lambda x: x**2, nums)

print(sum(squares))

#602
n = int(input())
nums = list(map(int, input().split()))

evens = filter(lambda x: x % 2 == 0, nums)

print(len(list(evens)))

#603
n = int(input())
words = input().split()

for i, w in enumerate(words):
    print(f"{i}:{w}", end=" ")

#604
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dot = sum(a*b for a, b in zip(A, B))

print(dot)

#605
s = input()

vowels = "aeiouAEIOU"

print("Yes" if any(c in vowels for c in s) else "No")

#606
n = int(input())
nums = list(map(int, input().split()))

print("Yes" if all(x >= 0 for x in nums) else "No")

#607
n = int(input())
words = input().split()

print(max(words, key=len))

#608
n = int(input())
nums = list(map(int, input().split()))

print(*sorted(set(nums)))

#609
n = int(input())
keys = input().split()
values = input().split()

d = dict(zip(keys, values))

query = input()

print(d.get(query, "Not found"))

#610
n = int(input())
nums = map(int, input().split())

print(sum(map(bool, nums)))
