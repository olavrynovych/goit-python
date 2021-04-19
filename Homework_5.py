def normalize(inner_string):
    inner_string = remove_spec(inner_string)

    symbol_map = {ord("а"): "a", ord("б"): "b", ord("в"): "v", ord("г"): "g", ord("д"): "d", ord("е"): "eh", ord("є"): "e", ord("ж"): "zh", ord("з"): "z", ord("и"): "ih", ord("і"): "i",
     ord("й"): "y", ord("к"): "k", ord("л"): "l", ord("м"): "m", ord("н"): "n", ord("о"): "o", ord("п"): "p", ord("р"): "r", ord("с"): "s", ord("т"): "t", ord("у"): "u", ord("ф"): "f", ord("х"): "kh",
      ord("ц"): "c", ord("ч"): "ch", ord("ш"): "sh", ord("щ"): "shh", ord("ь"): "jh", ord("ю"): "ju", ord("я"): "ja",
      ord("А"): "A", ord("Б"): "B", ord("В"): "V", ord("Г"): "G", ord("Д"): "D", ord("Е"): "Eh", ord("Є"): "E", ord("Ж"): "Zh", ord("З"): "Z", ord("И"): "Ih", ord("І"): "I",
     ord("Й"): "Y", ord("К"): "K", ord("Л"): "L", ord("М"): "M", ord("Н"): "N", ord("О"): "O", ord("П"): "P", ord("Р"): "R", ord("С"): "S", ord("Т"): "T", ord("У"): "U", ord("Ф"): "F", ord("Х"): "Kh",
      ord("Ц"): "C", ord("Ч"): "Ch", ord("Ш"): "Sh", ord("Щ"): "Shh", ord("Ю"): "Ju", ord("Я"): "Ja",
      }
    return inner_string.translate(symbol_map)

def remove_spec(str):
    alphabet = 'абвгдеєжзиійклмнопрстуфхцчшщьюя'
    numbers = '0123456789'
    res = alphabet + alphabet.upper() + numbers
    new_str = ''
    for n in str:
        if n not in res:
            new_str += '_'
        else:
            new_str += n
    
    return new_str


    


