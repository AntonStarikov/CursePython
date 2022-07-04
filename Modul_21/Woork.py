from decorators import debug

@debug
def age_passed(name, age=None):
  if age is None:
    return "Необходимо передать значение age"
  else:
    return "Аргументы по умолчанию заданы!"

print(age_passed("Роман"))
print(age_passed("Роман", age=21))


@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")

@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

print(test_twice.__name__)

def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Конец выполнения функции.")

    return wrapper

@my_decorator
def my_first_decorator():
    print("Это мой первый декоратор!")
