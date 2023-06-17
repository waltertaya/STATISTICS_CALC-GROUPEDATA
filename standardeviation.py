#standardeviation
'''
This file contain the formulae for calculating variance and standard deviation
'''
def calculate_variance(frequency,midpoints,n,total):
    from mean_mode import calculate_mean
    mean = calculate_mean(midpoints,n,frequency,total)
    fx = 0
    for i in range(n):
        fx += (midpoints[i]**2) * frequency[i]
    var = fx/total
    variance = var - (mean**2)
    std_dev = variance**0.5
    return(variance,std_dev)