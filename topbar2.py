import arcade
import buttons2 as buttons

def start(player, size):
    win_width, win_height = size
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
        content.append(buttons.Txt(i, win_width - 72, win_height - 48*(j), arcade.color.BLACK, 16))

    content.append(buttons.Img("data/icons/coin.png", win_width - 18, win_height - 32*(1)))
    content.append(buttons.Img("data/icons/investigationpoint.png", win_width - 18, win_height - 48*(2)))
    content.append(buttons.Img("data/icons/stone.png", win_width - 18, win_height - 32*(3)))
    content.append(buttons.Img("data/icons/wood.png", win_width - 18, win_height - 32*(4)))
    content.append(buttons.Img("data/icons/wool.png", win_width - 18, win_height - 32*(5)))
    content.append(buttons.Img("data/icons/wheat.png", win_width - 18, win_height - 32*(6)))
    content.append(buttons.Img("data/icons/flour.png", win_width - 18, win_height - 32*(7)))
    content.append(buttons.Img("data/icons/iron.png", win_width - 18, win_height - 32*(8)))
    content.append(buttons.Img("data/icons/iron.png", win_width - 18, win_height - 32*(9))) # gold eig
    content.append(buttons.Img("data/icons/iron.png", win_width - 18, win_height - 32*(10))) # sword
    content.append(buttons.Img("data/icons/wood.png", win_width - 18, win_height - 32*(11))) # bow
    return content 