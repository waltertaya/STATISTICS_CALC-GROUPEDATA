n = int(input('Enter the number of classes in the distribution: '))
classes = []
for i in range(n):
    k = input('Enter the classes separated by a comma: ')
    lower, upper = map(int, k.split(','))
    classes.append((lower, upper))
print(classes)

midpoints = []
for lower, upper in classes:
    x = (lower + upper) / 2
    midpoints.append(x)
print(midpoints)
frequency = []
for i in range(n):
    count = int(input('Enter the frequencies inorder of the classes: '))
    frequency.append(count)
print(frequency)
import pandas as pd
table_data = {
    'classes':classes,
    'midpoints':midpoints,
    'frequency':frequency
}
df = pd.DataFrame(table_data)
print(df)
total = sum(frequency)
import mean_mode
mean = mean_mode.calculate_mean(midpoints,n,frequency,total)
print(mean)
import mean_mode
mode,mode_class = mean_mode.calculate_mode(classes,n,frequency)
print(mode,mode_class)
import standardeviation
variance,std_dev = standardeviation.calculate_variance(frequency,midpoints,n,total)
print(variance,std_dev)