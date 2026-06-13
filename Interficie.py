import pygame

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Front Page")

FONT = pygame.font.SysFont(None, 48)
BUTTON_TEXT = FONT.render("START", True, (255, 255, 255))
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 80
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 160, 210)
BUTTON_RECT = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, (HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

BACKGROUND_COLOR = (30, 30, 30)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if BUTTON_RECT.collidepoint(mouse_pos):
                print("Start button clicked")

    WINDOW.fill(BACKGROUND_COLOR)

    button_color = BUTTON_HOVER_COLOR if BUTTON_RECT.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(WINDOW, button_color, BUTTON_RECT, border_radius=12)

    text_rect = BUTTON_TEXT.get_rect(center=BUTTON_RECT.center)
    WINDOW.blit(BUTTON_TEXT, text_rect)

    pygame.display.flip()

pygame.quit()

