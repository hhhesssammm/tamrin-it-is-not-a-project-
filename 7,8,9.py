def recursive(array,operator):
    arr_ans=[array[0]]
    if operator=='+' or operator=='-' or operator=='*' or operator=='/':
        for index,value in enumerate(array):
            if index>0:
                arr_ans.append(eval(str(value)+operator+str(arr_ans[index-1])))
        return arr_ans
    if operator=='<':
        for index,value in enumerate(array):
            if index>0:
                if arr_ans[index-1]<value:
                    arr_ans.append(value)
                else:
                    arr_ans.append(arr_ans[index-1])
        return arr_ans


print(recursive([1,2,3,4,5]  ,'+'))
print(recursive([3, 4, 6, 2, 1, 9, 0, 7, 5, 8]  ,'*'))
print(recursive([3, 4, 6, 2, 1, 9, 0, 7, 5, 8] ,'<'))
