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
    #Principal_Person_Sex   
    process_input_file(fname, ["V2036"], output_size=250, random_lines=True, sep=',')
    #EconomicImpact_DirectLoss
    process_input_file(fname, ["V4317_1","V4318_1","V4319_1","V4320_1","V4360_1","V4361_1","V4362_1","V4363_1"], output_size=250, random_lines=True, sep=',')
    #  EconomicImpact_IndirectLoss
    process_input_file(fname, ["VS298","VS299","VS300","VS301","VS358"], output_size=250, random_lines=True, sep=',')
    #  Financial_Problems
    process_input_file(fname, ["VS102","VS103","VS302","VS303","VS304","VS359","VS360","VS363","VS010","VS330","VS331","V4482B_1"], output_size=250, random_lines=True, sep=',')
    #  Legal_Problems
    process_input_file(fname, ["VS315","VS316","VS353","VS330","VS331"], output_size=250, random_lines=True, sep=',')
    # Most_Recent  
    process_input_file(fname, ["VS090","VS091","VS092","VS093","VS094"], output_size=250, random_lines=True, sep=',')
   

if __name__ == "__main__":
    main()
