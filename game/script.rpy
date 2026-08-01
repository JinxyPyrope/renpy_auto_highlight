image i_zeil smile = At("zeil smile", sprite_highlight('zeil'))
image i_anna neutral = At("anna neutral", sprite_highlight('anna'))

define character_zeil = Character("Zeil", image='i_zeil', callback=name_callback, cb_name = 'zeil')
define character_anna = Character("Anna", image='i_anna', callback=name_callback, cb_name = 'anna')


label start:
    scene bg classroom
    show i_zeil smile at right
    show i_anna neutral at left

    character_zeil "Zeil is speaking!"
    character_anna "Anna is speaking!"

    return
