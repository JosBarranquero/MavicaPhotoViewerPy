import argparse
import file_io as io
import errors

def main():
    # Parser for the application arguments
    # usage: mafovi.py [-h] -d DISK -o OUTPUT [-f FORMAT] [--wipe-disk | --no-wipe-disk]
    parser = argparse.ArgumentParser(description='Import pictures from a Sony Mavica floppy disk')
    parser.add_argument('-d', '--disk', type=str, required=True, help='path to Mavica disk')
    parser.add_argument('-o', '--output', type=str, required=True, help='path to copy the disk contents to')
    parser.add_argument('-f', '--format', type=str, default='%Y %m %d', help='output folder format (default %%Y %%m %%d)')
    parser.add_argument('--wipe-disk', type=bool, default=False, action=argparse.BooleanOptionalAction, help='delete the disk contents after importing')
    args = parser.parse_args()

    disk_path = args.disk
    output_path = args.output
    format = args.format
    wipe = args.wipe_disk

    try:
        io.initialize(disk_path)
        io.file_import(output_path, folder_format=format)
        if wipe:
            io.disk_delete()
        print('Done!')
    except errors.EmptyDiskError as e:
        print('Error: {0}'.format(e.message))
    except FileNotFoundError as e:
        print('Error: File ''{0}'' not found'.format(e.filename))

if __name__ == '__main__':
   main()
