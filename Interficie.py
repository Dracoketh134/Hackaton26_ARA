import pygame


# Inicialització de Pygame

pygame.init()
pygame.font.init()


# Configuració de la finestra i els elements de la interfície

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Front Page")


# Configuració del botó i el text

FONT = pygame.font.SysFont(None, 48)
BUTTON_TEXT = FONT.render("START", True, (255, 255, 255))
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 80
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 160, 210)
BUTTON_RECT = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, (HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

BACKGROUND_COLOR = (30, 30, 30)
SHOW_TEXT = False
MESSAGE_TEXT = FONT.render("Button clicked!", True, (255, 255, 255))

running = True

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not SHOW_TEXT and BUTTON_RECT.collidepoint(mouse_pos):
                SHOW_TEXT = True

    WINDOW.fill(BACKGROUND_COLOR)

    if not SHOW_TEXT:
        button_color = BUTTON_HOVER_COLOR if BUTTON_RECT.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(WINDOW, button_color, BUTTON_RECT, border_radius=12)

        text_rect = BUTTON_TEXT.get_rect(center=BUTTON_RECT.center)
        WINDOW.blit(BUTTON_TEXT, text_rect)
    else:
        message_rect = MESSAGE_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WINDOW.blit(MESSAGE_TEXT, message_rect)

    pygame.display.flip()

pygame.quit()

