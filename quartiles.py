def calculate_quartiles(classes, total, n, frequency):
    '''
    lower quartile calculation
    '''
    m = 0.25 * total
    cf = 0
    for i in range(n):
        f = frequency[i]
        lcl = i
        cf += f
        if cf >= m:
            break
    CI = (classes[i][1] - classes[i][0]) + 1
    lcb = classes[i][0] - 0.5
    q1 = lcb + (CI * (m - cf) / f)

    '''
    median calculation
    '''
    m = 0.5 * total
    cf = 0
    for i in range(n):
        f = frequency[i]
        lcl = classes[i]
        cf += f
        if cf >= m:
            break
    CI = (classes[i][1] - classes[i][0]) + 1
    lcb = classes[i][0] - 0.5
    q2 = lcb + (CI * (m - cf) / f)

    '''
    upper quartile calculation
    '''
    m = 0.75 * total
    cf = 0
    for i in range(n):
        f = frequency[i]
        lcl = classes[i]
        cf += f
        if cf >= m:
            break
    CI = (classes[i][1] - classes[i][0]) + 1
    lcb = classes[i][0] - 0.5
    q3 = lcb + (CI * (m - cf) / f)

    return q1, q2, q3
