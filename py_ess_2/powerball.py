from random import choice, sample

nums = [n for n in range(1, 70)]
ball = [n for n in range(1, 30)]

lottery = sample(nums, 5)
lottery = sorted(lottery)
lottery.append(choice(ball))

print(lottery)