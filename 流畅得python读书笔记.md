####开箱即用：  
**operator库：**
（`主要是代替使用匿名函数的使用，例：mul可以替代lambda a, b: a*b使用`）以下为常见接口，详情可参见源码  

    lt      return a<b  
    le      return a<=b
    eq      return a<=b
    ne      return a!=b
    ge      return a>=b
    gt      return a>b
    add     return a+b
    mod     return a%b
    mul     return a*b
**itemgetter：**  
 - 根据元组的某个字段给元组列表排序，例如：`sorted(tuple, itemgetter[1])`表示根据元组第二个位置来进行排序多个参数传给itemgetter时，会根据构建的函数返回提成的值构成新的元组  
 
**methodcaller：**  
 - 自行创建一个函数，调用`methodcaller`中的参数，用来执行其中的方法，例：   
 
        lst = 'Hello'
        a = methodcaller('lower')
        print(a(lst))

**functools库**  
 - partial：基于一个函数创建一个新的可调用对象，把原函数的某些参数固定，使用这个函数可以接受一个或多个参数的函数改编成需要回调的API，这样参数更少，例：  
        
        tmp = partial(mul, 4)
        print(tmp(45))-------same as------45*4

**装饰器基础知识**：  
装饰器是可调用对象，其参数是另一个函数`（被装饰的函数）`。装饰器可能处理被装饰的函数，然后将它返回，或者将其替换成另一个函数或可调用对象，例：  

    @decorate
    def target(*args):
        return args
    相当于decorate(target)
装饰器的一大特性是，能把被装饰函数替换成其他函数，第二个特性是，装饰器在加载模块时立即执行。
不过，大多数装饰器会修改被装饰的函数。通常，它们会定义一个内部函数，然后将其返回，替换被装饰的函数，使用内部函数的代码
几乎全部靠闭包才能正确运转，为了理解闭包，必须首先理解python的变量作用域  
一个例子引入作用域：  

    b = 6
    def func(a):
        print(a)
        print(b)
        b = 9
    func(3)
报错为：`UnboundLocalError: local variable 'b' referenced before assignment`。
这在于python编译函数体时，判断b是局部变量，因为在函数内给b赋值了，生成的字节码也证实了这个判断，python会尝试从本地环境
获取b，在调用func(3)时，尝试获取局部变量b的值，发现局部变量b没有赋值，于是抛出UnboundLocalError，如果想要消除错误，可
以使用globals()来定义b。  

**字节码**：dis模块为反汇编python函数字节码提供了简单的方式  
**闭包**：闭包指延申了作用域的函数，其中包含函数定义体中的引用，但是不在定义体中定义的非全局变量，概念比较复杂，以下通过实例说明。
1. 例一：
 
        class Averager():
            def __init__(self):
                self.seris = []
            def __call__(self, new_value):
                self.seris.append(new_value)
                total = sum(self.seris)
                return total/len(self.seris)
2. 例二：

        def make_average():
            series = []
            def average(new_value):
                series.append(new_value)
                total = sum(series)
                return total / len(series)
            return average
综上，闭包也是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义的作用域不可用了，但是仍然能使用那些绑定  

**nonlocal声明**：  
一个错误示例：  
                
    def make_average():
        count = 0
        total = 0
        def average(new_value):
            count += 1
            total += new_value
            return total / count
        return average
    avg = make_average()
    print(avg(1))
抛出异常：`UnboundLocalError: local variable 'count' referenced before assignment`
当count时数字或者任何不可变类型时，`count += 1`相当于`count = count + 1`，因此在average的定义体中为count赋值了，这会把count变为
局部变量，total也会受影响。为了解决这个问题，python3引入了nonlocal，它的作用是将局部变量转换为自由变量，在上例中增加一行：
    `nonlocal count, total`，对于没有nonlocal方法的python2，可以将实例转换为例如list等可变对象  
    
####**处理装饰器**：  
`functools`中的wraps装饰器能把相关属性从func复制到clocked中，这样就能在clocked函数中处理func函数，此外，还能支持关键字参数
1. functools.lru_cache：是非常使用的装饰器，这是一项优化技术，它把耗时的函数结果保存起来，避免传入相同的参数时重复计算，LRU三个字母是`'least recently used'`的缩写，表明缓存不会无限制增长，一段时间不用的缓存条目会被丢弃。
`functools.lru_cache(maxsize=128, typed=False)`，
`maxsize`指定存储多少个调用的结果，缓存满了之后，旧的结果会被扔掉，腾出空间，为了得到最佳性能，maxsize应该设为2的幂，`typed`如果设置为
True，把不同参数类型得到的结果分开保存，即把通常认为相等的整型和浮点型(如1和1.0)分开，它的所有参数都必须是可散列的
2. `from functools import singledispatch`(单分派泛函数):
 当有一个函数sort_type需要根据传入变量的类型来判断需要输出的内容，常见的作法是使用一个分派函数，在这个函数中通过大量的`if/elif/else`
来判断后执行相应的操作，这样来做不便于模块的扩展，而且显得笨重，时间一长不便于扩展，`functools.singledispatch`来作为装饰器使用，可
将整体方案拆分成多个小模块，甚至可以为你无法修改的类提供专门的函数，例：  

        @singledispatch
        def sort_type(obj):
            print(obj, type(obj), 'obj')

        @sort_type.register(str)
        def _(text):
            print(text, type(text), 'str')
            
        @sort_type.register(numbers.Integral)
        def _(n):
            print(n, type(n), 'int')
叠放装饰器：  

    @d1
    @d2
    def f():
        print('f')
    #等同于：
    def f():
        print('f')
    f = d1(d2(f))
参数化装饰器：有点头大



####对象应用，可变性和垃圾回收
 - python的赋值语句：应该始终先读右边，对象在右边创建或获取，在此之后左边的变量才会绑定到对象上，这就像为便利贴贴上标注。
每个变量都有标识，类型和值。对象一旦创建，它的标识绝地不会改变，可以把标识理解为内存中的地址，is运算符是比较两个对象的标识，id（）
函数返回对象标识的整数表示。  
 - 在==和is运算符之间选择：`==运算符`是比较两个对象的值（对象中保存的数据），`is运算符`是比较两个对象的标识（内存地址）
is运算符的速度比==运算符要快，因为is运算符不能重载，所以python不用寻找魔法函数，再比较两个变量的值，而直接比较两个变量的内存地址，
`a==b`相当于`a.__eq__(b)`。  
 - 元组的相对不可变性：元组与大多数python集合类似，保存的是对象的引用，如果引用的元素的可变的，即使元组本身不可变，元素依然是可变的。  例：   
 
        t1 = (1, 2, [30, 40])
        print(id(t1[-1])) ---》1795727319688
        t1[-1].append(50)
        print(id(t1[-1])) ---》1795727319688

 - 默认做浅复制：构造方法或者[:]做的是浅复制`(即复制了最外层的容器，副本中的元素是源容器中元素的引用)`，如果元素是不可变的，那这样是没有问题
的，还能节省内存，如果元素是可变的，那么这样可能带来意想不到的问题。  
 - 深复制的问题：  
   1. 如果对象有循环引用，深复制可能会被引入无限循环  
   2. 深复制可能太深了，例如，对象可能会引用不该复制的外部资源或单例值，我们可以通过`__copy__`或`__deepcopy__`来控制  
 - 函数的参数作为引用时：python唯一支持的参数传递模式时共享传参，共享传参指函数得各个形式参数获得实参中各个引用得副本。以下示例说明：
                    
        def f(a, b):
            a += b
            return a
        x, y = 1, 2
        print(f(x, y)) ---》3
        print(x, y) ---》1 2
        a, b = [1, 2], [3, 4]
        print(f(a, b)) ---》[1, 2, 3, 4]
        print(a, b) ---》[1, 2, 3, 4] [3, 4]
        #所以我们不要使用可变类型作为函数得默认值传入，为了进一步说明，以下示例说明：
        class HauntedBus:
            def __init__(self, passengers=[]):
                self.passengers = passengers
            def pick(self,name):
                self.passengers.append(name)
            def drop(self,name):
                self.passengers.remove(name)
        RUN：
        bus1 = HauntedBus(['Alice', 'Bob'])
        print(bus1.passengers) ---》['Alice', 'Bob']
        bus1.pick('Jack')
        bus1.drop('Alice')
        bus2 = HauntedBus()
        bus2.pick('Carrie')
        print(bus2.passengers) ---》['Carrie']
        bus3 = HauntedBus()
        bus3.pick('Dave')
        print(bus2.passengers) ---》['Carrie', 'Dave']
        print(bus2.passengers is bus3.passengers) ---》True
        print(bus1.passengers) ---》['Bob', 'Jack']
 以上问题得原因在于：  
 
    实例化类得时候，如果传入乘客，会按期运作，如果没有传入乘客，在加载模块得时候，默认值就变成
    了函数对象得属性，由于默认值是可变对象，也就出现了上面得问题，后续得操作都会受到影响。

 - del和垃圾回收：在`cpython`中，垃圾回收的主要算法是引用计数法，实际上，每个对象都会统计有多少个引用指向自己，当引用归零时，对象立即就被销毁，
`cpython`会在对象上调用`__del__`(如果定义了)，然后释放分配给对象的内存。`cpython2.0`中新增了分代垃圾回收算法用于检测引用循环
中涉及的对象组。del语句删除的时名称，也就是引用，而不是对象，例如：`a=1,b=1,del a`，这个语句时说明删除的是a这个引用，同时在1这个对象上的引用
减一，而不是删除1这个对象，当1的引用被删除为0是，就会立即销毁这个对象。  
 - 弱引用：在计算机程序设计中，弱引用与强引用相对，是指不能确保其引用的对象不会被垃圾回收器回收的引用，一个对象若只被弱引用引用，则在任何时刻都
      可能被回收，弱引用的主要作用是减少循环引用，减少内存中不必要的对象存在的数量。