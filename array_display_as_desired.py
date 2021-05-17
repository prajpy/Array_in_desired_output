'''
The below function takes a list and outputs the desired output based on the user input
3 Inputs required:
-first input is the list
-second input is the no of rows that needs to be displayed
-third input is the no of elements in each row which needs to be displayed

-output is the array printed cyclically in a loop

eg:
input:
list = [1,2,3,4], nof_of_iter=2, no_of_elements_in_grp=5
output:
['1','2','3','4','1']
['2','3','4','1','2']
'''

def printlist(mylist,nof_of_iter,no_of_elements_in_grp):
    #initializing the start
    start = 0
    #stop is initialized with no of elements to be displayed in each iteration
    stop = no_of_elements_in_grp
    #the below 5 lines to append and populate the list required for the complete iterations
    tot_elements = nof_of_iter*no_of_elements_in_grp
    res = tot_elements//len(mylist)
    mylist = mylist * res
    bal_elements = tot_elements % len(mylist)
    mylist.extend(mylist[0:bal_elements])
    #the below for loop for displaying the elements by using the index positions
    for _ in enumerate(range(1,nof_of_iter+1)):
        print(mylist[start:stop])
        #incrementing the index to pick the elements for the next iterations
        start+=no_of_elements_in_grp
        stop+=no_of_elements_in_grp


if __name__ == '__main__':
    len_of_list = int(input('enter the length of the list')) #[1,2,3,4,5,6]
    inp_list_element = []
    for i in range(len_of_list):
        element = input('enter the element to added in the list')
        inp_list_element.append(element)
    print('inp_list_element',inp_list_element)
    nof_of_iter = int(input('enter the no of iterations'))
    no_of_elements_in_grp = int(input('enter the no of elements in group'))

    printlist(inp_list_element,nof_of_iter,no_of_elements_in_grp)


