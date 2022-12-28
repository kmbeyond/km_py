#transform the array into ascending-then-descending order
#ascending order till mid & remaining in descending order
Ex: 1234567 -> 123 7 654

[2,4,6,8,7,1,9] => [1, 2, 4, 9, 8, 7, 6]

def sortAscDescSequence(a):
    a.sort()
    n = len(a)
    #swap middle digit with last digit
    mid = int((n + 1)/2)-1
    a[mid], a[n-1] = a[n-1], a[mid]

    #swap digits between mid+1 till last but one
    start, end = mid + 1, n-2
    while(start <= end):
        a[start], a[end] = a[end], a[start]
        start = start + 1
        end = end - 1

    return a


print(sortAscDescSequence([2,4,6,8,7,1,9]))
