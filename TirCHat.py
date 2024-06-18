import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка иконки окна
icon = pygame.image.load('img/boeing-ea-18-growler-boeing-air-force-airplane-military-figh.jpg')
pygame.display.set_icon(icon)

# Спрятать курсор
pygame.mouse.set_visible(False)

# Загрузка изображений
target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80
gun_image = pygame.image.load('img/оружие.png')  # Предположим, что у вас есть изображение ружья
gun_image = pygame.transform.scale(gun_image, (50, 70))  # Масштабирование ружья
shot_image = pygame.image.load('img/shot.png')  # Предположим, что у вас есть изображение выстрела
shot_image = pygame.transform.scale(shot_image, (100, 100))  # Масштабирование выстрела

# Начальная позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Переменные для выстрела
show_shot = False
shot_timer = 0

# Основной цикл игры
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                show_shot = True
                shot_timer = pygame.time.get_ticks()

    # Получение позиции курсора мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Рисование мишени
    screen.blit(target_img, (target_x, target_y))

    # Рисование ружья, следящего за курсором мыши
    gun_rect = gun_image.get_rect(center=(mouse_x, mouse_y))
    screen.blit(gun_image, gun_rect.topleft)

    # Рисование выстрела
    if show_shot:
        screen.blit(shot_image, gun_rect.topleft)
        if pygame.time.get_ticks() - shot_timer > 100:  # Показать выстрел в течение 100 мс
            show_shot = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()