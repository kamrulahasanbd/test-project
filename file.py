
test_write = open('c:/Users/Administrator/Desktop/pyhton practice/demo1.txt', 'r')
x = test_write.readline().replace('/n', '')
print(len(x))
#print('kamrul ahasan----1', 1980, 31, sep= " ",end="\n", file=test_write, flush=True)

qty = "i am kamrul ahasan. i am jobless. i am looking new job but have not get any positive response. that's why i m hopeless"
make_list = qty.split('.')
#make_list1= qty.split()
#print(make_list)
print(make_list)
print(len(qty))