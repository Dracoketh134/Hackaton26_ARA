import pygame
import random
import math

# Inicialització de Pygame
pygame.init()
pygame.font.init()

# Configuració de la finestra
WIDTH, HEIGHT = 1080, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aprèn Català")
CLOCK = pygame.time.Clock()

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


def draw_button(surface, rect, text, hover=False, color=None):
    if color is None:
        color = COLORS["button_hover"] if hover else COLORS["button"]
    border = COLORS["accent"] if hover else COLORS["muted"]
    pygame.draw.rect(surface, color, rect, border_radius=18)
    pygame.draw.rect(surface, border, rect, width=3, border_radius=18)
    draw_text(surface, text, FONT_MEDIUM, COLORS["text"], rect.center, align="center")


def draw_pictogram(surface, rect, icon):
    if icon == "wave":
        points = [
            (rect.left + 0.2 * rect.width, rect.centery),
            (rect.left + 0.45 * rect.width, rect.top + 0.3 * rect.height),
            (rect.left + 0.7 * rect.width, rect.bottom - 0.25 * rect.height),
            (rect.right - 0.2 * rect.width, rect.centery),
        ]
        pygame.draw.lines(surface, COLORS["accent"], False, points, 10)
    elif icon == "wing":
        pygame.draw.arc(surface, COLORS["accent"], rect.inflate(-rect.width * 0.3, -rect.height * 0.2), math.pi / 2, 2.5, 14)
        pygame.draw.arc(surface, COLORS["accent"], rect.inflate(-rect.width * 0.55, -rect.height * 0.5), math.pi / 2.7, 2.4, 12)
    elif icon == "heart":
        left = pygame.Rect(rect.left + rect.width * 0.18, rect.top + rect.height * 0.15, rect.width * 0.28, rect.height * 0.35)
        right = pygame.Rect(rect.left + rect.width * 0.54, rect.top + rect.height * 0.15, rect.width * 0.28, rect.height * 0.35)
        pygame.draw.ellipse(surface, COLORS["accent"], left)
        pygame.draw.ellipse(surface, COLORS["accent"], right)
        points = [
            (rect.left + rect.width * 0.2, rect.top + rect.height * 0.4),
            (rect.centerx, rect.bottom - rect.height * 0.15),
            (rect.right - rect.width * 0.2, rect.top + rect.height * 0.4),
        ]
        pygame.draw.polygon(surface, COLORS["accent"], points)
    elif icon == "circle":
        pygame.draw.circle(surface, COLORS["accent"], rect.center, int(rect.width * 0.3))
    elif icon == "drop":
        droppoints = [
            (rect.centerx, rect.top + rect.height * 0.1),
            (rect.left + rect.width * 0.3, rect.top + rect.height * 0.55),
            (rect.centerx, rect.bottom - rect.height * 0.12),
            (rect.right - rect.width * 0.3, rect.top + rect.height * 0.55),
        ]
        pygame.draw.polygon(surface, COLORS["accent"], droppoints)
    elif icon == "leaf":
        pygame.draw.ellipse(surface, COLORS["accent"], rect.inflate(-rect.width * 0.4, -rect.height * 0.15))
        pygame.draw.polygon(surface, COLORS["accent"], [
            (rect.centerx - rect.width * 0.05, rect.top + rect.height * 0.35),
            (rect.centerx + rect.width * 0.05, rect.top + rect.height * 0.35),
            (rect.centerx, rect.bottom - rect.height * 0.13),
        ])
    elif icon in ["one", "two", "three"]:
        number = "1" if icon == "one" else "2" if icon == "two" else "3"
        draw_text(surface, number, FONT_LARGE, COLORS["accent"], rect.center, align="center")
    else:
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
    overlay = pygame.Surface((WIDTH - 140, HEIGHT - 100), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (*COLORS["panel"], 240), (0, 0, overlay.get_width(), overlay.get_height()), border_radius=24)
    WINDOW.blit(overlay, (70, 50))

    draw_text(WINDOW, "Laboratori Català", FONT_LARGE, COLORS["accent"], (130, 90))
    draw_text(WINDOW, "Un joc per aprendre amb pictogrames i paraules", FONT_MEDIUM, COLORS["muted"], (130, 160))

    y = 240
    draw_text(WINDOW, "Selecciona el teu idioma / اختر لغتك / Elige idioma", FONT_SMALL, COLORS["text"], (130, y))
    y += 50

    BUTTONS.clear()
    for index, lang in enumerate(LANGUAGES):
        btn_rect = pygame.Rect(130, y + index * 80, 280, 60)
        label = f"{lang['label']} — {lang['name']}"
        hover = btn_rect.collidepoint(mouse_pos)
        draw_button(WINDOW, btn_rect, label, hover=hover, color=lang["accent"] if hover else COLORS["panel"])
        if hover:
            if pygame.mouse.get_pressed()[0]:
                pass
        BUTTONS.append((btn_rect, lang["id"]))

    draw_text(WINDOW, "Pensa en on viu el teu estudiant: Marroc, Colòmbia, Itàlia, Xina o Romania.", FONT_SMALL, COLORS["muted"], (130, HEIGHT - 120))


def draw_task(mouse_pos):
    WINDOW.fill(COLORS["background"])
    draw_background(WINDOW)
    overlay = pygame.Surface((WIDTH - 120, HEIGHT - 100), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (*COLORS["panel"], 230), (0, 0, overlay.get_width(), overlay.get_height()), border_radius=24)
    WINDOW.blit(overlay, (60, 50))

    lang_key = STATE["language"]
    msg = MESSAGES[lang_key]
    draw_text(WINDOW, msg["welcome"], FONT_MEDIUM, COLORS["accent"], (90, 80))
    draw_text(WINDOW, msg["instruction"], FONT_SMALL, COLORS["muted"], (90, 130))

    question = STATE["question_data"]["question"]
    card_rect = pygame.Rect(120, 190, 380, 360)
    pygame.draw.rect(WINDOW, (28, 36, 62), card_rect, border_radius=24)
    pygame.draw.rect(WINDOW, COLORS["muted"], card_rect, width=2, border_radius=24)
    draw_text(WINDOW, question["category"], FONT_SMALL, COLORS["accent"], (card_rect.left + 24, card_rect.top + 20))
    draw_text(WINDOW, question["catala"], FONT_LARGE, COLORS["text"], (card_rect.centerx, card_rect.top + 130), align="center")

    icon_area = pygame.Rect(card_rect.left + 90, card_rect.top + 190, 200, 120)
    draw_pictogram(WINDOW, icon_area, question["icon"])

    answers = STATE["question_data"]["options"]
    BUTTONS.clear()
    for index, answer in enumerate(answers):
        btn_rect = pygame.Rect(550 + (index % 2) * 420, 220 + (index // 2) * 140, 380, 100)
        hover = btn_rect.collidepoint(mouse_pos)
        draw_button(WINDOW, btn_rect, answer, hover=hover)
        BUTTONS.append((btn_rect, answer))

    if STATE["feedback"]:
        color = COLORS["right"] if STATE["feedback"] == "right" else COLORS["wrong"]
        text = "Correcte!" if STATE["feedback"] == "right" else "Mala resposta"
        draw_text(WINDOW, text, FONT_MEDIUM, color, (90, HEIGHT - 120))

    status = f"{msg['score']}: {STATE['score']}    Ronda: {STATE['round']} / 5"
    draw_text(WINDOW, status, FONT_SMALL, COLORS["muted"], (90, HEIGHT - 190))


def draw_result(mouse_pos):
    WINDOW.fill(COLORS["background"])
    draw_background(WINDOW)
    overlay = pygame.Surface((WIDTH - 240, HEIGHT - 200), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (*COLORS["panel"], 245), (0, 0, overlay.get_width(), overlay.get_height()), border_radius=28)
    WINDOW.blit(overlay, (120, 100))

    lang_key = STATE["language"]
    msg = MESSAGES[lang_key]
    draw_text(WINDOW, "Final de la ronda", FONT_LARGE, COLORS["accent"], (260, 150))
    draw_text(WINDOW, f"{msg['score']}: {STATE['score']} / 5", FONT_MEDIUM, COLORS["text"], (260, 240))
    draw_text(WINDOW, msg["retry"], FONT_SMALL, COLORS["muted"], (260, 320))

    btn_rect = pygame.Rect(620, 330, 320, 90)
    hover = btn_rect.collidepoint(mouse_pos)
    draw_button(WINDOW, btn_rect, msg["retry"], hover=hover)
    BUTTONS.clear()
    BUTTONS.append((btn_rect, "restart"))


def handle_click(pos):
    for rect, value in BUTTONS:
        if rect.collidepoint(pos):
            if STATE["screen"] == "menu":
                STATE["language"] = value
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_click(event.pos)
            elif event.type == pygame.USEREVENT + 1:
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)
                if STATE["screen"] == "task":
                    start_round()

        if STATE["screen"] == "menu":
            draw_menu(mouse_pos)
        elif STATE["screen"] == "task":
            draw_task(mouse_pos)
        elif STATE["screen"] == "result":
            draw_result(mouse_pos)

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

