import arcade
import buttons

def start(player):
    num_coins = str(player.coins)
    num_inpo = str(player.investigationpoints)
    num_stone = str(player.goods["stone"])
    num_wood = str(player.goods["wood"])
    num_coal = str(player.goods["wool"])
    num_wheat = str(player.goods["wheat"])
    num_flour = str(player.goods["flour"])
    num_iron = str(player.goods["iron"])
    num_gold = str(player.goods["gold"])
    num_swords = str(player.goods["swords"])
    num_bows = str(player.goods["bows"])
    lis = [num_coins, num_inpo, num_stone, num_wood, num_coal, num_wheat, num_flour, num_iron, num_gold, num_swords, num_bows]
    empty = []
    for i in lis:
        if len(i) == 1:
            i = "00" + i
        elif len(i) == 2:
            i = "0" + i
        empty.append(i)
    lis = empty
    content = []
    x_positions = [10, 90, 170, 250, 330, 410, 490, 570, 650, 730, 810]

    for i,j in zip(lis, range(len(lis))):
        content.append(buttons.Txt(i, 10+80*(j), 800, arcade.color.BLACK, 16))

    content.append(buttons.Img("data/icons/coin.png", 65, 808))
    content.append(buttons.Img("data/icons/investigationpoint.png", 145, 808))
    content.append(buttons.Img("data/icons/stone.png", 225, 808))
    content.append(buttons.Img("data/icons/wood.png", 305, 808))
    content.append(buttons.Img("data/icons/wool.png", 385, 808))
    content.append(buttons.Img("data/icons/wheat.png", 465, 808))
    content.append(buttons.Img("data/icons/flour.png", 545, 808))
    content.append(buttons.Img("data/icons/iron.png", 625, 808))
    content.append(buttons.Img("data/icons/iron.png", 705, 808)) # gold eig
    content.append(buttons.Img("data/icons/iron.png", 785, 808)) # sword
    content.append(buttons.Img("data/icons/wood.png", 865, 808)) # bow
    return content 