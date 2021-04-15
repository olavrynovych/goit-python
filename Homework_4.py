import pathlib
import sys

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
    
def recursive(path):
    
    if path.exists():
        if path.is_dir():
            ##print(path)
            for el in path.iterdir():
                recursive(el)
        else:
            index = -1
            try:
                index = path.name.rindex('.')
                extension = path.name[index+1:].upper()
            except ValueError:
                #print(path)
                pass

            if index != -1:
                if extension in image_ext:
                    images[path] = path.name
                elif extension in video_ext:
                    videos[path] = path.name
                elif extension in doc_ext:
                    documents[path] = path.name
                elif extension in music_ext:
                    musics[path] = path.name
                elif extension in arc_ext:
                    archives[path] = path.name
                else:
                    unknown[path] = path.name
            else:
                unknown[path] = path.name
                print(unknown[path])
    else:
        print(f'Path {path.absolute()} not exist.')

def print_results(dict):
    for key in dict:
        print(f'---{key}')

def main():
    input = sys.argv[1]
    
    folder_path = pathlib.Path(input)
    recursive(folder_path)

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

