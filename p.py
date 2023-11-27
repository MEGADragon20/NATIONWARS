def wheat_plot(wheat_plot):
    lvl = str(wheat_plot.lvl)
    name = "wheat_plot"
    villagename = wheat_plot.village.name
    color = wheat_plot.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_wheat_plot", 7))

    return content