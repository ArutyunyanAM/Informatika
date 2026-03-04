infor_objom = 1.44
pages = 100
stroki = 50
simvol = 25
kol_byte_na_simvol = 4
perevod = 1024

objom_v_byte = infor_objom * perevod**2 # Переводим Мб в байты
kol_simvol = objom_v_byte / kol_byte_na_simvol # Находим количество символов во всех книгах
kol_strok = kol_simvol / simvol # Находим количество строк во всех книгах
kol_pages = kol_strok / stroki # Находим количество страниц во всех книгах
kol_knig = int(kol_pages / pages) #Находим количеств книг

print("Количество книг, помещающихся на дискету:", kol_knig) #Выводим количество книг
