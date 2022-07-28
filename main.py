import pygame
from pygame import *
from player import Player
from blocks import Platform

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#776262"
entities = pygame.sprite.Group() # Все объекты
platforms = [] # то, во что мы будем врезаться или опираться
hero = Player(55, 55)  # создаем героя по (x,y) координатам
entities.add(hero)
level = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "-   -----------         -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]

timer = pygame.time.Clock()


left = right = False  # по умолчанию — стоим
up = False

pygame.init()  # Инициация PyGame, обязательная строчка
screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
# будем использовать как фон
bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

while 1:  # Основной цикл программы
    timer.tick(60)
    for e in pygame.event.get():  # Обрабатываем события
        if e.type == QUIT:
            raise SystemExit
        if e.type == KEYDOWN and e.key == K_LEFT:
            left = True
        if e.type == KEYDOWN and e.key == K_RIGHT:
            right = True

        if e.type == KEYUP and e.key == K_RIGHT:
            right = False
        if e.type == KEYUP and e.key == K_LEFT:
            left = False

        if e.type == KEYDOWN and e.key == K_UP:
            up = True

        if e.type == KEYUP and e.key == K_UP:
            up = False

    x = y = 0  # координаты
    screen.blit(bg, (0, 0))

    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля


    hero.update(left, right, up, platforms)  # передвижение


    entities.draw(screen)  # отображение всего


    pygame.display.update() # обновление и вывод всех изменений на экран
