import argparse

from srt_file import SrtFile
from translator import Translator

def run(in_path, out_path, auth_key, dst_lang):

    translator = Translator(auth_key, dst_lang)
    srt_file = SrtFile(in_path)

    for idx in range(len(srt_file)):
        src_content = srt_file.content(idx)
        dst_content = translator.translate(src_content)
        print(f'{src_content} -> {dst_content}')
        srt_file.set_content(idx, dst_content)

    srt_file.save(out_path)

if __name__ == '__main__':

    print('run')

    parser = argparse.ArgumentParser(description='add two integers')
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-a', '--auth_key', type=str)
    parser.add_argument('-l', '--dst_lang', type=str, default='JA')
    args = parser.parse_args()

    run(args.input, args.output, args.auth_key, args.dst_lang)
