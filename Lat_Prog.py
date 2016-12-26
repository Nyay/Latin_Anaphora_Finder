import re

def main():
    I = 0                                                               # Чисто формальные переменные.
    FINAL = []                                                          # Чисто формальные переменные.
    FILE_NAME = input('Введите название файла: ')
    RESULT_FILE = open( 'program_result.txt','a', encoding='UTF-8')
    TEXT = open( FILE_NAME,'r', encoding='UTF-8')                       # Выбор Файла для нахождения Анафор.
    TEXT = TEXT.read()                                                  # Чтение текста.
    TEXT_LOW = TEXT.lower()                                             # Приводим к нижнему регистру.
    TEXT_LOW_CLEAN = re.sub(' \w\.', '',TEXT_LOW)
    TEXT_LOW_CLEAN = re.sub('\n', '', TEXT_LOW_CLEAN)
    TEXT_LOW_CLEAN = re.sub(' ', '\n', TEXT_LOW_CLEAN)
    TEXT_LOW_CLEAN = re.sub(',', '\n=', TEXT_LOW_CLEAN)                 # Задаем один вид для знаков(,.!?).
    TEXT_LOW_CLEAN = re.sub('\.', '\n=', TEXT_LOW_CLEAN)
    TEXT_LOW_CLEAN = re.sub('!', '\n=', TEXT_LOW_CLEAN)
    TEXT_LOW_CLEAN = re.sub('\?', '\n=', TEXT_LOW_CLEAN)
    TEXT_LOW_CLEAN = re.sub(';', '\n=', TEXT_LOW_CLEAN)
    NDD_CONST = re.findall('=\n(.+?)\n', TEXT_LOW_CLEAN)                # Поиск слов идущих после знаков.
    for X in range(len(NDD_CONST)-1):                                   # Смотрим какие из них повторяются.
        if NDD_CONST[X] == NDD_CONST[X+1]:
            I +=1
            X +=1
        else:
            LINE = NDD_CONST[X] + ' ' + str(I)
            if '0' in LINE:                                             # Отделяем значения >= 1
                continue
            else:
                FINAL.append(LINE)
            I = 0
            X +=1
    FINAL_TEXT = '\n'.join(FINAL)                                       # Создаем построчный текст.
    RESULT_FILE.write('\n\nНазвание Файла:\n\n' + FILE_NAME + '\n\nРезультат поиска:\n\n' + FINAL_TEXT)
    #print( 'Список Анафор которые нашлись в этом тексте(1 - соответствует 2 словам после знако): \n\n' + FINAL_TEXT)

if __name__ == '__main__':
    main()