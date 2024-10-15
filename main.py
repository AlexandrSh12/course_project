import pygame
import sys
import random

# Инициализация микшера pygame
pygame.mixer.init()

# Загрузка музыки
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)  # Воспроизведение музыки в цикле


# Инициализация pygame
pygame.init()

# Установка размеров экрана
screen = pygame.display.set_mode((1024, 1024))

# Установка заголовка окна
pygame.display.set_caption("RUSSIAN MARIO")

# Загрузка фонового изображения
background = pygame.image.load('back.jpg')

# Создание игрока
player = pygame.image.load('mario.png')
player_pos = [250, 670]

# Создание блина
candy = pygame.image.load('blin.png')
candy_pos = [random.randint(0, 800), 0]
candy_speed = 1.5



# Скорость перемещения игрока и сила прыжка
player_speed = 2
jump_strength = 10

# Переменная для отслеживания состояния прыжка
is_jumping = False

# Очки игрока
score = 0
font = pygame.font.Font(None, 36)

# Игровой цикл
while True:
    # Заполнение экрана цветом
    screen.fill((0, 0, 0))

    # Отрисовка фона
    screen.blit(background, (0, 0))

    # Отрисовка игрока
    screen.blit(player, player_pos)

    # Отрисовка конфеты
    screen.blit(candy, candy_pos)
    candy_pos[1] += candy_speed
    if candy_pos[1] > 800:
        candy_pos = [random.randint(0, 800), 0]

    # Проверка столкновения с конфетой
    if player_pos[0] < candy_pos[0] < player_pos[0] + 250 and player_pos[1] < candy_pos[1] < player_pos[1] + 333:
        score += 1
        candy_pos = [random.randint(0, 800), 0]

    # Отображение очков
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Проверка на достижение N очков
    end = 15
    if score >= end:
        pygame.mixer.music.stop()  # Остановка фоновой музыки
        pygame.mixer.music.load('end.mp3')  # Загрузка музыки концовки
        pygame.mixer.music.play()  # Воспроизведение музыки концовки
        win_text = font.render('Вы победили!', True, (255, 255, 255))
        screen.blit(win_text, (350, 300))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True

    # Получение состояния клавиатуры
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed

    # Обработка прыжка
    if is_jumping:
        player_pos[1] -= jump_strength
        jump_strength -= 0.5  # Уменьшаем силу прыжка медленнее
        if jump_strength < -10:
            is_jumping = False
            jump_strength = 10

    # Обновление дисплея
    pygame.display.update()