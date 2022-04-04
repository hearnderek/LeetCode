def kth_largest(xs, k):
    return sorted(xs, reverse=True)[k-1]


def test(xs, k, answer):
    r = kth_largest(xs, k)
    if r != answer:
        print("fail:", r , "!=", answer)

if __name__ == '__main__':
    test([1,2,3,4,5], 2, 4)
    test([3,2,3,1,2,4,5,5,6], 4, 4)
    test([2,1],2,1)