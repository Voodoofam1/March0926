from input_utils import get_text, get_number
from math_utils import div, add, sub, mul
from string_utils import reverse_text, upper_text, count_text


def run_math():
    a = get_number("введите первое число: ")
    b = get_number("введите второе число: ")

    print("сложение: ", add(a, b))
    print("вычитание: ", sub(a, b))
    print("умножение: ", div(a, b))
    print("деление: ", mul(a, b))


def run_string():
    c = get_text("Введите текст,который необходимо прочесть в обратном порядке")
    d = get_text("Введите название или имя котрое необходимо написать с загланых букв")
    e = get_text("Введите тескт в котором необходимо подсчитать длинну")

    print("переворот текста", reverse_text(c))
    print("увелечение текста", upper_text(d))
    print("подсчет длинны текста", count_text(e))


def main():
    print("1: калькулятор")
    print("2: работа с текстом")
    choice = input("выберите режим: ")
    if choice == "1":
        run_math()
    elif choice == "2":

        run_string()


if __name__ == "__main__":
    main()
