def Lisamine(i: list, p: list, k: int):
    """Добавление данных в списки.
    Возвращает списки.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    :parameter int k: Количество людей
    :rtype: list, list
    """
    for X in range(k):
        while True:
            nimi = input("Введите имя человека: ").strip()
            if nimi:  
                break
            else:
                print("Пожалуйста, введите действительное имя.")

        while True:
            try:
                palk = int(input("Какая у него зарплата? "))
                break
            except ValueError:
                print("Пожалуйста, введите только цифры.")

        i.append(nimi)
        p.append(palk)
    return i, p

def Eemaldamine(i: list, p: list):
    """Удаление данных из списков.
    Возвращает списки.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    :rtype: list, list
    """
    while True:
        nimi = input("Имя: ")
        n = i.count(nimi)
        if n > 0:
            for x in i:
                if x == nimi:
                    ind = i.index(x)
                    i.remove(x)
                    p.pop(ind)
            break  
        else:
            print(nimi, "не в списке")
    return i, p

def SuurimPalk(i: list, p: list):
    """Находит максимальную зарплату и тех, кто ее получает.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    :rtype: int, list
    """
    if not p:
        print("Список зарплат пуст.")
        return None, []
    
    nimi_list = []
    max_palk = max(p)  
    a = 0
    for palk in p:
        if palk == max_palk:
            ind = p.index(max_palk, a)
            nimi = i[ind]
            a += 1
            nimi_list.append(nimi)
    return max_palk, nimi_list

def VaiksemPalk(i: list, p: list):
    """Находит минимальную зарплату и тех, кто ее получает.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    :rtype: int, list
    """
    if not p:
        print("Список зарплат пуст.")
        return None, []
    
    nimi_list = []
    min_palk = min(p)  
    a = 0
    for palk in p:
        if palk == min_palk:
            ind = p.index(min_palk, a)
            nimi = i[ind]
            a += 1
            nimi_list.append(nimi)
    return min_palk, nimi_list

def Sort(i: list, p: list, a: int):
    N = len(i)

    if a == 1:
        for n in range(N):
            for m in range(n + 1, N):
                if p[n] < p[m]:
                    p[n], p[m] = p[m], p[n]
                    i[n], i[m] = i[m], i[n]
    else:
        for n in range(N):
            for m in range(n + 1, N):
                if p[n] > p[m]:
                    p[n], p[m] = p[m], p[n]
                    i[n], i[m] = i[m], i[n]

    return i, p

def SarnasedPalgad(i: list, p: list):
    """Находит людей с одинаковой зарплатой.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    """
    unikaalsed_palgad = set(p)
    
    for palgapunkt in unikaalsed_palgad:
        indeksid = [index for index, palk in enumerate(p) if palk == palgapunkt]

        if len(indeksid) > 1:
            print(f"Следующие люди получают зарплату {palgapunkt}:")
            for indeks in indeksid:
                print(f"Имя: {i[indeks]}, Зарплата: {p[indeks]}")
            print("----------")

def OtsiPalgaJargi(i: list, p: list, nimi: str):
    """Находит зарплату по указанному имени.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    :parameter str nimi: Имя для поиска зарплаты
    :rtype: list
    """
    leitud_palgad = []

    for indeks, inimese_nimi in enumerate(i):
        if inimese_nimi == nimi:
            leitud_palgad.append(p[indeks])

    return leitud_palgad

def PalkYleSumma(i: list, p: list, summa: int, yle: bool = True):
    """Выводит людей, зарабатывающих больше/меньше указанной суммы.

    :parameter list i: Список имен
    :parameter list p: Список зарплат
    :parameter int summa: Указанная сумма
    :parameter bool yle: Ищет людей, зарабатывающих больше (True) или меньше (False) указанной суммы
    :rtype: list
    """
    sobivad_inimesed = []

    for indeks, palk in enumerate(p):
        if (yle and palk > summa) or (not yle and palk < summa):
            sobivad_inimesed.append((i[indeks], palk))

    return sobivad_inimesed

def Top(inimesed, palgad):
    if len(palgad) < 3:
        print("В списке должно быть как минимум 3 человека.")
        return None

    sorted_indices = sorted(range(len(palgad)), key=lambda k: palgad[k])

    madalad_nimed = [inimesed[i] for i in sorted_indices[:3]]
    madalad_palgad = [palgad[i] for i in sorted_indices[:3]]

    korged_nimed = [inimesed[i] for i in sorted_indices[-3:]]
    korged_palgad = [palgad[i] for i in sorted_indices[-3:]]

    return (madalad_nimed, madalad_palgad), (korged_nimed, korged_palgad)

def Keskmine(i: list, p: list):
    """
    Возвращает среднюю зарплату и имя человека, получающего ее.

    :param list i: Список имен
    :param list p: Список зарплат
    :return: Кортеж (средняя зарплата, имя человека)
    :rtype: tuple
    """
    if not i or not p:
        return None  

    keskmine_palk = sum(p) / len(p)
    lahim_nimi = i[p.index(min(p))]  
    return keskmine_palk, lahim_nimi

def Tulumaks(palk: float, lapsed: int) -> float:
    """
    Вычисляет зарплату, которую человек получит на руки после вычета подоходного налога.

    :param float palk: Ежемесячная зарплата
    :param int lapsed: Количество детей
    :return: Зарплата после вычета подоходного налога
    :rtype: float
    """
    aastapalk = palk * 12  

    if aastapalk <= 14400:
        mitteobl_nal = 7848
    elif palk > 1200:
        mitteobl_nal = max(0, 654 - (654 / 900) * (palk - 1200))
    else:
        mitteobl_nal = 0

    mitteobl_nal += 3270 * lapsed

    tulumaksusem = max(0, aastapalk - mitteobl_nal)
    tulumaks = 0.2 * tulumaksusem

    return palk - (tulumaks / 12)

palk = float(input("Введите ежемесячную зарплату: "))
lapsed = int(input("Введите количество детей: "))
netopalk = Tulumaks(palk, lapsed)
print(f"Зарплата после вычета подоходного налога: {netopalk:.2f} EUR")

def SortByName(i: list, p: list, ascending: bool = True):
    """
    Сортирует данные по имени.

    :param list i: Список имен
    :param list p: Список зарплат
    :param bool ascending: Если True, сортировка по возрастанию, если False, по убыванию
    :return: Отсортированные списки имен и зарплат
    :rtype: tuple
    """
    N = len(i)

    sorted_indices = sorted(range(N), key=lambda k: i[k], reverse=not ascending)

    sorted_i = [i[idx] for idx in sorted_indices]
    sorted_p = [p[idx] for idx in sorted_indices]

    return sorted_i, sorted_p

def PalkAllaKeskmine(i: list, p: list):
    """
    Удаляет людей, у которых зарплата ниже средней.

    :param list i: Список имен
    :param list p: Список зарплат
    :return: Списки имен и зарплат после удаления
    :rtype: tuple
    """
    if not p:
        print("Список зарплат пуст.")
        return i, p

    keskmine_palk = sum(p) / len(p)
    alla_keskmine = [(i[idx], p[idx]) for idx in range(len(p)) if p[idx] < keskmine_palk]

    for nimi, palk in alla_keskmine:
        print(f"{nimi} зарабатывает меньше средней ({keskmine_palk} EUR): {palk} EUR")

    i = [name for name, salary in zip(i, p) if salary >= keskmine_palk]
    p = [salary for salary in p if salary >= keskmine_palk]

    return i, p

def Formaatimine(i: list, p: list):
    """
    Форматирует списки: имена с заглавной буквы, зарплаты в формате int.

    :param list i: Список имен
    :param list p: Список зарплат
    :return: Отформатированные списки
    :rtype: tuple
    """
    formatted_i = [name.capitalize() for name in i]
    formatted_p = [int(salary) for salary in p]

    return formatted_i, formatted_p

def ToopaevapalgaMuutus(i: list, p: list, aastad: int):
    """
    Увеличивает зарплату каждого работника на 5% каждый год.

    :param list i: Список имен
    :param list p: Список зарплат
    :param int aastad: Количество лет
    :return: Списки имен и зарплат после изменений
    :rtype: tuple
    """
    if not p:
        print("Список зарплат пуст.")
        return i, p

    for aasta in range(1, aastad + 1):
        p = [round(salary * 1.05, 2) for salary in p]
        print(f"Зарплата после {aasta} года повышения:")
        for nimi, palk in zip(i, p):
            print(f"{nimi}: {palk} EUR")

    return i, p

def RenameEveryThird(i: list):
    """
    Переименовывает каждого третьего человека. Новые имена вводит пользователь.

    :param list i: Список имен
    :return: Список имен после изменений
    :rtype: list
    """
    new_names = input("Введите новые имена (разделенные запятой): ").split(',')
    for idx in range(2, len(i), 3):
        i[idx] = new_names.pop(0).strip()

    return i

def EditData(i: list, p: list):
    """
    Редактирует данные - имя или зарплату. Измененные данные сохраняются в списке.

    :param list i: Список имен
    :param list p: Список зарплат
    :return: Списки имен и зарплат после изменений
    :rtype: tuple
    """
    print("Редактирование:")
    print("1 - Имя")
    print("2 - Зарплата")
    valik = int(input("Выбор: "))

    if valik == 1:
        vana_nimi = input("Введите старое имя: ").capitalize()
        uus_nimi = input("Введите новое имя: ").capitalize()
        if vana_nimi in i:
            idx = i.index(vana_nimi)
            i[idx] = uus_nimi
            print("Имя успешно изменено.")
        else:
            print("Такого имени не найдено.")

    elif valik == 2:
        nimi = input("Введите имя сотрудника: ").capitalize()
        if nimi in i:
            idx = i.index(nimi)
            try:
                uus_palk = int(input("Введите новую зарплату: "))
                p[idx] = uus_palk
                print("Зарплата успешно изменена.")
            except ValueError:
                print("Пожалуйста, введите только числа.")
        else:
            print("Такого имени не найдено.")

    return i, p

def LeidkeInimesedAlgabTahega(i: list, p: list, taht: str):
    """
    Находит имена, начинающиеся с введенной буквы, и соответствующие зарплаты.

    :param list i: Список имен
    :param list p: Список зарплат
    :param str taht: Введенная буква
    """
    leitud_inimesed = [(name, salary) for name, salary in zip(i, p) if name.startswith(taht.capitalize())]
    for name, salary in leitud_inimesed:
        print(f"{name}: {salary} EUR")
        
def LisaPremia(i: list, p: list, nimi: str):
    """
    Начисляет премию в размере 10% от зарплаты выбранному сотруднику по имени.

    :param list i: Список имен
    :param list p: Список зарплат
    :param str nimi: Имя сотрудника
    :return: Списки имен и зарплат после начисления премии
    :rtype: tuple
    """
    if not p:
        print("Список зарплат пуст.")
        return i, p

    if nimi in i:
        idx = i.index(nimi)
        premia = p[idx] * 0.1
        p[idx] += premia
        print(f"{nimi} получил премию в размере 10%. Новая зарплата: {p[idx]} EUR")
    else:
        print("Такого имени не найдено.")

    return i, p
