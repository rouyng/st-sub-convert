import csv
import sys
import getopt

st_csv = 'traditional_simplified.csv'

def main(argv):
    input_file = ''
    output_file = ''
    input_char = 's'
    try:
        opts, args = getopt.getopt(argv, "hi:o:l:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('converter.py -i <inputfile> -o <outputfile> -l <s for simplified input, t for traditional input>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('converter.py -i <inputfile> -o <outputfile> -l <s for simplified input, t for traditional input>')
            sys.exit()
        elif opt == "-i":
            input_file = arg
        elif opt == '-o':
            output_file = arg
        elif opt == '-l':
            input_char = arg

    if input_char not in ('s', 't'):    # -l option should be 's' or 't', if not, exit
        print('-l option must be "s" or "t"')
        sys.exit(2)

    print(f'Input: {input_file}')

    # open the csv file containing the traditional/simplified conversion chart
    with open(st_csv, encoding='gbk') as d:
        reader = csv.reader(d, delimiter=',')
        # make a translation table from the csv file
        if input_char == 's':
            st_ttrans = str.maketrans({row[0]: row[1] for row in reader})
        else:
            st_ttrans = str.maketrans({row[1]: row[0] for row in reader})

    output = []

    # open the input file, translate each line and append it to the output list
    with open(input_file, mode='r', encoding='utf8') as f:
        for line in f:
            output.append(line.translate(st_ttrans))

    # write each translated line to the output file
    with open(output_file, mode='w', encoding='utf8') as f:
        for line in output:
            f.write(line)

    print(f'Output: {output_file}')


if __name__ == '__main__':
    main(sys.argv[1:])
