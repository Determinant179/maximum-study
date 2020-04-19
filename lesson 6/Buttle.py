import Tanks

tank_1 = Tanks.superTank("Опустошитель", 100, 20, 40, 150, True)
tank_2 = Tanks.Tank("Танос", 150, 30, 50, 270)
tank_3 = Tanks.invisibleTank("Путин", 0, 0, 5, 10, True)

#tank_1.print_info()
#tank_2.print_info()

tank_1.shot(tank_2)

tank_2.shot(tank_1)
tank_2.shot(tank_1)
tank_2.shot(tank_1)
tank_2.shot(tank_1)
tank_2.shot(tank_1)

tank_1.shot(tank_3)


