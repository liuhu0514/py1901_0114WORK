'''
变量的语法
    全局变量：被所有代码都能访问的变量
        声明在函数的外部
    局部变量：只能被当前所属函数能访问的~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    变量
        声明在函数的内部
'''
# 全局变量，能被当前文件中的所有python代码访问【先声明赋值，后使用变量】
users = "admin"

# 普通代码中使用
print("普通代码中使用", users)

# if结构中使用
if 1:
    print("if结构中使用", users)


# 循环结构中使用
while 1:
    print("循环结构中使用", users)
    break

# 函数中使用
def test_a():
    # 声明一个test_a()函数中的局部变量
    phone = 'HUWEI META20'
    print("test_a中访问test_a局部变量：", phone)
    print("test_a访问全局变量：", users)


def test_b():
    # print("test_b中访问test_a局部变量：", phone) # ERROR
    print("test_b访问全局变量：", users)


# print("普通代码中访问test_a局部变量：", phone) # ERROR

test_a()
test_b()

# print("普通代码中访问test_a局部变量：", phone) # ERROR


'''
困扰：什么时候定义数据为全局变量？什么时候定义数据为局部变量？
    如果一个数据需要被多个函数公共使用，建议定义为全局变量
        如：系统中保存所有用户的变量~可能会被系统中任意函数使用，所以定义为全局变量
    如果一个数据只是当前函数中运算临时需要，建议定义为局部 变量
        如：系统中登录函数，用户输入账号+密码，验证是否正确返回登录结果【成功|失败】
                用户输入的账号+密码临时在当前函数中验证使用，函数执行完成后失去了意义；
                输入的账号+密码，定义为局部变量
'''
