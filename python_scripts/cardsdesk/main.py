from math import factorial


class CardsDesk:
    # минимальное и максимальное значения на картах
    NUMBER_RANGE = [1, 7]
    # число всех возможных значений (не трогать)
    size = NUMBER_RANGE[1] - NUMBER_RANGE[0] + 1
    # число значений на одной карте из колоды
    CARD_NUM_COUNT = 4
    # максимальная сумма значений
    MAX_CARD_NUM_SUM = 11
    # минимальная сумма значений
    MIN_CARD_NUM_SUM = 5

    @staticmethod
    def getCountOfNumbersPairs() -> int:
        # колличество пар значений (карт), удовлетворяющих условию:
        # сумма всех значений карты меньше или равно MAX_CARD_NUM_SUM

        # количество всех сочетаний с повторениями
        all_combs_count = CardsDesk.getAllCombinations()
        # все возможные значения сумм
        all_sums = {}
        # временное зналище чисел на основе диапозона из NUMBER_RANGE
        numbers = []
        for i in range(CardsDesk.NUMBER_RANGE[0], CardsDesk.NUMBER_RANGE[1] + 1):
            numbers.append(i)
        # счётчик для сочетаний (увеличивается, когда нет повторов)
        counter = 0
        # счётчик для индексов чисел (увеличивается постоянно)
        numbers_counter = 0
        while counter < all_combs_count:
            indexes = CardsDesk.getIndexesFromCounter(numbers_counter)
            # сумма значений карты
            temp_sum = 0
            # значения карты
            temp_numbers = []
            # все значения в виде одного числа для уменьшения занимаемой памяти
            numbers_in_one = 0
            for i in indexes:
                temp_sum += numbers[i]
                temp_numbers.append(numbers[i])
            temp_numbers.sort()
            for i in range(len(temp_numbers)):
                numbers_in_one = numbers_in_one + temp_numbers[i] * 10 ** i
            if all_sums.get(temp_sum) is None:
                all_sums[temp_sum] = []
            temp_numbers = all_sums[temp_sum]
            if numbers_in_one not in temp_numbers:
                all_sums[temp_sum].append(numbers_in_one)
                counter += 1
            numbers_counter += 1
        # подсчёт самой суммы по условию
        result_count = 0
        for key in all_sums:
            # вывод всех сумм
            # print(key, ': ', all_sums[key])
            if CardsDesk.MIN_CARD_NUM_SUM <= key <= CardsDesk.MAX_CARD_NUM_SUM:
                print(all_sums[key])
                result_count += len(all_sums[key])
        return result_count

    @staticmethod
    def getIndexesFromCounter(counter: int = 0):
        # последовательное вытаскавание индексов заместо циклов в цикле
        indexes = []
        for i in range(CardsDesk.CARD_NUM_COUNT):
            indexes.append(counter // (CardsDesk.size**i) % CardsDesk.size)
        return indexes

    @staticmethod
    def getAllCombinations() -> int:
        # расчёт сочетаний по формуле с повторениями
        comb_c = CardsDesk.size + CardsDesk.CARD_NUM_COUNT - 1
        temp_up = factorial(comb_c)
        temp_down = factorial(CardsDesk.size - 1) * factorial(CardsDesk.CARD_NUM_COUNT)
        return temp_up // temp_down

print(CardsDesk.getCountOfNumbersPairs())
