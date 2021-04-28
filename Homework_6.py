import pathlib
import sys
import shutil
import os

image_ext = ['JPEG', 'PNG', 'JPG', 'SVG']
video_ext = ['AVI', 'MP4', 'MOV', 'MKV']
doc_ext = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
music_ext = ['MP3', 'OGG', 'WAV', 'AMR']
arc_ext = ['ZIP', 'GZ', 'TAR']
images = {}
videos = {}
documents = {}
musics = {}
archives = {}
unknown = {}
folders = ['archives', 'video', 'audio', 'documents', 'images', 'unknown']
source_dir = None


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
    alphabet_ua = 'абвгдеєжзиійклмнопрстуфхцчшщьюя'
    alphabet_eng = 'abcdefghijklmnoprstuvxqwryz'
    numbers = '0123456789'
    res = alphabet_ua + alphabet_ua.upper() + alphabet_eng + \
        alphabet_eng.upper() + numbers + '.'
    new_str = ''
    for n in str:
        if n not in res:
            new_str += '_'
        else:
            new_str += n

    return new_str


def path_combine(parent, child):
    return pathlib.Path(os.path.join(parent, child))


def move_file(file_path, place):
    folder = path_combine(source_dir, place)
    if not folder.exists():
        folder.mkdir()
    shutil.move(file_path, path_combine(folder, file_path.name))


def recursive(path):

    if path.exists():
        if path.is_dir():
            # print(path)
            for el in path.iterdir():
                if el.name in folders:
                    return

                if remove_folder_ifempty(el):
                    return

                new_el = normalize(remove_spec(el.name))
                if el.name != new_el:
                    el = el.rename(f'{el.parent}\{new_el}')
                recursive(el)
                if remove_folder_ifempty(el):
                    return
        else:
            index = -1
            try:
                index = path.name.rindex('.')
                extension = path.name[index+1:].upper()
            except ValueError:
                # print(path)
                pass

            if index != -1:
                if extension in image_ext:
                    images[path] = path.name
                    move_file(path, folders[4])
                elif extension in video_ext:
                    videos[path] = path.name
                    move_file(path, folders[1])
                elif extension in doc_ext:
                    documents[path] = path.name
                    move_file(path, folders[3])
                elif extension in music_ext:
                    musics[path] = path.name
                    move_file(path, folders[2])
                elif extension in arc_ext:
                    archives[path] = path.name
                    move_file(path, folders[0])
                else:
                    unknown[path] = path.name
                    move_file(path, folders[5])
            else:
                unknown[path] = path.name
                move_file(path, folders[5])
                print(unknown[path])
    else:
        print(f'Path {path.absolute()} not exist.')


def print_results(dict):
    for key in dict:
        print(f'---{key}')


def remove_folder_ifempty(path):
    if path.is_dir() and len(os.listdir(path)) == 0:
        print(f'{path} - will be removed')
        shutil.rmtree(path)
        return True
    else:
        return False


def main():
    # input = sys.argv[1]
    input = 'c:\sort_test'
    global source_dir
    source_dir = pathlib.Path(input)
    recursive(source_dir)

    print('Image files:')
    print_results(images)

    print('Video files:')
    print_results(videos)

    print('Doc files:')
    print_results(documents)

    print('Music files:')
    print_results(musics)

    print('Archives files:')
    print_results(archives)

    print('Unknown files:')
    print_results(unknown)


if __name__ == '__main__':
    main()
