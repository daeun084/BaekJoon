import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_post_order(pre_order):
    if not pre_order:
        return []

    root = pre_order[0]
    left_subtree = [x for x in pre_order if x < root]
    right_subtree = [x for x in pre_order if x > root]

    left_post_order = find_post_order(left_subtree)
    right_post_order = find_post_order(right_subtree)

    return left_post_order + right_post_order + [root]


if __name__ == "__main__":
    pre_order = []

    while True:
        try:
            pre_order.append(int(input()))
        except:
            break

    post_order = find_post_order(pre_order)
    print(" ".join(map(str, post_order)))