#! /usr/bin/python3

import os, logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def mkdir(path):
    if os.path.exists(path):
        logging.info('folder %s already exists...'%(path))
    else:
        os.makedirs(path)
        logging.info('folder %s created...' %(path))


def tif2png(tif_file, png_file):
    os.system('convert %s %s' %(tif_file, png_file))


def get_tif_count(input_root):
    count = 0
    for root, dirs, files in os.walk(input_root):
        for filename in files:
            fname, ext = os.path.splitext(filename)
            if ext == '.tiff' or ext == '.tif':
                count += 1
    return count


def main(input_root, output_root):
    tif_count = get_tif_count(input_root)
    png_count = 0
    mkdir(output_root)
    for root, dirs, files in os.walk(input_root):
        target_root = root.replace(input_root, output_root)
        logging.info('output --> %s' %target_root)
        dirs.sort()
        for folder in dirs:
            path = os.path.join(target_root, folder)
            mkdir(path)
        files.sort()
        for filename in files:
            path = os.path.join(root, filename)
            path = '\"' + path + '\"'
            fname, ext = os.path.splitext(filename)
            if ext == '.tiff' or ext == '.tif':
                target_filename = fname + '.png'
                target_path = os.path.join(target_root, target_filename)
                target_path = '\"' + target_path + '\"'
                tif2png(path, target_path)
                png_count += 1
                logging.info('tif2png %d/%d done, out --> %s' %(png_count, tif_count, target_filename))
            else:
                logging.info('not tif, pass... in <-- %s' %(filename))
    

if __name__ == '__main__':
    # import argparse
    # parser = argparse.ArgumentParser(description='convert tif to png recursively.')
    # parser.add_argument('--input_root', '-i', required=True, help='path of the folder which holds tif files')
    # parser.add_argument('--output_root', '-o', required=True, help='path of the folder where you want png files stored')
    # args = parser.parse_args()
    # main(args.input_root, args.output_root)
    import sys
    if len(sys.argv) < 3:
        print("usage: tif2png <input_dir> <output_dir>")
        exit()
    input_root = sys.argv[1]
    output_root = sys.argv[2]
    main(input_root, output_root)

