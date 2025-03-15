import pygame
import random
import itertools

# Inisialisasi pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 500, 500
COLOR_CYCLE = itertools.cycle([(255, 182, 193), (255, 105, 180), (219, 112, 147), (255, 20, 147), (255, 192, 203)])  # Warna pink dominan
WHITE = (255, 255, 255)
FONT_PATH = "./PressStart2P-Regular.ttf"

# Setup tampilan layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Tebak Angka - Pink Edition")

# Load Font
font = pygame.font.Font(FONT_PATH, 16)

# Load Sound
pygame.mixer.init()
success_sound = pygame.mixer.Sound("successed-295058.mp3")  
error_sound = pygame.mixer.Sound("error-126627.mp3")
pygame.mixer.music.load("sound_game.mp3")  
pygame.mixer.music.play(-1) 

# Angka rahasia
angka_rahasia = random.randint(1, 1000)
percobaan = 0
input_text = ""
hasil_tebakan = ""
warna_teks = next(COLOR_CYCLE)

# Fungsi untuk menggambar teks dengan efek bayangan dan rata tengah
def draw_text(text, y, color=WHITE):
    shadow_offset = 3
    shadow_color = (50, 50, 50)
    render_shadow = font.render(text, True, shadow_color)
    render_text = font.render(text, True, color)
    text_rect = render_text.get_rect(center=(WIDTH // 2, y))
    shadow_rect = render_shadow.get_rect(center=(WIDTH // 2 + shadow_offset, y + shadow_offset))
    screen.blit(render_shadow, shadow_rect.topleft)
    screen.blit(render_text, text_rect.topleft)

# Fungsi untuk menggambar background gradient pink
def draw_gradient():
    for i in range(HEIGHT):
        color = (
            int(255 - (50 * (i / HEIGHT))),  # Merah
            int(100 + (50 * (i / HEIGHT))),  # Hijau 
            int(150 + (100 * (i / HEIGHT)))  # Biru
        )
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

running = True
frame_counter = 0
while running:
    screen.fill((255, 182, 193))  # Latar belakang pink pastel
    draw_gradient()
    
    draw_text("Tebak Angka (1 - 1000)", 50, warna_teks)
    draw_text("Masukkan Tebakan:", 120, WHITE)
    draw_text(input_text, 160, warna_teks)
    draw_text(hasil_tebakan, 220, warna_teks)
    
    pygame.display.flip()
    
    frame_counter += 1
    if frame_counter % 30 == 0:  # Ubah warna teks setiap 30 frame
        warna_teks = next(COLOR_CYCLE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    tebakan = int(input_text)
                    percobaan += 1
                    if tebakan < angka_rahasia:
                        hasil_tebakan = "Terlalu Kecil!"
                        error_sound.play()
                    elif tebakan > angka_rahasia:
                        hasil_tebakan = "Terlalu Besar!"
                        error_sound.play()
                    else:
                        hasil_tebakan = f"Selamat! ({percobaan} percobaan)"
                        success_sound.play()
                        angka_rahasia = random.randint(1, 1000)
                        percobaan = 0
                    input_text = ""
                except ValueError:
                    hasil_tebakan = "Masukkan angka valid!"
                    error_sound.play()
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if event.unicode.isdigit():
                    input_text += event.unicode
    
pygame.quit()
