import argparse

def main():
    # Parser for the application arguments
    # usage: mafovi.py [-h] -d DISK -o OUTPUT [-f | --format | --no-format]
    parser = argparse.ArgumentParser(description='Import pictures from a Sony Mavica floppy disk')
    parser.add_argument("-d", "--disk", type=str, required=True, help="path to Mavica disk")
    parser.add_argument("-o", "--output", type=str, required=True, help="path to copy the disk contents to")
    parser.add_argument("-f", "--format", type=bool, default=False, action=argparse.BooleanOptionalAction, help="delete the file contents after import")
    args = parser.parse_args()

    disk_path = args.disk
    output_path = args.output
    format = args.format

    print('Disk path:', disk_path, '\nOutput path: ', output_path, '\nFormat: ', format)

if __name__ == "__main__":
   main()
