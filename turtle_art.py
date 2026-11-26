import colorsys
import turtle


def draw_mandala(petals=36, radius=160, steps_per_petal=60):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#121622")
    screen.title("Python Turtle: 기하학 만다라 꽃무늬")
    screen.tracer(0)

    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    t.pensize(2)

    angle_step = 360 / petals

    for i in range(petals):
        # HSV 색 공간에서 hue(색조)를 0.0 ~ 1.0 사이로 순환시켜 그라데이션 연출
        hue = i / petals
        r, g, b = colorsys.hsv_to_rgb(hue, 0.85, 1.0)
        t.pencolor(r, g, b)

        t.penup()
        t.goto(0, 0)
        t.setheading(i * angle_step)
        t.pendown()

        # 한 잎의 곡선 그리기
        for step in range(steps_per_petal):
            progress = step / steps_per_petal
            length = radius * (1 - abs(2 * progress - 1) * 0.35)
            t.forward(length / steps_per_petal)
            t.left(180 / steps_per_petal)

    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    draw_mandala()