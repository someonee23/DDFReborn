﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Ван", color='#ffffff')
define m = Character("Марк", color='#ffffff')
define b = Character("Билли", color='#ffffff')
define r = Character("Рикардо", color='#ffffff')
define s1 = Character("Эрик", color='#ffffff')
define s2 = Character("Дункан", color='#ffffff')

# The game starts here.

label start:

    'Данная игра не рекомендуется лицам младше 18 лет. Игра содержит ненормативную лексику, сцены насилия, а также сцены сексуального характера. Если Вам что-то не нравится - выключайте игру.'
    'Все персонажи, события, и места являются вымышленными, и любое совпадение с реально живущими людьми или когда-либо жившими людьми случайно, любое совпадение с реально существующим местом или событием случайно.'
    scene bg van storyteller
    with fade
    v 'Моё имя Ван Каркхолм, я художник. Художник неформальных искусств.'
    v 'Люди нанимают меня для воплощения своих фантазий. Глубоких тёмных фантазий.'
    v 'В детстве я хотел быть киноактером, но так сложилась судьба, что я стал порноактером, а затем Мастером. Мастером подземелья.'
    v 'Сейчас вы услышите мою историю. Вы узнаете, как простой азиат стал Мастером. Мастером подземелья.'
    scene bg van closeup
    with dissolve
    v 'Раньше я жил во Вьетнаме, но мне пришлось переехать в США, так как в то время людей моей ориентации в моей стране не уважали.'
    v 'Поначалу я подрабатывал в разных местах, но вскоре я стал работать в эскорте.'
    v 'За время работы в эскорте стало понятно, что у людей странные желания и запросы. Пожтому я решил, что надо открыть своё подземелье для людей, которые хотят воплотить все свои фантазии.'
    v 'Но было решено отложить это дело, так как работа отнимала всё время.'
    v 'Однажды я решил сходить в качалку.'
    v 'И этот поход заставил меня открыть подземелье...'
    scene bg van gym full
    with dissolve
    v 'Сразу же, как я вошёл в раздевалку ко мне обратился человек.'
    m 'Эй, дружок-пирожок, ты ошибся дверью. Клуб любителей кожи двумя этажами ниже.'
    scene bg van gym fucku
    with dissolve
    v 'Иди нахуй.'
    m 'Нет, нахуй пойдёшь ты, кожаный человек.'
    scene bg vw gym point with dissolve
    pause 1
    scene bg vw gym tell with dissolve
    pause 0.1
    m 'Снимай свою броню, я тебе покажу, кто Босс этой качалки.'
    v 'Да, разберёмся прям в этой качалке.'
    ##fight scene 1
    v 'Началась борьба. Поначалу выигрывал мой противник.'
    ##fight scene 2
    ##fight scene 3
    v 'Но ситуация резко обернулась в мою сторону. И я стал выигрывать.'
    ##fight scene 4
    v 'Я повалил его, он был сломлен, как физически, так и морально.'
    v 'Казалось бы я победил, я стал Боссом этой качалки!'
    v 'Но не тут то было...'
    ##fight scene 5
    v 'Пока я радовался победе, мой противник нанёс ответный удар. Он встал и продолжил борьбу'
    v 'У меня не осталось сил бороться, и он повалил меня.'
    ##fight scene 6
    m 'Я БОСС ЭТОЙ КАЧАЛКИ!!!'
    m 'Ты повержен, кожаный человек, уходи из этой качалки.'
    v 'Этот человек стал моим злейшим врагом. Я поставил себе цель отомстить ему.'
    v 'Для этого надо было узнать, кто он такой и открыть своё подземелье.'
    scene bg van closeup
    with dissolve
    v 'Я вернулся домой, сел за ПК и проверил свою электронную почту.'
    v 'Там было сообщение от моего старого друга - Рикардо...'
    ##computer scene 1
    r 'Здарова, братан,ь слыхал, что ты хочешь открыть своё подземелье. У меня есть несколько человек, готовы быть рабами. Нужны?'
    v 'Привет, конечно нужны, присылай. Жду всех. Как жизнь? Как хуй, стоит?'
    ##computer scene 2
    r 'Да всё отлично, с Билли Керрингтоном тусим.'
    r 'Его друг - Марк Пульф говорит, что он сегодня победил в качалке какого-то петуха.'
    v 'Это был я. Он напал на меня, когда я пришел в качалку. Мы боролись долго, и я почто победил, но у меня не хватило сил.'
    v 'В результате он выиграл и стал Боссом качалки. Но я отомщу ему.'
    r 'Вот как! Удачи тебе, отомсти ему и выеби его в жопу.'
    scene bg van closeup
    with dissolve
    v 'Одно дело сделано - я узнал его имя. Но ещё оставались недоделанные дела, например, открыть подземелье.'
    v 'Я переделал свой дом в подземелье. Получилось очень круто.'
    v 'Прошла неделя, в моё подземелье приехали рабы.'
    ##dungeon scene 1
    v 'Я встретил их, и мы стали творить разные запретные вещи...'
    ##dungeon scene 2
    v 'Дела шли хорошо, рабы были послушные.'
    v 'Мы ебались, было хорошо и мне, и им.'
    ##dungeon scene 3 
    v 'Но однажды двое рабов сбежали. Их звали Жрик Дайклс и Дункан Пилс. Я их быстро нашёл и вернул назад.'
    v 'Я решил допросить их...'
    s1 'Сэр, сейчас мы всё объясним!'
    v 'Почему вы сбежали?'
    s1 'Мы хотели уйти к девушкам.'
    v 'Чёртовы рабы! Зачем? У вас был Мастер, другие рабы и подземелье. Зачем вам девушки?!'
    s2 'Прости нас, Мастер.'
    v 'Нет, Я устрою вам ад, парни.'

menu:  

    'Наказать шокером':
        jump taser

    'Наказать хуём':
        jump huy

    'Простить рабов':
        jump forgive

label taser:
    'In development'
    return

label huy:
    'In development'
    return

label forgive:
    pause 0.2
    v 'Сегодня я добрый, вам повезло, не получите своё наказание. Но, если ещё раз сбежите - получите по полной.'
    Character('Рабы', color='#ffffff') 'Спасибо, мастер!'
    scene bg van closeup
    with dissolve
    v 'Прошло несколько дней и я решил выглянуть в окно...'
    ##billy scene 1
    v 'На улице я увидел Билли Керрингтона, проезжающего на своём мотоцикле рядом с моим подземельем.'
    v 'Далее я решил посмотреть трансляцию Кико-Кико-Дога...'
    ##billy scene 2
    v 'Там показывали речь Билли Керрингтона. Того самого Билли, который только что проезжал рядом с подземельем.'
    v 'Ну что ж, послушаем!'
    ##billy scene 3
    b 'Мои братья, я, Билли Керрингтон, стою здесь, смирившись с поставленной перед нами задачей, помня о жертвах, которые принесли наши предки из Кико-Кико.'
    b 'Я хочу сообщить Вам, что мы находимся в разгаре кризиса. Кико-Кико воюет со штормом беспокойства. Экономика Кико-Кико ослабевает, это следствие безответственности со стороны руководства, а также коллективная неспособность сделать трудный выбор.'
    b 'Сегодня я говорю вам, что этот вызов реальный. Подтверждая величие нашего сайта, мы понимаем, что величие никогда не даётся просто так. Наше путешествие никогда не было коротким. Этот путь никогда не был для слабых людей. Эти люди боролись, чтобы мы с вами могли жить лучше.'
    b 'Мы остаёмся самым мощным сайтом в интернете. У нас изобретательные умы и необходимые услуги.'
    b 'На данный момент есть те, кто сомневаются в наших амбициях. Они предполагают, что наша система не сможет выдержать слишком много фильмов. Их воспоминания слишком коротки, потому что они забыли, что Кико-Кико уже сделал то, что могут достичь свободные люди.'
    b 'Итак, всем людям, которые смотрят это видео. От больших городов до маленьких деревень, знайте, что Кико-кико друг каждого человека, который ищет будущее, любви и мира.'
    b 'Теперь от нас требуется больше ответственности, это цена за гражданство Кико-кико.'
    b 'Давайте вспомним эти вечные слова: В ЖОПУ МЫ МОЖЕМ!'
    b 'Благодарю вас, и благословит вас Бог.'
    ''
    pause 0.7
    v 'Хорошая речь вышла, уважаю Билли.'
    scene bg van closeup
    with dissolve
    v 'Время шло дальше, а мы решили попробовать сакшен...'
    ##suction scene 1
    