# A = [64, 25, 12, 22, 11]

# for i in range(len(A)):
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
#     A[i], A[min_idx] = A[min_idx], A[i]

# print("sorted array")
# for i in range(len(A)):
#     print("%d" %A[i])



"""Selection sort with python classes!"""
# class ArraySorter:
#     def __str__(self) -> str:
#         "Array sorter with selection sort algorithm" 


#     def sort_array(self, array) -> list:
#         for i in range(len(array)):
#             index = i
#             for j in range(i + 1, len(array)):
#                 if array[i] > array[j]:
#                     index = j
#             array[i], array[index] = array[index], array[i]
#         return array




