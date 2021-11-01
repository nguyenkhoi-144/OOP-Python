#unpaking(giai nen)
#với 1 hàm thì argv 0 luôn là self
#nhung trong unpaking thì argv  sẽ la biến
'''def fun(a,b,c,d):
    print(a,b,c,d)
my_list = [1,2,3,4]
#print(my_list)
fun(*my_list)'''
'''argv = [0,1,2,3]
def sum(a,b,c,d):
    return a + b + c + d
print(sum(*argv))'''
'''argv = [2,7]
for i in range(*argv):
    print(i, end=" ")'''

#paking
# khong biet co bao nhieu doi so sẽ truyen vao ham
'''def mysum(*argv):   # khong biet truyen vao bao nhieu doi so
    return sum(argv) # tinh tong cac doi so
print(mysum(1,2,3,4,5,6))'''
#paking and unpaking
# trong def 2 goji def 1
def fun1(a,b,c):
    print(a,b,c)

def fun2(*argv):
    argv = list(argv)
    argv[0] = "a"
    argv[1] = "b"
    fun1(*argv)
fun2("hello", "an", "binh")

