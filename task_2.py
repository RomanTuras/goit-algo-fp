import turtle
import math

def draw_pythagoras_tree(branch_length, level, angle):
    '''Рекурсивна функція малювання дерева'''

    if level == 0: #Базовий вападок
        return

    turtle.forward(branch_length)

    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), level - 1, angle)

    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * math.sin(math.radians(angle)), level - 1, angle)

    turtle.left(angle)
    turtle.backward(branch_length)

def main():
    # рівень рекурсії
    level = int(input("Введіть рівень рекурсії (5..9): "))
    if level > 9:
        print("Занадто велике значення - буде досить повільно працювати")
    elif level <5:
        print("Занадто мале значення - не буде зрозуміло, що намальовано")
    else:
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Pythagoras Tree Fractal")

        turtle.speed(0)  # Максимальна швидкість малювання
        turtle.left(90)  # Початковий напрямок вгору
        turtle.up()
        turtle.goto(0, -200)  # Початкове положення turtle
        turtle.down()

        # Початкові параметри для дерева Піфагора
        initial_branch_length = 100
        angle = 45  # Кут розгалуження

        draw_pythagoras_tree(initial_branch_length, level, angle)
        
        turtle.hideturtle()
        screen.mainloop()

if __name__ == "__main__":
    main()
