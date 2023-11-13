import argparse
import file_io as io

def main():
    # Parser for the application arguments
    # usage: mafovi.py [-h] -d DISK -o OUTPUT [-f | --format | --no-format]
    parser = argparse.ArgumentParser(description='Import pictures from a Sony Mavica floppy disk')
    parser.add_argument("-d", "--disk", type=str, required=True, help="path to Mavica disk")
    parser.add_argument("-o", "--output", type=str, required=True, help="path to copy the disk contents to")
    parser.add_argument("-f", "--format", type=bool, default=False, action=argparse.BooleanOptionalAction, help="delete the disk contents after importing")
    args = parser.parse_args()

    disk_path = args.disk
    output_path = args.output
    format = args.format

    io.initialize(disk_path)
    io.file_import(output_path)
    if format:
        io.disk_delete()

if __name__ == "__main__":
   main()
