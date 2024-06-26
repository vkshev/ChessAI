import pygame

def load_and_transform_image(filename, width, height):
    img = pygame.image.load(filename)
    return pygame.transform.smoothscale(img, (width, height))

def load_piece_images(width, height):
    piece_names = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']
    piece_images = {}
    for i in range(6):
        for j in range(2):
            color = 'white' if j == 0 else 'black'
            filename = f'{color}_{piece_names[i]}.png'
            img = load_and_transform_image(f'assets\img\{filename}', width, height)
            piece_images[filename] = img
    return piece_images

def init_sounds():
    pygame.mixer.init()
    global move_sound, capture_sound
    move_sound = pygame.mixer.Sound('assets/sounds/move.wav')
    capture_sound = pygame.mixer.Sound('assets/sounds/capture.wav')

def play_move_sound():
    if 'move_sound' in globals():
        move_sound.play()

def play_capture_sound():
    if 'capture_sound' in globals():
        capture_sound.play()

def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return "{:02d}:{:02d}".format(minutes, seconds)