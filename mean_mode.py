#mean_mode.py
'''
This is a file that contains a function to calculate mean and mode
'''
def calculate_mean(midpoints,n,frequency,total):
    fx = 0
    for i in range(n):
        fx += midpoints[i]*frequency[i]
    mean = fx/total
    return(mean)
def calculate_mode(classes,n,frequency):
    mode = 0
    for i in range(n):
        if frequency[i]>mode:
            mode = frequency[i]
        mode_class = classes[i]
    return(mode,mode_class)