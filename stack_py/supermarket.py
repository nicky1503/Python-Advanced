from collections import deque

data = input()
costumers = deque([])
while data != "End":
    if data != "Paid":
        costumers.append(data)
    else:
        for name in range(len(costumers)):
            print(costumers.popleft())

    data = input()
print(f"{len(costumers)} people remaining.")