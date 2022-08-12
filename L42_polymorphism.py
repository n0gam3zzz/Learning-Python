# written by zyf in 2022/07/17 12:44
# 多态
# ·简单地说，多态就是“具有多种形态"
#   它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，
#   在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法。
# 静态语言和动态语言关于多态的区别
# ·静态语言实现多态的三个必要条件
#   ·继承
#   ·方法重写
#   ·父类引用指向子类对象
# ·动态语言的多态崇尚“鸭子类型”当看到一只鸟走起来像鸭子、游泳起来像鸭子、收起来也像鸭子，
#   那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。
# ·Java为静态语言、Python为动态语言
class Animal(object):
    def eat(self):
        print("动物要吃东西...")


class Dog(Animal):
    def eat(self):
        print("狗吃肉...")


class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')


class Human(object):
    @staticmethod
    def eat():
        print("人吃五谷杂粮。")


def fun(obj):
    obj.eat()  # 调用eat方法


fun(Animal())
fun(Dog())
fun(Cat())
fun(Human())
