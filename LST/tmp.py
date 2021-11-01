def get_score(str_score:str)->str:
    p1 = p2 = 0
    i = 0
    flag = True
    while p1 != 10 or p2 != 10:
        if p1 > 10 or p2 > 10:
            return str(p1) + ':' + str(p2)
        if flag:
            for j in range(2):
                if str_score[j] == '1':
                    p1 += 1
                else:
                    p2 += 1
                i += 1
            flag = False
        else:
            for j in range(2):
                if str_score[i] == '1':
                    p2 += 1
                else:
                    p1 += 1
                i += 1
            flag = True
    while abs(p1-p2) < 2:
        if flag:
            if str_score[i] == '1':
                p1 += 1
            else:
                p2 += 1
            flag = False
            i += 1
        else:
            if str_score[i] == '1':
                p2 += 1
            else:
                p1 += 1
            flag = False
            i += 1
    return str(p1) + ':' + str(p2)





x = '1111111111111111111110'
# x = list(map(int, list(x)))
# print(len(x))
# m_score = t_score = 0
a = get_score(x)
print(a)


# print(m_score, ':',t_score)
# print(x[20:])

# x = "123#12@13#133@23#12"
# x = "4@3"
# at_list = x.split('@')
#
# for i in range(len(at_list)):
#     tmp = at_list[i]
#     if '#' not in tmp:
#         continue
#     a, b = tuple(map(int, tmp.split('#')))
#     new_b = a & b
#     at_list[i] = a - new_b
# print(at_list)


import collections

# n, m = tuple(map(int, input().split()))
# # adj = collections.defaultdict(dict)
# adj = dict()
# for _ in range(m):
#     u, v, c, w = tuple(map(int, input().split()))
#     if u not in adj:
#         adj[u] = {v:{c:{w}}}
#     else:
#         adj[u].update({v:{c:{w}}})
#     if v not in adj:
#         adj[v] = {u:{c:{w}}}
#     else:
#         adj[v].update({u:{c:{w}}})
#     # adj[u] = {v: (c, w)}
#     #rint()
# print(adj)







