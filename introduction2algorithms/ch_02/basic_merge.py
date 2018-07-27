# arr = [3, 41, 52, 226, 38, 57, 9, 49]
#
#
# # Devide the list into two arr
# sub_arr_1 = arr[0: int(len(arr)/2)]
# sub_arr_2 = arr[int(len(arr)/2):]
# print("arr 1 ", sub_arr_1)
# print("arr 2 ", sub_arr_2)
#
#
# for i in :
#     pass



# def merge(items, p, q, r):
#     L = items[p:q+1]
#     R = items[q+1:r+1]
#     i = j = 0
#     k = p
#     while i < len(L) and j < len(R):
#         if(L[i] < R[j]):
#             items[k] = L[i]
#             i += 1
#         else:
#             items[k] = R[j]
#             j += 1
#         k += 1
#     if(j == len(R)):
#         items[k:r+1] = L[i:]
#
#
#
# def mergesort(items, p, r):
#     print("num p ", p)
#     print("num r ", r)
#     if(p < r):
#         q = (p+r)//2
#         mergesort(items, p, q)
#         mergesort(items, q+1, r)
#         merge(items, p, q, r)
#
#
# items = [4,3,2,1,17]
# mergesort(items, 0, len(items)-1)
# print(items)
