# BEDWARS: ПОСЛЕДНЯЯ КРОВАТЬ
# Визуальная новелла для Ren'Py
# Автор сценария: Артём
# Версия с музыкой и звуками

# ============================================
# ИНИЦИАЛИЗАЦИЯ
# ============================================

init python:
    # Система кармы
    karma = 0
    has_yellow_wool = False

# ============================================
# ТРАНСФОРМАЦИИ (для зума CG)
# ============================================
define flash = Fade(0.1, 0.0, 0.1, color="#fff")

transform slow_zoom_in:
    zoom 1.0
    linear 29.0 zoom 1.15

transform center_zoom:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    linear 29.0 zoom 1.15

# Трансформация для уменьшения персонажей (65% от оригинального размера)
transform character_scale:
    zoom 0.65

# Трансформации для затемнения и подсветки персонажей
transform dim_character:
    matrixcolor BrightnessMatrix(-0.3)

transform highlight_character:
    matrixcolor BrightnessMatrix(0.0)

# Комбинированные трансформации: позиция + масштаб
transform char_center:
    xalign 0.5
    yalign 1.0
    zoom 0.65

transform char_left:
    xalign 0.2
    yalign 1.0
    zoom 0.65

transform char_right:
    xalign 0.8
    yalign 1.0
    zoom 0.65

# Комбинированные трансформации: позиция + масштаб + подсветка
transform char_center_speaking:
    xalign 0.5
    yalign 1.0
    zoom 0.65
    matrixcolor BrightnessMatrix(0.0)

transform char_left_speaking:
    xalign 0.2
    yalign 1.0
    zoom 0.65
    matrixcolor BrightnessMatrix(0.0)

transform char_right_speaking:
    xalign 0.8
    yalign 1.0
    zoom 0.65
    matrixcolor BrightnessMatrix(0.0)

# Комбинированные трансформации: позиция + масштаб + затемнение
transform char_center_silent:
    xalign 0.5
    yalign 1.0
    zoom 0.65
    matrixcolor BrightnessMatrix(-0.3)

transform char_left_silent:
    xalign 0.2
    yalign 1.0
    zoom 0.65
    matrixcolor BrightnessMatrix(-0.3)

transform char_right_silent:
    xalign 0.8
    yalign 1.0
    zoom 0.65
    matrixcolor BrightnessMatrix(-0.3)

# ============================================
# СИСТЕМА АВТОМАТИЧЕСКОЙ ПОДСВЕТКИ ПЕРСОНАЖЕЙ
# ============================================

init -1 python:
    # Callback функция для подсветки говорящего персонажа
    def highlight_speaking_character(who, *args, **kwargs):
        """
        Автоматически подсвечивает говорящего персонажа
        и затемняет остальных
        """
        # Маппинг имен персонажей на теги изображений
        character_tags = {
            "Марк": "mark",
            "Карпик": "karpik",
            "Маяковский": "mayakovsky"
        }

        if who and who in character_tags:
            speaking_tag = character_tags[who]

            # Получаем список всех отображаемых персонажей
            for tag in ["mark", "karpik", "mayakovsky"]:
                if renpy.showing(tag):
                    # Определяем позицию персонажа
                    layer_at_list = renpy.get_at_list(tag)

                    if layer_at_list:
                        current_transform = str(layer_at_list[0])

                        # Определяем нужную трансформацию
                        transform_name = None

                        # Если это говорящий персонаж - подсвечиваем
                        if tag == speaking_tag:
                            if "char_left" in current_transform:
                                transform_name = "char_left_speaking"
                            elif "char_right" in current_transform:
                                transform_name = "char_right_speaking"
                            elif "char_center" in current_transform:
                                transform_name = "char_center_speaking"
                        # Иначе - затемняем
                        else:
                            if "char_left" in current_transform:
                                transform_name = "char_left_silent"
                            elif "char_right" in current_transform:
                                transform_name = "char_right_silent"
                            elif "char_center" in current_transform:
                                transform_name = "char_center_silent"

                        # Применяем трансформацию
                        if transform_name:
                            try:
                                transform_obj = eval(transform_name)
                                renpy.show(tag, at_list=[transform_obj], layer="master")
                            except:
                                pass

        # ВАЖНО: callback должен вернуть args и kwargs
        return args, kwargs

    # Устанавливаем callback
    config.say_arguments_callback = highlight_speaking_character

# ============================================
# ОПРЕДЕЛЕНИЕ ПЕРСОНАЖЕЙ
# ============================================

define m = Character("Марк", color="#55ff55")
define m_inner = Character("Марк", color="#55ff55", what_prefix='"', what_suffix='"', what_italic=True)
define k = Character("Карпик", color="#5555ff")
define may = Character("Маяковский", color="#ffff55")
define narrator = Character(None)

# ============================================
# ОПРЕДЕЛЕНИЕ ИЗОБРАЖЕНИЙ
# ============================================

# Фоны
image bg diamond_island = "bg/bg_diamond_island.png"
image bg green_island_destroyed = "bg/bg_green_island_destroyed.png"
image bg blue_island = "bg/bg_blue_island.png"
image bg red_island = "bg/bg_red_island.png"
image bg center_island = "bg/bg_center_island.png"
image bg center_battle = "bg/bg_center_battle.png"
image bg sky_battle = "bg/bg_sky_battle.png"
image bg sky_ceiling = "bg/bg_sky_ceiling.png"
image bg sky_broken = "bg/bg_sky_broken.png"
image bg bedroom = "bg/bg_bedroom.png"
image bg black = "bg/bg_black.png"
image cg book_ending = "cg/cg_book_ending.png"

# Марк
image mark idle = "mark/mark_idle.png"
image mark confident = "mark/mark_confident.png"
image mark walking = "mark/mark_walking.png"
image mark running = "mark/mark_running.png"
image mark building = "mark/mark_building.png"
image mark collecting = "mark/mark_collecting.png"
image mark looting = "mark/mark_looting.png"
image mark examining = "mark/mark_examining.png"
image mark fighting = "mark/mark_fighting.png"
image mark defending = "mark/mark_defending.png"
image mark placing_water = "mark/mark_placing_water.png"
image mark shocked = "mark/mark_shocked.png"
image mark angry = "mark/mark_angry.png"
image mark scared = "mark/mark_scared.png"
image mark pleading = "mark/mark_pleading.png"
image mark determined = "mark/mark_determined.png"
image mark thinking = "mark/mark_thinking.png"
image mark suspicious = "mark/mark_suspicious.png"
image mark relieved = "mark/mark_relieved.png"
image mark facepalm = "mark/mark_facepalm.png"
image mark falling = "mark/mark_falling.png"
image mark climbing = "mark/mark_climbing.png"
image mark reaching_down = "mark/mark_reaching_down.png"
image mark eating_apple = "mark/mark_eating_apple.png"
image mark defeated = "mark/mark_defeated.png"
image mark waking = "mark/mark_waking.png"
image mark hanging = "mark/mark_hanging.png"

# Карпик
image karpik smug = "karpik/karpik_smug.png"
image karpik aggressive = "karpik/karpik_aggressive.png"
image karpik friendly = "karpik/karpik_friendly.png"
image karpik hanging = "karpik/karpik_hanging.png"
image karpik falling = "karpik/karpik_falling.png"

# Маяковский
image mayakovsky menacing = "mayakovsky/mayakovsky_menacing.png"
image mayakovsky battle = "mayakovsky/mayakovsky_battle.png"
image mayakovsky listening = "mayakovsky/mayakovsky_listening.png"
image mayakovsky neutral = "mayakovsky/mayakovsky_neutral.png"
image mayakovsky back = "mayakovsky/mayakovsky_back.png"

# ============================================
# ОПРЕДЕЛЕНИЕ МУЗЫКИ И ЗВУКОВ
# ============================================

define audio.menu_music = "audio/menu.mp3"
define audio.tension_music = "audio/tension.mp3"
define audio.battle_music = "audio/battle.mp3"
define audio.sad_music = "audio/sad.mp3"
define audio.escape_music = "audio/escape.mp3"
define audio.peaceful_music = "audio/peaceful.mp3"
define audio.final_cg_music = "audio/final_cg.mp3"

define audio.beep_sound = "audio/beep.ogg"
define audio.explosion_sound = "audio/explosion.ogg"
define audio.sword_sound = "audio/sword.ogg"

# ============================================
# НАЧАЛО ИГРЫ
# ============================================

label start:
    
    $ karma = 0
    $ has_yellow_wool = False
    
    # -----------------------------------------
    # ПРОЛОГ
    # -----------------------------------------
    
    play music tension_music fadeout 1.0 fadein 2.0 volume 0.8
    
    scene bg diamond_island with fade
    
    centered "{size=+10}BEDWARS: ПОСЛЕДНЯЯ КРОВАТЬ{/size}"
    
    pause 1.0
    
    centered "BedWars. Финальная арена."
    
    show mark collecting at char_center with dissolve
    
    m_inner "Алмазы... Ещё немного и хватит на полную броню."
    
    hide mark collecting
    show mark examining at char_center with dissolve
    
    play sound beep_sound volume 0.8
    
    "Браслет на руке Марка начинает пищать."
    
    m "Что за...?"
    
    centered "⚠️ ВАША КРОВАТЬ АТАКОВАНА"
    
    m "Чёрт! Nikita! Pytin! Ответьте!"
    
    "Из рации доносятся лишь помехи, звуки взрывов и крики..."
    
    m_inner "Нет ответа... Нужно бежать!"
    
    hide mark examining
    show mark running at char_center with dissolve
    
    pause 0.5
    
    # -----------------------------------------
    # ЭПИЗОД 1: НАЧАЛО
    # -----------------------------------------
    
    scene bg green_island_destroyed with fade
    
    show mark shocked at char_center with dissolve
    
    m "Нет... Нет-нет-нет!"
    
    "Кровать разрушена. Вокруг разбросаны блоки и вещи погибших тиммейтов."
    
    m_inner "Они мертвы. Оба. А я теперь один... Один против всех."
    
    hide mark shocked
    show mark idle at char_center with dissolve
    
    "Среди парящего лута Марк замечает маленький кубик жёлтой шерсти."
    
    menu:
        "Подобрать странную шерсть":
            $ karma += 1
            $ has_yellow_wool = True
            m_inner "Жёлтая шерсть? Откуда она тут... Ладно, потом разберусь."
            
        "Не обращать внимания, это мусор":
            m_inner "Некогда собирать всякий хлам. Нужно думать о выживании."
    
    hide mark idle
    show mark examining at char_center with dissolve
    
    "Марк смотрит на таблицу счёта на умных часах."
    
    m_inner "Так... Красные — все мертвы. Остались синие и жёлтые."
    
    hide mark examining
    show mark thinking at char_center with dissolve
    
    m_inner "Синие ближе всех... Но сколько их? Вроде бы двое оставалось..."
    
    hide mark thinking with dissolve
    
    # -----------------------------------------
    # ЭПИЗОД 2: СИНИЕ ОКАЗАЛИСЬ ГОЛУБЫМИ
    # -----------------------------------------
    
    scene bg blue_island with fade
    
    show mark building at char_center with dissolve
    
    "Марк осторожно строится к острову синих."
    
    m_inner "Обсидиановый купол вокруг кровати? Серьёзно? Они что, всю игру фармили изумруды?"
    
    hide mark building
    show mark idle at char_center with dissolve
    
    "Внезапно — удар в спину!"
    
    hide mark idle
    show karpik smug at char_center with vpunch
    
    k "Ты чего тут забыл? Скинуть тебя сейчас или послушать твои мольбы о пощаде, жалкий Марк Штейн?"
    
    menu:
        "Предложить союз против жёлтого":
            $ karma += 1
            jump alliance_path
            
        "Оскорбить в ответ":
            $ karma -= 1
            jump insult_path
            
        "Молча принять судьбу":
            jump silent_path

# -----------------------------------------
# ВЕТКА: Союз
# -----------------------------------------

label alliance_path:

    hide karpik smug
    show mark confident at char_left with dissolve
    show karpik smug at char_right with dissolve

    m "Погоди! Жёлтый остался один, но у него уже 3 убийства! Он слишком опасен. Поодиночке он нас уничтожит... Но вместе — у нас есть шанс!"

    hide karpik smug
    show karpik aggressive at char_right with dissolve

    k "Хуйня идея! Я его и так смогу одолеть. Прощай, лошара!"

    jump karpik_pushes

# -----------------------------------------
# ВЕТКА: Оскорбление
# -----------------------------------------

label insult_path:

    hide karpik smug
    show mark angry at char_left with dissolve
    show karpik smug at char_right with dissolve

    m "Пошёл на хуй, синий ублюдок! Думаешь, я тебя боюсь?!"

    hide karpik smug
    show karpik aggressive at char_right with dissolve

    k "Сам напросился! Прощай, мудак!"

    jump karpik_pushes

# -----------------------------------------
# ВЕТКА: Молчание
# -----------------------------------------

label silent_path:
    
    hide karpik smug
    show mark scared at char_left with dissolve
    show karpik smug at char_right with dissolve
    
    "Марк молчит."
    
    hide karpik smug
    show karpik aggressive at char_right with dissolve
    
    k "Нечего сказать? Тогда прощай!"
    
    jump karpik_pushes

# -----------------------------------------
# Карпик сбрасывает Марка
# -----------------------------------------

label karpik_pushes:
    
    "Карпик бьёт Марка палкой на отдачу!"
    
    hide mark scared
    hide mark angry
    hide karpik aggressive
    
    show mark falling at char_center with hpunch
    
    pause 0.5
    
    scene bg black with fade
    
    "Тишина..."
    
    pause 1.0
    
    scene bg blue_island with fade
    
    show mark hanging at char_left with dissolve
    
    "Рука Марка в последний момент хватается за выступ!"
    
    show karpik smug at char_right with dissolve
    
    "Карпик смотрит вниз на висящего Марка, затем оглядывается на центральный остров..."
    
    hide karpik smug
    show karpik friendly at char_right with dissolve
    
    k "Ёб твою мать... Жёлтый в полной алмазке с чарками. Ладно, вылезай."
    
    "Карпик вытягивает Марка обратно на остров."
    
    jump after_karpik_deal

# -----------------------------------------
# После сделки с Карпиком
# -----------------------------------------

label after_karpik_deal:
    
    hide mark confident
    hide mark scared
    show mark relieved at char_left with dissolve
    show karpik friendly at char_right with dissolve
    
    k "Извини, чувак, погорячился. Нам точно нужно стать союзниками."
    
    hide mark relieved
    show mark suspicious at char_left with dissolve
    
    m "Ага, блять, сейчас снова меня сбросишь?"
    
    k "Слушай план. Ты вернёшься на свой остров, заберёшь ресурсы. Принесёшь сюда. Прокачаем броню, мечи, возьмём голды и уничтожим жёлтого."
    
    k "И кстати — у нас один шанс. Моя кровать тоже уничтожена. Жёлтый использовал динамит, перепрыгнул к нам и снёс её, пока мы даже шерстью не достроили..."
    
    hide mark suspicious
    show mark idle at char_left with dissolve
    
    m "А нахрена тут столько обсидиана? Вы могли потратить его на броню!"
    
    hide karpik friendly
    show karpik smug at char_right with dissolve
    
    k "Твои глупые тиммейты и красные клюнули на такую застройку. Приходили ломать обсидиан — а мы им ломали кровати, ха!"
    
    m "Ладно... Выдвигаемся."
    
    hide mark idle
    hide karpik smug
    
    # Марк идёт за ресурсами
    
    scene bg green_island_destroyed with fade
    
    show mark looting at char_center with dissolve
    
    "Марк собирает оставшиеся ресурсы на своей разрушенной базе."
    
    hide mark looting with dissolve
    
    # Возвращение
    
    scene bg blue_island with fade
    
    show karpik smug at char_center with dissolve
    
    "Марк возвращается — Карпик уже в улучшенной броне."
    
    k "Оставь ресурсы. Сгоняй за алмазами для себя — я чёт забыл и прокачал всё своё, а твоё забыл, хех."
    
    hide karpik smug
    show mark suspicious at char_left with dissolve
    show karpik smug at char_right with dissolve
    
    m "А ты точно не спиздишь ресурсы и не пойдёшь в центр?"
    
    hide karpik smug
    show karpik friendly at char_right with dissolve
    
    k "Точно."
    
    hide mark suspicious
    show mark idle at char_left with dissolve
    
    m "Ну тогда окей..."
    
    hide mark idle
    hide karpik friendly
    
    # Сбор алмазов
    
    scene bg diamond_island with fade
    
    show mark collecting at char_center with dissolve
    
    "Марк собирает алмазы."
    
    hide mark collecting with dissolve
    
    # Возвращение — видит предательство
    
    scene bg blue_island with fade
    
    show mark facepalm at char_center with dissolve
    
    m_inner "Этот идиот строится к центру. Я так и знал."
    
    hide mark facepalm
    show karpik hanging at char_center with vpunch
    
    "Карпик поскальзывается и повисает на шерсти!"
    
    k "БЛЯЯЯТЬ! Я ПОДСКОЛЬЗНУЛСЯ!"
    
    menu:
        "Бежать на помощь":
            $ karma += 1
            hide karpik hanging
            show mark running at char_center with dissolve
            m "Держись!"
            hide mark running
            
        "Остаться на месте":
            hide karpik hanging
            show mark idle at char_center with dissolve
            m_inner "После того как он меня сбросил? Сам виноват."
            hide mark idle
    
    # В любом случае — фаербол
    
    play sound explosion_sound volume 1
    
    scene bg center_island with flash
    
    "Фаербол прилетает из центра!"
    
    "ВЗРЫВ!"
    
    show karpik falling at char_center with hpunch
    
    k "ДА БЛЯТЬ, Я ПОДСКОЛЬЗНУЛСЯ!!!"
    
    hide karpik falling
    
    scene bg blue_island with fade
    
    show mark shocked at char_center with dissolve
    
    m "...Чёрт."
    
    hide mark shocked with dissolve
    
    # -----------------------------------------
    # ЭПИЗОД 3: ЗЕЛЁНЫЙ ПРОТИВ ЖЁЛТОГО
    # -----------------------------------------
    
    scene bg red_island with fade
    
    show mark looting at char_center with dissolve
    
    "Марк обыскивает базу красных."
    
    m_inner "Изумруды? Жёлтый их тут оставил... Идиот. Или это ловушка?"
    
    hide mark looting
    show mark determined at char_center with dissolve
    
    "Марк экипируется."
    
    m_inner "Алмазная броня. Алмазный меч. Пара голдов. Стак блоков. Я готов."
    
    m_inner "Эта битва станет последней. Для одного из нас."
    
    hide mark determined with dissolve
    
    # Путь к центру
    
    play music battle_music fadeout 1.0 fadein 1.0 volume 0.8
    
    scene bg center_island with fade
    
    show mark building at char_center with dissolve
    
    "Марк строится к центру."
    
    hide mark building
    show mark idle at char_center with dissolve
    
    m_inner "Тихо... Слишком тихо. Где он?"
    
    "Свист сверху!"
    
    hide mark idle
    show mark scared at char_center with vpunch
    
    play sound explosion_sound volume 1
    
    "Динамит падает рядом — ВЗРЫВ!"
    
    hide mark scared
    show mark placing_water at char_center with dissolve
    
    m "Вода! Нужна вода!"
    
    "Марк разливает воду, гасящую взрывную волну."
    
    hide mark placing_water
    show mark building at char_center with dissolve
    
    "Марк строит вверх, к источнику динамита."
    
    hide mark building with dissolve
    
    # Подъём
    
    scene bg sky_battle with fade
    
    show mark climbing at char_center with dissolve
    
    "Марк поднимается выше..."
    
    hide mark climbing
    show mayakovsky menacing at char_center with dissolve
    
    "Марк видит имя на нагруднике противника."
    
    centered "{size=+5}МАЯКОВСКИЙ{/size}"
    
    hide mayakovsky menacing
    show mark angry at char_left with dissolve
    show mayakovsky menacing at char_right with dissolve
    
    m "МАЯКОВСКИЙ! А ВЫ ЧЕГО ВСЁ ПРЯЧЕТЕСЬ ОТ МЕНЯ?!"
    
    hide mayakovsky menacing
    show mayakovsky battle at char_right with dissolve
    
    "Маяковский использует эндер-перл и телепортируется к Марку!"
    
    play sound sword_sound volume 0.8
    
    "Серия ударов!"
    
    hide mark angry
    hide mayakovsky battle
    
    show mark falling at char_center with hpunch
    
    "Марк падает, но приземляется на воду внизу!"
    
    hide mark falling
    
    scene bg center_battle with fade
    
    show mark eating_apple at char_center with dissolve
    
    "Марк ест золотое яблоко."
    
    hide mark eating_apple
    show mark determined at char_center with dissolve
    
    "Марк жестом зовёт Маяковского вниз."
    
    hide mark determined
    show mayakovsky battle at char_center with dissolve
    
    "Маяковский спрыгивает."
    
    hide mayakovsky battle with dissolve
    
    # БОЙ
    
    centered "{size=+10}БИТВА{/size}"
    
    show mark fighting at char_left with dissolve
    show mayakovsky battle at char_right with dissolve
    
    play sound sword_sound volume 0.8
    
    "Обмен ударами. Броня трещит."
    
    play sound sword_sound volume 0.8
    
    hide mark fighting
    show mark defending at char_left with dissolve
    
    "Маяковский парирует удар Марка и контратакует!"
    
    hide mark defending
    hide mayakovsky battle
    
    show mark defeated at char_left with dissolve
    show mayakovsky menacing at char_right with dissolve
    
    "Марк на земле. Меч отлетел в сторону."
    
    "Маяковский заносит клинок..."
    
    menu:
        "Кричать о ловушке создателей":
            $ karma += 2
            jump speech_path
            
        "Просить пощады":
            $ karma -= 2
            jump bad_ending
            
        "Молча принять смерть":
            $ karma -= 2
            jump bad_ending

# -----------------------------------------
# ВЕТКА: Речь о ловушке
# -----------------------------------------

label speech_path:
    
    stop music fadeout 2.0
    
    hide mark defeated
    show mark pleading at char_left with dissolve
    
    m "СТОЙ! Они этого только и ждут!"
    
    hide mayakovsky menacing
    show mayakovsky listening at char_right with dissolve
    
    may "...Что?"
    
    m "Они ждут, чтобы мы убили друг друга! Чтобы началась новая игра! А затем снова — убийства, уничтоженные кровати, и всё по кругу!"
    
    m "Вспомни! Мы всех убили, чтобы попасть на эту арену — это ФИНАЛ! Нас душили газом, отправляли на новую арену, и так пока мы не очутились здесь!"
    
    m "Это всё нереально! Мы тут застряли — нужно ВЫБИРАТЬСЯ!"
    
    may "И что ты думаешь — если я тебя убью, они меня не выпустят?"
    
    hide mark pleading
    show mark confident at char_left with dissolve
    
    m "Конечно нет! Ты станешь призом для следующего финала. И так — вечно."
    
    "Пауза."
    
    hide mayakovsky listening
    show mayakovsky neutral at char_right with dissolve
    
    "Маяковский опускает меч."
    
    may "...Похоже, ты прав."
    
    may "Но учти — я убью тебя при первой возможности, если бросишь хоть один косой взгляд."
    
    hide mark confident
    show mark relieved at char_left with dissolve
    
    m "Договорились. Идём вверх."
    
    hide mark relieved
    hide mayakovsky neutral
    
    # -----------------------------------------
    # ЭПИЗОД 4: ПОБЕГ
    # -----------------------------------------
    
    play music escape_music fadein 1.0 volume 0.8
    
    scene bg sky_battle with fade
    
    show mark climbing at char_left with dissolve
    show mayakovsky neutral at char_right with dissolve
    
    "Марк и Маяковский строят башню вверх."
    
    "50 блоков... 70... 90..."
    
    hide mark climbing
    show mark scared at char_left with dissolve
    
    "Небо краснеет."
    
    m "Что за...?"
    
    "Из облаков начинают лететь стрелы и фаерболы!"
    
    hide mayakovsky neutral
    show mayakovsky battle at char_right with dissolve
    
    may "Создатели! Они пытаются нас остановить!"
    
    hide mark scared
    show mark determined at char_left with dissolve
    
    m "Продолжаем! Мы почти у потолка!"
    
    hide mark determined
    hide mayakovsky battle
    
    # Потолок
    
    scene bg sky_ceiling with fade
    
    show mark fighting at char_center with dissolve
    
    "Марк ломает верхний блок неба!"
    
    hide mark fighting
    
    scene bg sky_broken with flash
    
    "За ним — не пустота. Там... земля. Лес. Настоящий мир."
    
    show mark reaching_down at char_center with dissolve
    
    "Марк забирается, ложится на живот, тянет руку Маяковскому."
    
    m "Давай руку!"
    
    hide mark reaching_down
    show mayakovsky neutral at char_center with dissolve
    
    "Маяковский смотрит вверх на Марка."
    
    "Затем оглядывается назад, на горящую арену..."
    
    hide mayakovsky neutral with dissolve
    
    stop music fadeout 2.0
    
    # Проверка концовки
    
    if karma >= 4 and has_yellow_wool:
        jump good_ending
    elif karma >= 2:
        jump neutral_ending
    else:
        jump bad_ending

# -----------------------------------------
# ХОРОШАЯ КОНЦОВКА
# -----------------------------------------

label good_ending:
    
    show mayakovsky neutral at char_center with dissolve
    
    "Маяковский берёт руку Марка."
    
    hide mayakovsky neutral
    
    scene bg black with flash
    
    "Яркая вспышка!"
    
    pause 1.0
    
    play music peaceful_music fadein 2.0 volume 0.8
    
    scene bg bedroom with fade
    
    show mark waking at char_center with dissolve
    
    "Марк резко просыпается в своей кровати."
    
    m "Что... Где я?"
    
    "Утренний свет. Комната. Компьютер с Minecraft на экране."
    
    m_inner "Сон... Это был просто сон."
    
    "Марк замечает книгу на тумбочке."
    
    hide mark waking with dissolve
    
    # ========================================
    # СПЕЦИАЛЬНАЯ СЦЕНА С ЗУМОМ
    # Здесь включается final_cg.mp3
    # Картинка зумится с 100% до 115% за 15 секунд
    # ========================================
    
    stop music fadeout 1.0
    pause 0.5
    play music final_cg_music fadein 1.0 volume 0.8
    
    # Показываем CG с медленным зумом (15% за 29 секунд)
    scene cg book_ending at center_zoom with dissolve
    
    centered "МАЯКОВСКИЙ. СОБРАНИЕ СТИХОТВОРЕНИЙ"
    
    "Закладка — кусочек жёлтой шерсти."
    
    pause 5.0
    
    m_inner "...Или нет?"
    
    # Ждём пока зум и музыка завершатся (оставшиеся ~20 секунд)
    pause 20.0
    
    scene bg black with fade
    
    stop music fadeout 3.0
    
    pause 1.0
    
    centered "{size=+10}КОНЕЦ{/size}"
    
    pause 1.0
    
    centered "ХОРОШАЯ КОНЦОВКА"
    
    centered "Спасибо за игру!"
    
    return

# -----------------------------------------
# НЕЙТРАЛЬНАЯ КОНЦОВКА
# -----------------------------------------

label neutral_ending:
    
    play music sad_music fadein 2.0 volume 0.8
    
    show mark reaching_down at char_left with dissolve
    
    m "Давай руку!!"
    
    show mayakovsky back at char_right with dissolve
    
    "Маяковский смотрит на Марка."
    
    "Отворачивается."
    
    "И уходит обратно вниз, в красное зарево арены."
    
    hide mayakovsky back
    hide mark reaching_down
    
    show mark shocked at char_center with dissolve
    
    m "МАЯКОВСКИЙ!"
    
    hide mark shocked
    
    scene bg black with fade
    
    pause 1.0
    
    centered "Некоторые клетки выбирают сами себя."
    
    pause 1.0
    
    stop music fadeout 2.0
    
    centered "{size=+10}КОНЕЦ{/size}"
    
    pause 1.0
    
    centered "НЕЙТРАЛЬНАЯ КОНЦОВКА"
    
    return

# -----------------------------------------
# ПЛОХАЯ КОНЦОВКА
# -----------------------------------------

label bad_ending:
    
    play music sad_music fadein 1.0 volume 0.8
    
    scene bg center_battle with fade
    
    show mayakovsky menacing at char_right with dissolve
    
    if karma < 0:
        show mark scared at char_left with dissolve
        m "Пожалуйста... Не надо..."
    else:
        show mark defeated at char_left with dissolve
        "Марк закрывает глаза."
    
    may "Прощай, Марк Штейн."
    
    hide mark scared
    hide mark defeated
    hide mayakovsky menacing
    
    play sound sword_sound volume 0.8
    
    scene bg black with flash
    
    "..."
    
    pause 1.0
    
    stop music fadeout 2.0
    
    centered "Игра окончена."
    
    pause 1.0
    
    centered "{size=+10}ТЫ ПРОИГРАЛ{/size}"
    
    return
