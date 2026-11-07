"""for, while, range, break/continue/else, enumerate and zip."""

for i in range(3):
    print("i =", i)
print(list(range(10, 0, -3)))  # start, stop (excluded), step

names = ["ada", "linus", "grace"]
for index, name in enumerate(names, start=1):
    print(index, name)
for name, score in zip(names, [90, 80, 95], strict=True):
    print(f"{name:>6}: {score}")

# while repeats until the condition is false.
n, steps = 27, 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
print("collatz steps for 27:", steps)

# break leaves the loop, continue skips to the next iteration.
for number in range(2, 20):
    if number % 2 == 0:
        continue
    if number > 11:
        break
    print("odd:", number)

# The else clause of a loop runs only if the loop was NOT ended by break.
for candidate in (9, 15, 21):
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            print(candidate, "is composite")
            break
    else:
        print(candidate, "is prime")

# Nested loops: a multiplication table.
for row in range(1, 4):
    print(" ".join(f"{row * col:2}" for col in range(1, 5)))
