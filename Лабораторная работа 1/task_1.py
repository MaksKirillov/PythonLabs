numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_of_none = numbers.index(None)
numbers[index_of_none] = 0
sum_of_numbers = sum(numbers)
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers
numbers[index_of_none] = average_of_numbers

print("Измененный список:", numbers)
