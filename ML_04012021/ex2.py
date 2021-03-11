L = [1, 3, 5, 4, 7, 9]
print('L is: ', L)
print('================================')

# print 2 -> 4
print('Print from pos 2 to 4: ', L[2:4])

# print 2 -> end
print('Print from pos 2 to end:', L[2:])

# print 1 3 5
print('Print pos 1 3 5: ',L[1:6:2])

# insert value 10
L.append(10)
print("After adding 10: ", L)

# print size of list
print('Len of L:', len(L))

# sort and print
print('Print sorted list L:')
L.sort()
print(L)

# Reverse
print('Revers list:')
L.reverse()
print(L)

# Delete list element at pos 3
print('Delete list element at pos 3:')
L.remove(L[3])
print(L)



