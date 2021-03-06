# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Надежда', color="#FF00FF")
define mc = Character("Егор", color="#98FB98")
define myself=Character("",color="#98FB98",kind=nvl)
define mcnvl=Character("Егор", color="#98FB98",kind=nvl)

define root1Progress=0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

image stream  ="n1.png"

# Игра начинается здесь:
label start:
    play music "audio/rain.mp3" fadeout 1
    #queue music "audio/rain.mp3"
    #queue music "audio/rain.mp3"
    scene bg black
    $ flash = Fade(.25, 0, .75, color="#fff")
    scene bg lightsoff
    with Dissolve(1.5)

    mc "........"
    pause .5
    scene bg lightsoff lightning
    with hpunch
    play sound "audio/thunder.mp3"
    mc "!"
    mc "М, ой а я заснул оказывается"
    mc "Хорошо что меня хоть молния разбудила"

    scene bg lightsoff
    with Dissolve(1.0)

    pause .5

    mc "Это была тяжёлая и трудная неделя для меня, меня так всё достало что и сил не осталось вовсе."

    scene bg lightson
    with Dissolve(.5)

    pause .5

    mc "Я решил отдохнуть и поиграть дотку, но самому играть было скучно, а мои друзья в доту не играли."
    image bg transitions:
        "bg lightson"
        "bg lightson lightning"with dissolve
        pause 2.5
        "bg lightson"with dissolve
        pause 1.0
        repeat 2
    play sound "audio/thunder.mp3"
    mc " Я зашел на твич в поиске компаньонов для игры, Spray228 его смотрело больше 10к зрителей - нет подумал я. Дальше был BEMBI - тоже нет. "


    #show bg lightson:
    #crop(0,0,1920,2080)
    #zoom(1920,1080)

    #crop(329,1138,1031,679)

    scene bg mwitch none
    with Dissolve(.5)
    pause .5

    mc " Я продолжил поиск, я листал и листал страницу мвича пока не наткнулся на странный и довольно-таки интересный никнейм NadinKorobka, я не смог пройти мимо."

    scene stream
    #with Dissolve(.5)

    mc "Я зашел на страницу и сказал \"Привет\" NadinKorobka."

    mc " Мне ответили."

    "Вскоре я услышал шелест страниц и увидел на странице как NadinKorobka сидит на столе на котором разбросаны листки и переписывает их в старый ноутбук NSI"

    mc "Что ты делаешь?"

    e " Я пишу визуальную новеллу ответила она."

    mc "Давай вместе напишем?"

    e "Нет, это сложно: не для моего уровня"

    mc "Как тебя зовут?"

    e "Надя"

    mc "А почему ты решила написать новеллу? "

    e " А что делать? {p} Просто скучно и я захотела попробовать себя в новелле."

    mc " И что ты написала?"

    #confused moment

    e "Новеллу"

    mc " Нет, я имею в виду про что она"

    e "Про конец света"

    mc "Ничего себе!{p=1.0} Так это про конец света что ли? {p=0.3} А когда он наступит?"

    e "Через ... {p=0.5} триста лет"

    mcnvl "Я вдруг вспомнил свою подругу, которой приснился сон про апокалипсис"
    mcnvl "Oна постоянно повторяет, что это такое было, а потом не помнит, о чем было и с ужасом думает, что ей теперь делать?"

    nvl clear
    nvl hide dissolve

    mc " Хммм... Какая странная тематика для новеллы, Надь"

    "Уже было поздно, на часах было около 20:21 вечера. {w} Надя начала зевать"

    e "Уже поздно, так что я пойду спать"



    "{i}стрим завершился{/i}"


    scene bg lightson
    with pixellate
    #with Dissolve(.5)
    play sound "audio/thunder.mp3"
    scene bg lightson lightning
    with hpunch
    pause 0.5

    scene bg lightsoff
    with Dissolve(.5)

    scene bg black
    stop music fadeout 1
    mcnvl "Я выключил компьютер.{w} Пока на улице был хоть какой-то свет, я пялился в потолок."
    mcnvl "Я не хотел спать потому что знал что за этим последует."

    scene bg lightsoff lightning

    mcnvl " Я сам не знаю, как и почему я это умею,{w} короче говоря: я умел проникать в чужие сны"
    mcnvl " Я мог просто наблюдать за ним, а еще мог менять сон на своё усмотрения."

    scene bg lightsoff with Dissolve(.5)

    mcnvl " Я часто прикалывался так над друзьями, насылая Лавкрафтаские ужасы к ним в сны. {p}А потом когда они мне рассказывали о своих ужасах я тихонько про себя смеялся."
    mcnvl " Это было забавно.{w} Я не часто так делал, но делал. "

    scene bg black with Dissolve(.5)

    mcnvl "Дальше я не заметил сам, но я заснул. "
    mcnvl "Я понял что я сплю потому что я очутился во сне Нади."

    mcnvl " Она меня не видела, потому что чтобы меня увидеть я сам должен показаться."

    mcnvl " Я буквально хожу невидимый"

    jump NadinNightmare1
    #jump globalEnding

    label globalEnding:
        return
