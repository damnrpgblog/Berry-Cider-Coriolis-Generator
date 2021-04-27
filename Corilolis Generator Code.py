import random
   
WT = ["Пистолет", "Карабин", "Винтовка", "Дробовик", "Карманный пистолет"]
Type = (random.choice(WT))
if Type == ('Пистолет'): 
        Mod = ['+0', '+1', '+2', '+3']
        Int = ['0', '+1', '+2', '+3']
        DMG = ['1', '2', '3']
        P = ['-', '1', '2', '3', '4']
        Dist = ['Средняя', 'Дальняя']
        Othr = ['Легкое', 'Надежное', 'Автоматическое', 'Бесшумное', 'Шоковое', '-', 'Бронебойное']
        Lvl = ['Современное', 'Передовое']
        Cost = random.randint(300, 3000)

        print ('Тип:', Type)
        print ('Модификатор:', random.choice(Mod))
        print ('Инициатива:', random.choice(Int))
        print ('Урон:', random.choice(DMG))
        print ('Порог:', random.choice(P))
        print ('Дальность:', random.choice(Dist))
        print ('Свойства:', random.choice(Othr))
        print ('Уровень:', random.choice(Lvl))
        print ('Цена:', Cost)
        
if Type == ('Карабин'):
        Mod = ['+0', '+1', '+2', '+3']
        Int = ['-3', '-2', '-1', '0', '+1', '+2', '+3']
        DMG = ['1', '2', '3', '4', '5']
        P = ['-', '1', '2', '3', '4']
        Dist = ['Средняя', 'Дальняя']
        Othr = ['Легкое', 'Надежное', 'Автоматическое', 'Бесшумное', 'Шоковое', '-', 'Бронебойное']
        Lvl = ['Современное', 'Передовое']
        Cost = random.randint(700, 10000)

        print ('Тип:', Type)
        print ('Модификатор:', random.choice(Mod))
        print ('Инициатива:', random.choice(Int))
        print ('Урон:', random.choice(DMG))
        print ('Порог:', random.choice(P))
        print ('Дальность:', random.choice(Dist))
        print ('Свойства:', random.choice(Othr))
        print ('Уровень:', random.choice(Lvl))
        print ('Цена:', Cost)
    
if Type == ('Витновка'):
        Mod = ['+0', '+1', '+2', '+3']
        Int = ['-3', '-2', '-1', '0', '+1', '+2', '+3']
        DMG = ['3', '4', '5', '6']
        P = ['-', '1', '2', '3', '4']
        Dist = ['Средняя', 'Дальняя']
        Othr = ['Легкое', 'Надежное', 'Автоматическое', 'Бесшумное', 'Шоковое', '-', 'Бронебойное']
        Lvl = ['Современное', 'Передовое']
        Cost = random.randint(1000, 10000)

        print ('Тип:', Type)
        print ('Модификатор:', random.choice(Mod))
        print ('Инициатива:', random.choice(Int))
        print ('Урон:', random.choice(DMG))
        print ('Порог:', random.choice(P))
        print ('Дальность:', random.choice(Dist))
        print ('Свойства:', random.choice(Othr))
        print ('Уровень:', random.choice(Lvl))
        print ('Цена:', Cost)

if Type == ('Дробовик'):
        Mod = ['+0', '+1', '+2', '+3']
        Int = ['-3', '-2', '-1', '0', '+1', '+2']
        DMG = ['3', '4', '5', '6']
        P = ['-', '1', '2', '3', '4']
        Dist = ['Ближняя', 'Средняя']
        Othr = ['Легкое', 'Надежное', 'Автоматическое', 'Бесшумное', 'Шоковое', '-', 'Бронебойное']
        Lvl = ['Современное', 'Передовое']
        Cost = random.randint(1000, 10000)

        print ('Тип:', Type)
        print ('Модификатор:', random.choice(Mod))
        print ('Инициатива:', random.choice(Int))
        print ('Урон:', random.choice(DMG))
        print ('Порог:', random.choice(P))
        print ('Дальность:', random.choice(Dist))
        print ('Свойства:', random.choice(Othr))
        print ('Уровень:', random.choice(Lvl))
        print ('Цена:', Cost)

if Type == ('Карманный пистолет'):
        Mod = ['+0', '+1', '+2', '+3']
        Int = ['+2']
        DMG = ['1', '2', '3', '4']
        P = ['-', '1', '2']
        Dist = ['Ближняя', 'Средняя']
        Othr = ['Легкое', 'Надежное', 'Автоматическое', 'Бесшумное', 'Шоковое', '-', 'Бронебойное']
        Lvl = ['Современное', 'Передовое']
        Cost = random.randint(1000, 10000)

        print ('Тип:', Type)
        print ('Модификатор:', random.choice(Mod))
        print ('Инициатива:', random.choice(Int))
        print ('Урон:', random.choice(DMG))
        print ('Порог:', random.choice(P))
        print ('Дальность:', random.choice(Dist))
        print ('Свойства:', random.choice(Othr))
        print ('Уровень:', random.choice(Lvl))
        print ('Цена:', Cost)


