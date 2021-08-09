# Use python3
import sys

def merge(left,right):
    count,i,j,res = 0,0,0,[]
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
            count += (len(left)-i)
        else:
            res.append(left[i])
            i += 1
    return res + left[i:] + right[j:],count

def get_number_of_inversions(a, b, left, right):
    length_array = len(a)
    if length_array <=1:
        return a,0
    ave = length_array // 2
    left_arr, number_of_inversions_left = get_number_of_inversions(a[:ave], b, left, ave)
    right_arr, number_of_inversions_right = get_number_of_inversions(a[ave:], b, ave, right)
    merged, count = merge(left_arr,right_arr)
    count += (number_of_inversions_left + number_of_inversions_right)
    return merged, count

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a))[1])
