#accuracy.py
'''
file finds the accuracy u
'''
def calculate_accuracy(classes):
    if classes == int(classes):  # Check if the number is a whole number
        return 1  # Accuracy is 1 for whole numbers
    else:
        decimal_places = len(str(classes).split('.')[1])
        accuracy = 10 ** -decimal_places
        return accuracy
    