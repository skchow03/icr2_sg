import argparse
from sg_classes import SGFile


def main():
    parser = argparse.ArgumentParser(description='Converts CSV files to SG format.')
    parser.add_argument('header_csv', help='CSV file containing the header data.')
    parser.add_argument('section_csv', help='CSV file containing the section data.')
    parser.add_argument('output_sg', help='Output file in SG format.')

    args = parser.parse_args()

    # Load data from CSV files and create SGFile object
    sgfile = SGFile.from_csv(args.header_csv, args.section_csv)

    # Output the SG file
    sgfile.output_sg(args.output_sg)


if __name__ == '__main__':
    main()
