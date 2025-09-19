#coding =utf-8
# author =fufu
# test_assert.py
passed_tests = 0 #通过的测试数量
total_tests = 0 # 总测试量
# # 断言函数
# def my_assert(condition,message):
#     global passed_tests,total_tests
#     total_tests += 1
#     try:
#         if condition:
#             passed_tests += 1
#             print(f"✅ PASS: {message}")
#         else:
#             print(f"❌ FAIL: {message}")
#             raise AssertionError(f"条件不成立！")
#     except AssertionError as e:
#         print(f"异常：{e}-->{message}")

#================封装1: 检查是否相等=====================
def check_equal(actual,expected,msg=""):
    '''检查 actual == expected'''
    global passed_tests, total_tests
    total_tests += 1
    if expected == actual:
        passed_tests += 1
        print(f"✅ PASS: {msg} | 实际{actual} == 期望{expected}")
    else:
        print(f"❌ FAIL: {msg} | 实际{actual} != 期望{expected}")

#================封装2: 检查是否不相等=====================
def check_not_equal(actual,expected,msg=""):
    '''检查 actual != expected'''
    global passed_tests, total_tests
    total_tests += 1
    if expected != actual:
        passed_tests += 1
        print(f"✅ PASS: {msg} | 实际{actual} != 期望{expected}")
    else:
        print(f"❌ FAIL: {msg} | 实际{actual} == 期望{expected}")

#================封装3: 检查是否抛出预期异常=====================
def check_exception(func,expected_exception,msg=""):
    '''检查 func()是否抛出expected_exception'''
    global passed_tests, total_tests
    total_tests += 1
    try:
        func()
        print(f"❌ FAIL: {msg} | 应抛出 {expected_exception.__name__}，但未抛出")
    except expected_exception:
        passed_tests += 1
        print(f"✅ PASS: {msg} | 正确抛出 {expected_exception.__name__}")
    except Exception as e:
        print(f"❌ FAIL: {msg} | 抛出异常 {type(e).__name__}，但期望是 {expected_exception.__name__}")

#================封装4: 检查是否在容器中=====================
def check_in(item,container,msg=""):
    '''检查item是否在container容器中'''
    global passed_tests, total_tests
    total_tests += 1
    if item in container:
        passed_tests += 1
        print(f"✅ PASS: {msg} | {item}在{container}中")
    else:
        print(f"❌ FAIL: {msg} | {item}不在{container}中")

#================封装5:比较2个数大小 =====================
def check_greater_than(a,b,msg=""):
    '''检查2个数谁大'''
    global passed_tests, total_tests
    total_tests += 1
    if a > b:
        passed_tests += 1
        print(f"✅ PASS: {msg} | {a}比{b}大")
    else:
        print(f"❌ FAIL: {msg} | {a}没有比{b}大")

#================封装6:判断是否是偶数 =====================
def check_is_even(number, msg=""):
    '''判断是否是偶数'''
    global passed_tests, total_tests
    total_tests += 1
    if number % 2 == 0:
        passed_tests += 1
        print(f"✅ PASS: {msg} | {number}是偶数")
    else:
        print(f"❌ FAIL: {msg} | {number}不是偶数")

#================封装7:判断2个数谁小 =====================
def check_is_less_than(a,b,msg=""):
    '''判断2个数谁小'''
    global passed_tests, total_tests
    total_tests += 1
    if a < b:
        passed_tests += 1
        print(f"✅ PASS: {msg} | {a}比{b}小")
    else:
        print(f"❌ FAIL: {msg} | {a}不比{b}小")

#================封装8:字符串包含 =====================
def check_in_container(text,substring,msg=""):
    '''判断字符串是否包含'''
    global passed_tests, total_tests
    total_tests += 1
    if substring in text:
        passed_tests += 1
        print(f"✅ PASS: {msg} | {text}包含{substring}")
    else:
        print(f"❌ FAIL: {msg} | {text}不包含{substring}")

#================封装9:判断是否近似相等 =====================
def check_approx_equal(actual,expected,tolerance=0.01,msg=""):
    '''判断2个数是否近似相等'''
    global passed_tests, total_tests
    total_tests += 1
    if abs(actual - expected) < tolerance:
        passed_tests += 1
        print(f"✅ PASS: {msg} | 实际{actual}近似等于 期望{expected}")
    else:
        print(f"❌ FAIL: {msg} | 实际{actual}不近似等于 期望{expected}")


# 被测试的函数
def add(a,b):
    return a + b

def format_money(amount):
    return f"cny {amount:.2f}"

def devide(a,b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a/b

#测试函数
def test_add():
    check_equal(add(1,2), 3,"1+2 应该等于3")
    check_equal(add(1,-1), 0,"1+（-1） 应该等于0")



def test_format_money():
    check_equal(format_money(123.456),"cny 123.46","金额格式化测试")
    check_equal(format_money(0), "cny 0.00", "0金额测试")

def test_devide():
    check_equal(devide(10, 2),5,"10/2应该等于5")
    check_not_equal(devide(10, 3), 3, "10/3不等于3")
    check_exception(lambda :devide(1, 0),ValueError,'除数不能为0')
    check_exception(lambda: devide(1, 'a'),ZeroDivisionError , '除数不能为非数字')
    check_exception(lambda: devide(1, 1), ValueError, '1/1 等于1')

def test_check_in():
    check_in('apple',['apple','banner','xigua'],'apple在水果中')
    check_in('pig', ['apple', 'banner', 'xigua'], 'pig不在水果中')

def test_check_greater_than():
    check_greater_than(1,2,"1没有比2大")
    check_greater_than(3, 2, "3比2大")

def test_check_is_even():
    check_is_even(2,"2是偶数")
    check_is_even(3, "3不是偶数")

def test_check_is_less_than():
    check_is_less_than(1,2,"1比2小")
    check_is_less_than(3, 2, "3不比2小")

def test_check_in_container():
    check_in_container('abc','a',"a在字符串abc中")
    check_in_container('dbc', 'a', "a不在字符串cbc中")

def test_check_approx_equal():
    check_approx_equal(1.01,1.009,msg='1.01近似等于1.009')
    check_approx_equal(2,1,0.02,"1不近似等于2")






if __name__ == "__main__":
    print("🚀 开始运行自动化测试...\n")
    test_add()
    test_format_money()
    test_devide()
    test_check_in()
    test_check_greater_than()
    test_check_is_even()
    test_check_is_less_than()
    test_check_in_container()
    test_check_approx_equal()
    print("\n" + "="*50)
    print("📊 测试报告")
    print(f"✅ 通过测试数：{passed_tests}")
    print(f"📋测试总数：{total_tests}")
    print(f"🎯用例通过率：{passed_tests / total_tests*100:.1f}%")
    if passed_tests == total_tests:
        print("\n🎉 恭喜！所有测试通过！你的代码稳如泰山！")
    else:
        print("\n⚠️ 注意：有测试未通过，请检查代码！")

