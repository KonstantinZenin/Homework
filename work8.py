secret_letter = [
    ['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
    ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'],
    ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
    ['и$##sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
    ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']
]

decrypted_message = ""

small_rus = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]


for array in secret_letter:
    for word in array:
        for letter in word:
            if letter in small_rus:
                decrypted_message += letter
    decrypted_message += ' '

print(decrypted_message)
input('Для выхода из программы нажмите Enter')
