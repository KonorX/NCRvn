define enemy=Character("",color="#c90000")
#default is_scaredIn1night=True

label NadinNightmare1:

    #scene bg black with Dissolve(.5)
    scene bg firstnightmare light
    with Dissolve(.5)
    "и тут Егор внезапно увидел как на Надю во сне напала какая то тварь"
    e "боже что за дичь вокруг происходит\n я что, little misfortune что ли что вокруг меня какие то твари появляются "
    e "не дай бог ты подойдешь ближе,надеюсь я проснусь и не вспомню этого мерзкого места "
    scene bg firstnightmare dark
    enemy "{i}приближается{\i}"

    mc "кажется у Нади проблемы c Тенью"
    menu:
        "Помочь":
            $ is_scaredIn1night=False
            nvl clear
            myself "Егор попытался отбить Тень,однако она откинула его далеко"
            mcnvl "Блина,как же его отбить"
            myself "И тут Егор вспомнил что у него в телефоне есть фонарик{p=0.05}которым можно попытаться отвлечь Тень"
            with flash
            myself "Егор посветил в Тень и она начала шипеть и исчезать"
            scene bg firstnightmare dying
            nvl clear
            nvl hide
            enemy "Ааааа-аааарх {i} звуки смерти Тени {\i}"

            jump helpedInFirst
        "Не помогать":
            scene bg firstnightmare close 2
            $ is_scaredIn1night=True
            e "{b} прекратись ты гребанный кошмар {\b}"
            jump endOfNightmare

    label helpedInFirst:
        scene bg nightmarewon
        e "Здесь кто то есть? Покажись!"
        mc "кажется из-за этой тени и держался кошмар"
        e "Спасибо {p} Как тебя зовут?"
        menu :
            "говорить":
                $ root1Progress+=1
                mc "Егор"
                e "Спасибо, Егор"
                e "Подожди,а не ты ли сегодня был на стриме?"
                mc "Я {p} когда следующий стрим?"
                e "вообще я планировала послезавтра"
                e "ты как раз хотел помочь с новеллой,если будут идеи подкинешь на стриме?"
                mc "ок,тогда до стрима"
                "кошмар растворяется как и Егор из него"
                jump endOfNightmare
            "не говорить":
                "{i} герой скрывается в исчезающей тени кошмара {\i}"
                jump endOfNightmare
    label endOfNightmare:
        scene bg lightsoff with Dissolve(.5)
        mc "я проснулся и кажется опять случайно воспользовался своей способностью"
        mc "и впрямь надо бы уже ложиться спать"

        jump SecondDay
        #jump globalEnding
