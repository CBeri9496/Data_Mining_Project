import sys
import random

SKIP_INTERVAL = 25

def process_input_file(filename, variables, sep='\t', output_size=10, random_lines=False):
    with open(filename) as fi:
        variables_indices = []

        # intialize the lines to skip
        if random_lines:
            skip_count = random.randint(1, SKIP_INTERVAL)
        else:
            skip_count = 0

        # process the header -> get the index # of the variables and store them (in order)
        header = fi.next().split()
        for v in variables:
            variables_indices.append(header.index(v))

        # process the rest of the file
        line_count = 0
        for line in fi:
            if skip_count:
                skip_count -= 1
            else:
                if line_count < output_size+1:
                    line_data = line.split()
                    print sep.join([line_data[v] for v in variables_indices])
                    line_count += 1

                    if random_lines: # re-initialize
                        skip_count = random.randint(1, SKIP_INTERVAL)
                else:
                    break # we need not process more of the file than necessary


def main():
    fname = "C:\\Users\\Nagesh\\Desktop\\Datasets\\ICPSR_34735\\DS0001\\34735-0001-Data.tsv"
    process_input_file(fname, ["V3079","VS002","VS012","VS013","VS014","VS015","VS017","VS019"], output_size=250, random_lines=True, sep=',')

if __name__ == "__main__":
    main()
