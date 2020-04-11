import copy


def matrix_bomb(m):
    px = py = 0
    l = []
    while px < len(m):
        m1 = copy.deepcopy(m)
        for i in range(0, len(m)):
            for j in range(0, len(m)):
                if i >= py - 1 and i <= py + 1:
                    if j >= px - 1 and j <= px + 1:
                        if i == py and j == px:
                            m1[i][j] = m1[py][px]
                        else:
                            if (m1[i][j] - m1[py][px]) > 0:
                                m1[i][j] = (m1[i][j] - m1[py][px])
                            elif m1[i][j] - m1[py][px] < 0:
                                m1[i][j] = 0
        s = 0

        for i in m1:
            for j in i:
                s += j
        l.append({(py, px), s})
        if px < len(m):
            px += 1
        if px == len(m):
            px = 0
            py += 1
        if py == len(m):
            break
    print(l)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_bomb(m)
