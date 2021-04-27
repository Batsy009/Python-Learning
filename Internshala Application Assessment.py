def fib(num):
  if num <= 2:
    return 1
  return (9*fib(num - 1)) - (4*fib(num - 2))


def is_part_of_series(lst):
    for i in lst:
        if fib(i) in lst:
            return True
        return False
l = [1, 2, 3, 4, 5]
print(is_part_of_series(l))
