import pygame
import random
import math
import Paraules
from IntroIdiomes import ARAB, CAST, ANG, RUM, XIN

# Inicialització de Pygame
pygame.init()
pygame.font.init()

# Configuració de la finestra
WIDTH, HEIGHT = 1080, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Aprèn Català")
CLOCK = pygame.time.Clock()

def make_fonts(height):
    return (
        pygame.font.SysFont("Gill Sans", max(24, int(height * 0.07)), bold=True),
        pygame.font.SysFont("Gill Sans", max(18, int(height * 0.045))),
        pygame.font.SysFont("Gill Sans", max(14, int(height * 0.035))),
        pygame.font.SysFont("Gill Sans", max(12, int(height * 0.03))),
    )

FONT_LARGE, FONT_MEDIUM, FONT_SMALL, FONT_TINY = make_fonts(HEIGHT)

# Colors i estètica
COLORS = {
    "background": (18, 24, 42),
    "panel": (24, 32, 54),
    "accent": (248, 164, 53),
    "accent_soft": (68, 152, 210),
    "text": (240, 242, 248),
    "muted": (164, 173, 196),
    "button": (40, 95, 170),
    "button_hover": (64, 138, 219),
    "wrong": (210, 82, 82),
    "right": (86, 190, 112),
}

FONT_LARGE = pygame.font.SysFont("Gill Sans", 52, bold=True)
FONT_MEDIUM = pygame.font.SysFont("Gill Sans", 32)
FONT_SMALL = pygame.font.SysFont("Gill Sans", 24)
FONT_TINY = pygame.font.SysFont("Gill Sans", 20)

LANGUAGES = [
    {"id": "marroc", "name": "Marroc", "label": "العربية", "accent": (194, 115, 61)},
    {"id": "colombia", "name": "Colòmbia", "label": "Español", "accent": (220, 84, 63)},
    {"id": "italia", "name": "Itàlia", "label": "Italiano", "accent": (77, 155, 96)},
    {"id": "xina", "name": "Xina", "label": "中文", "accent": (198, 61, 70)},
    {"id": "romania", "name": "Romania", "label": "Română", "accent": (74, 131, 204)},
]

MESSAGES = {
    "marroc": {
        "welcome": "اختر لغتك لتبدأ درسًا بسيطًا من الكتالانية",
        "instruction": "اضغط على الكلمة الكتالانية الصحيحة التي تتوافق مع الرسم.",
        "next": "Següent",
        "retry": "Torna-ho a provar",
        "score": "Punts",
    },
    "colombia": {
        "welcome": "Elige tu idioma para empezar una lección de catalán",
        "instruction": "Haz clic en la palabra catalana correcta que coincide con el dibujo.",
        "next": "Siguiente",
        "retry": "Intentar de nuevo",
        "score": "Puntos",
    },
    "italia": {
        "welcome": "Scegli la tua lingua per iniziare una lezione di catalano",
        "instruction": "Clicca sulla parola catalana corretta che corrisponde al disegno.",
        "next": "Avanti",
        "retry": "Riprova",
        "score": "Punti",
    },
    "xina": {
        "welcome": "请选择您的语言，开始加泰罗尼亚语课程",
        "instruction": "点击与图画匹配的正确加泰罗尼亚语单词。",
        "next": "下一步",
        "retry": "再试一次",
        "score": "得分",
    },
    "romania": {
        "welcome": "Alege limba pentru a începe o lecție de catalană",
        "instruction": "Apasă cuvântul catalan corect care se potrivește cu pictograma.",
        "next": "Următor",
        "retry": "Reîncearcă",
        "score": "Puncte",
    },
}

# Introduccions en varis idiomes
INTRODUCTIONS = {
    "marroc": ARAB,
    "colombia": CAST,
    "italia": ANG,
    "xina": XIN,
    "romania": RUM,
}

VOCABULARY = [
    {
        "catala": "Hola",
        "category": "Salutacions",
        "icon": "wave",
        "translations": {
            "marroc": "مرحبا",
            "colombia": "Hola",
            "italia": "Ciao",
            "xina": "你好",
            "romania": "Salut",
        },
    },
    {
        "catala": "Adéu",
        "category": "Salutacions",
        "icon": "wing",
        "translations": {
            "marroc": "مع السلامة",
            "colombia": "Adiós",
            "italia": "Ciao",
            "xina": "再见",
            "romania": "La revedere",
        },
    },
    {
        "catala": "Gràcies",
        "category": "Cordial",
        "icon": "heart",
        "translations": {
            "marroc": "شكرا",
            "colombia": "Gracias",
            "italia": "Grazie",
            "xina": "谢谢",
            "romania": "Mulțumesc",
        },
    },
    {
        "catala": "Roig",
        "category": "Colors",
        "icon": "circle",
        "translations": {
            "marroc": "أحمر",
            "colombia": "Rojo",
            "italia": "Rosso",
            "xina": "红色",
            "romania": "Roșu",
        },
    },
    {
        "catala": "Blau",
        "category": "Colors",
        "icon": "drop",
        "translations": {
            "marroc": "أزرق",
            "colombia": "Azul",
            "italia": "Blu",
            "xina": "蓝色",
            "romania": "Albastru",
        },
    },
    {
        "catala": "Verd",
        "category": "Colors",
        "icon": "leaf",
        "translations": {
            "marroc": "أخضر",
            "colombia": "Verde",
            "italia": "Verde",
            "xina": "绿色",
            "romania": "Verde",
        },
    },
    {
        "catala": "Un",
        "category": "Nombres",
        "icon": "one",
        "translations": {
            "marroc": "واحد",
            "colombia": "Uno",
            "italia": "Uno",
            "xina": "一",
            "romania": "Unu",
        },
    },
    {
        "catala": "Dos",
        "category": "Nombres",
        "icon": "two",
        "translations": {
            "marroc": "اثنان",
            "colombia": "Dos",
            "italia": "Due",
            "xina": "二",
            "romania": "Doi",
        },
    },
    {
        "catala": "Tres",
        "category": "Nombres",
        "icon": "three",
        "translations": {
            "marroc": "ثلاثة",
            "colombia": "Tres",
            "italia": "Tre",
            "xina": "三",
            "romania": "Trei",
        },
    },
]

STATE = {
    "screen": "menu",
    "language": None,
    "question": None,
    "options": [],
    "score": 0,
    "round": 0,
    "feedback": None,
    "intro_fade": 0,  # Para animación de fade-in
}

BUTTONS = []


def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def draw_background(surface):
    for y in range(0, HEIGHT, 3):
        ratio = y / HEIGHT
        color = lerp_color(COLORS["background"], (30, 42, 78), ratio)
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

    for i in range(3):
        radius = 220 + i * 80
        alpha = max(10, 70 - i * 20)
        circle_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(circle_surf, (*COLORS["accent"], alpha), (radius, radius), radius)
        surface.blit(circle_surf, (WIDTH - radius - 120, HEIGHT - radius - 140))


def draw_text(surface, text, font, color, pos, align="topleft"):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(**{align: pos})
    surface.blit(rendered, rect)
    return rect


def resize_window(width, height):
    global WIDTH, HEIGHT, WINDOW, FONT_LARGE, FONT_MEDIUM, FONT_SMALL, FONT_TINY
    WIDTH = max(800, min(1080, width))
    HEIGHT = max(560, min(720, height))
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    FONT_LARGE, FONT_MEDIUM, FONT_SMALL, FONT_TINY = make_fonts(HEIGHT)


def draw_button(surface, rect, text, hover=False, color=None):
    if color is None:
        color = COLORS["button_hover"] if hover else COLORS["button"]
    border = COLORS["accent"] if hover else COLORS["muted"]
    pygame.draw.rect(surface, color, rect, border_radius=18)
    pygame.draw.rect(surface, border, rect, width=3, border_radius=18)
    draw_text(surface, text, FONT_MEDIUM, COLORS["text"], rect.center, align="center")


def draw_pictogram(surface, rect, icon):
    # Dibuixa un rectangle com a pictograma de mostra
    pygame.draw.rect(surface, COLORS["accent"], rect.inflate(-rect.width * 0.3, -rect.height * 0.3), border_radius=14)


def make_question(language_key):
    question = random.choice(VOCABULARY)
    choices = {question["translations"][language_key]: question}
    other_items = [item for item in VOCABULARY if item is not question]
    random.shuffle(other_items)
    while len(choices) < 4:
        candidate = other_items.pop()
        translation = candidate["translations"][language_key]
        if translation not in choices:
            choices[translation] = candidate
    items = list(choices.items())
    random.shuffle(items)
    return {
        "question": question,
        "options": [label for label, _ in items],
        "correct": question["translations"][language_key],
        "answers": {label: item for label, item in items},
    }


def start_round():
    STATE["question_data"] = make_question(STATE["language"])
    STATE["feedback"] = None
    STATE["round"] += 1


def draw_menu(mouse_pos):
    WINDOW.fill(COLORS["background"])
    draw_background(WINDOW)

    margin_x = int(WIDTH * 0.08)
    margin_y = int(HEIGHT * 0.08)
    overlay_width = WIDTH - margin_x * 2
    overlay_height = HEIGHT - margin_y - 40
    overlay = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
    pygame.draw.rect(
        overlay,
        (*COLORS["panel"], 240),
        (0, 0, overlay_width, overlay_height),
        border_radius=24,
    )
    WINDOW.blit(overlay, (margin_x, margin_y // 2))

    title_x = margin_x + 20
    draw_text(WINDOW, "Laboratori Català", FONT_LARGE, COLORS["accent"], (title_x, margin_y))
    draw_text(
        WINDOW,
        "Un joc per aprendre amb pictogrames i paraules",
        FONT_MEDIUM,
        COLORS["muted"],
        (title_x, margin_y + 70),
    )

    y = margin_y + 150
    draw_text(WINDOW, "Selecciona el teu idioma / اختر لغتك / Elige idioma", FONT_SMALL, COLORS["text"], (title_x, y))
    y += int(HEIGHT * 0.08)

    BUTTONS.clear()
    button_width = min(360, overlay_width - 60)
    button_height = int(HEIGHT * 0.08)
    button_gap = int(HEIGHT * 0.02)
    for index, lang in enumerate(LANGUAGES):
        btn_rect = pygame.Rect(title_x, y + index * (button_height + button_gap), button_width, button_height)
        label = f"{lang['label']} — {lang['name']}"
        hover = btn_rect.collidepoint(mouse_pos)
        draw_button(
            WINDOW,
            btn_rect,
            label,
            hover=hover,
            color=lang["accent"] if hover else COLORS["panel"],
        )
        BUTTONS.append((btn_rect, lang["id"]))

    draw_text(
        WINDOW,
        "Pensa en on viu el teu estudiant: Marroc, Colòmbia, Itàlia, Xina o Romania.",
        FONT_SMALL,
        COLORS["muted"],
        (title_x, HEIGHT - margin_y // 2 - 10),
    )


def draw_intro(mouse_pos):
    WINDOW.fill(COLORS["background"])
    draw_background(WINDOW)

    # Animació de fade-in
    if STATE["intro_fade"] < 1:
        STATE["intro_fade"] = min(1, STATE["intro_fade"] + 0.03)
    
    margin = int(WIDTH * 0.06)
    overlay_width = WIDTH - margin * 2
    overlay_height = HEIGHT - margin * 2
    
    # Creem una superfície amb transparència per la animació
    overlay = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
    alpha = int(230 * STATE["intro_fade"])
    pygame.draw.rect(
        overlay,
        (*COLORS["panel"], alpha),
        (0, 0, overlay_width, overlay_height),
        border_radius=24,
    )
    WINDOW.blit(overlay, (margin, margin))

    lang_key = STATE["language"]
    intro_text = INTRODUCTIONS[lang_key]
    
    # Títol amb color de l'idioma
    lang_data = next(l for l in LANGUAGES if l["id"] == lang_key)
    accent_color = lang_data["accent"]
    
    text_x = margin + 30
    text_y = margin + 30
    
    # Títol decoratiu
    draw_text(WINDOW, "📚 Benvingut/da 📚", FONT_LARGE, accent_color, (text_x, text_y))
    
    # Text de introducció amb wrapping
    text_y += 80
    line_height = int(FONT_SMALL.get_linesize() * 1.3)
    max_width = overlay_width - 60
    
    # Divideix el text en línies
    words = intro_text.split()
    current_line = ""
    lines = []
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if FONT_SMALL.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Dibuixa les línies amb fade-in escalonada
    for idx, line in enumerate(lines):
        fade_delay = idx * 0.05
        if STATE["intro_fade"] > fade_delay:
            line_alpha = min(1, (STATE["intro_fade"] - fade_delay) / 0.3)
            color_with_alpha = tuple(int(c * line_alpha) for c in COLORS["text"][:3])
            draw_text(WINDOW, line, FONT_SMALL, color_with_alpha, (text_x, text_y))
        text_y += line_height
    
    # Botó per continuar
    text_y += 20
    btn_width = min(300, overlay_width - 60)
    btn_height = int(HEIGHT * 0.08)
    btn_rect = pygame.Rect(
        WIDTH // 2 - btn_width // 2,
        min(text_y, HEIGHT - margin - btn_height - 20),
        btn_width,
        btn_height
    )
    
    hover = btn_rect.collidepoint(mouse_pos)
    draw_button(WINDOW, btn_rect, "Comença! ▶", hover=hover, color=accent_color if hover else COLORS["button"])
    
    BUTTONS.clear()
    BUTTONS.append((btn_rect, "start_game"))



def draw_task(mouse_pos):
    WINDOW.fill(COLORS["background"])
    draw_background(WINDOW)

    margin = int(WIDTH * 0.06)
    overlay_width = WIDTH - margin * 2
    overlay_height = HEIGHT - margin * 2
    overlay = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
    pygame.draw.rect(
        overlay,
        (*COLORS["panel"], 230),
        (0, 0, overlay_width, overlay_height),
        border_radius=24,
    )
    WINDOW.blit(overlay, (margin, margin))

    lang_key = STATE["language"]
    msg = MESSAGES[lang_key]
    text_x = margin + 20
    draw_text(WINDOW, msg["welcome"], FONT_MEDIUM, COLORS["accent"], (text_x, margin + 20))
    draw_text(WINDOW, msg["instruction"], FONT_SMALL, COLORS["muted"], (text_x, margin + 80))

    question = STATE["question_data"]["question"]
    card_width = min(int(overlay_width * 0.42), 420)
    card_height = int(overlay_height * 0.33)
    card_rect = pygame.Rect(text_x, margin + 120, card_width, card_height)
    pygame.draw.rect(WINDOW, (28, 36, 62), card_rect, border_radius=24)
    pygame.draw.rect(WINDOW, COLORS["muted"], card_rect, width=2, border_radius=24)
    draw_text(WINDOW, question["category"], FONT_SMALL, COLORS["accent"], (card_rect.left + 24, card_rect.top + 20))
    draw_text(
        WINDOW,
        question["catala"],
        FONT_LARGE,
        COLORS["text"],
        (card_rect.centerx, card_rect.top + 110),
        align="center",
    )

    icon_area = pygame.Rect(
        card_rect.left + 50,
        card_rect.top + int(card_rect.height * 0.42),
        card_rect.width - 100,
        int(card_rect.height * 0.25),
    )
    draw_pictogram(WINDOW, icon_area, question["icon"])

    answers = STATE["question_data"]["options"]
    BUTTONS.clear()
    button_height = max(40, int(HEIGHT * 0.075))
    button_gap = max(8, int(HEIGHT * 0.015))
    available_width = overlay_width - card_width - 60
    grid_mode = available_width >= 260
    if grid_mode:
        btn_width = min(int(available_width / 2) - 10, 300)
        for index, answer in enumerate(answers):
            row = index // 2
            col = index % 2
            btn_rect = pygame.Rect(
                card_rect.right + 30 + col * (btn_width + 20),
                card_rect.top + row * (button_height + button_gap),
                btn_width,
                button_height,
            )
            hover = btn_rect.collidepoint(mouse_pos)
            draw_button(WINDOW, btn_rect, answer, hover=hover)
            BUTTONS.append((btn_rect, answer))
    else:
        btn_width = overlay_width - 40
        for index, answer in enumerate(answers):
            btn_rect = pygame.Rect(
                text_x,
                card_rect.bottom + 30 + index * (button_height + button_gap),
                btn_width,
                button_height,
            )
            hover = btn_rect.collidepoint(mouse_pos)
            draw_button(WINDOW, btn_rect, answer, hover=hover)
            BUTTONS.append((btn_rect, answer))

    if STATE["feedback"]:
        color = COLORS["right"] if STATE["feedback"] == "right" else COLORS["wrong"]
        text = "Correcte!" if STATE["feedback"] == "right" else "Mala resposta"
        draw_text(WINDOW, text, FONT_MEDIUM, color, (text_x, HEIGHT - margin - 40))

    status = f"{msg['score']}: {STATE['score']}    Ronda: {STATE['round']} / 5"
    draw_text(WINDOW, status, FONT_SMALL, COLORS["muted"], (text_x, HEIGHT - margin - 80))


def draw_result(mouse_pos):
    WINDOW.fill(COLORS["background"])
    draw_background(WINDOW)

    margin = int(WIDTH * 0.08)
    overlay_width = WIDTH - margin * 2
    overlay_height = HEIGHT - margin * 2
    overlay = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
    pygame.draw.rect(
        overlay,
        (*COLORS["panel"], 245),
        (0, 0, overlay_width, overlay_height),
        border_radius=28,
    )
    WINDOW.blit(overlay, (margin, margin))

    lang_key = STATE["language"]
    msg = MESSAGES[lang_key]
    title_x = margin + 30
    draw_text(WINDOW, "Final de la ronda", FONT_LARGE, COLORS["accent"], (title_x, margin + 40))
    draw_text(WINDOW, f"{msg['score']}: {STATE['score']} / 5", FONT_MEDIUM, COLORS["text"], (title_x, margin + 140))
    draw_text(WINDOW, msg["retry"], FONT_SMALL, COLORS["muted"], (title_x, margin + 200))

    btn_width = min(320, overlay_width - 80)
    btn_height = int(HEIGHT * 0.11)
    btn_rect = pygame.Rect(WIDTH // 2 - btn_width // 2, HEIGHT - margin - btn_height - 20, btn_width, btn_height)
    hover = btn_rect.collidepoint(mouse_pos)
    draw_button(WINDOW, btn_rect, msg["retry"], hover=hover)
    BUTTONS.clear()
    BUTTONS.append((btn_rect, "restart"))


def handle_click(pos):
    for rect, value in BUTTONS:
        if rect.collidepoint(pos):
            if STATE["screen"] == "menu":
                STATE["language"] = value
                STATE["screen"] = "intro"
                STATE["intro_fade"] = 0  # Inicia l'animació
            elif STATE["screen"] == "intro":
                if value == "start_game":
                    STATE["screen"] = "task"
                    STATE["score"] = 0
                    STATE["round"] = 0
                    start_round()
            elif STATE["screen"] == "task":
                correct = STATE["question_data"]["correct"]
                if value == correct:
                    STATE["score"] += 1
                    STATE["feedback"] = "right"
                else:
                    STATE["feedback"] = "wrong"
                if STATE["round"] >= 5:
                    STATE["screen"] = "result"
                else:
                    pygame.time.set_timer(pygame.USEREVENT + 1, 800)
            elif STATE["screen"] == "result" and value == "restart":
                STATE["screen"] = "menu"
                STATE["language"] = None
                STATE["question_data"] = None
                STATE["feedback"] = None


def main():
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                resize_window(event.w, event.h)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_click(event.pos)
            elif event.type == pygame.USEREVENT + 1:
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)
                if STATE["screen"] == "task":
                    start_round()

        if STATE["screen"] == "menu":
            draw_menu(mouse_pos)
        elif STATE["screen"] == "intro":
            draw_intro(mouse_pos)
        elif STATE["screen"] == "task":
            draw_task(mouse_pos)
        elif STATE["screen"] == "result":
            draw_result(mouse_pos)

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

