"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""
list1 = [1,2,3,4,5,6,7,8,9,10]
print("The original list",list1)
extacted_list = list1[0:5]
reversed_list = extacted_list[::-1]
print("The extracted list",extacted_list)
print("The reversed list",reversed_list)