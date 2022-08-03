#Binary Search Implementation

def binarySearch( array, key ):
    left = 0
    right = len(array) - 1
    
    while( left <= right ):
        mid = ( left + right )// 2
        
        if( array[mid] == key ):
            return mid

        elif( array[mid] < key ):
            left = mid + 1
        else:
            right = mid - 1

    return -1

#Main
arr = []

n = int( input( "Enter the number of Elements: " ) )

print("Enter array of numbers: ")

for i in range( 0, n ):
    arr.append( int( input( ) ) )
arr.sort()

target = int( input( "Enter the Element to find: " ) )

pos = binarySearch( arr, target )
if(pos != -1 ):
    pos+= 1
    print( "Element found at ", pos )
else:
    print( "Element not found" )