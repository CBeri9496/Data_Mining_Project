import sys
import random

def process_input_file(filename, output_size=10, variables=["VS010"], random=False):
    with open(filename) as fi:
        variables_indices = []

        for line_number, line in enumerate(fi):
            line_data = line.split()

            if line_number == 0: # process the header -> get the index # of the variables
                for v in variables:
                    variables_indices.append(line_data.index(v))

            if line_number < output_size+1:
                print "\t".join([line_data[v] for v in variables_indices])


def main():
    fname = "C:\\Users\\Keith\\Downloads\\26362-0001-Data.tsv"
    process_input_file(fname, variables=["V3079","VS002","VS012","VS013","VS014","VS015","VS017","VS019"], output_size=500)

if __name__ == "__main__":
    main()