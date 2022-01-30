import os
import sys

"""
script is written by Ruman Bhuiyan
script call example : python mfcudl_split_xdi_covidextpmy.py <input_data_file> <output_dir>
"""

def write_file(file_name, data):
    with open(file_name, 'a') as file:
        for each_line in data:
            file.write(each_line)
    # free up memory
    data.clear()


def check_and_remove(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def check_letter_assign_data(letter_type, file_data, file109_data, file110_data):
    if letter_type == 0:
        file109_data = file109_data[0:]+file_data[0:]
    else:
        file110_data = file110_data[0:]+file_data[0:]
    # free up memory
    file_data.clear()
    return [file109_data, file110_data]


def main(input_file_path, output_folder_path):
    # if MFCUDL109.DAT and MFCUDL110.DAT are generated due to previous script call
    # then remove these two data files
    check_and_remove('{0}/MFCUDL109.DAT'.format(output_folder_path))
    check_and_remove('{0}/MFCUDL110.DAT'.format(output_folder_path))

    file_data = []  # stores real data files data
    file109_data = []  # stores data for letter 109
    file110_data = []  # stores data for letter 110
    anchor_counter = 0
    nesting_counter = 0
    letter_type = None

    # open data file which came as a paramater in argv at the time of script call
    with open(input_file_path) as data_file:
        for line in data_file:
            # if this is anchor line then decide where to keep file_data that you read before
            if line.strip() == '[COVIDEXTPMT]':
                anchor_counter += 1
                if letter_type in [0, 1]:
                    file109_data, file110_data = check_letter_assign_data(letter_type, file_data, file109_data,
                                                                          file110_data)

            file_data.append(line)

            # if this line contains double nesting verbiage then check the equality of number of 
            # anchors and number of double nesting verbiages. If they aren't equal then throw error
            if line.strip().startswith('accountNumber'):
                nesting_counter += 1
                if nesting_counter > anchor_counter:
                    raise Exception('Double nesting issue due to missing anchor!')

            if line.strip().startswith('letterType'):
                letter_type = int(line.strip().split('=')[1])

                if letter_type not in [0, 1]:
                    raise Exception('Letter type can\'t be anything else except 0 or 1')
                else:
                    file109_data, file110_data = check_letter_assign_data(letter_type, file_data, file109_data,
                                                                          file110_data)

    # at the end of file we didn't get any anchor thats why file_data has few data to assign again
    if len(file_data) != 0:
        file109_data, file110_data = check_letter_assign_data(letter_type, file_data, file109_data, file110_data)

    # write down the data file taking data from their respective list
    write_file('{0}/MFCUDL109.DAT'.format(output_folder_path), file109_data)
    write_file('{0}/MFCUDL110.DAT'.format(output_folder_path), file110_data)


if __name__ == '__main__':
    # check whether data file name & output directory path came as parameter or not
    if len(sys.argv) != 3:
        raise Exception(
            'Invalid arguments! Usage: python mfcudl_split_xdi_covidextpmy.py <input_data_file> <output_dir>')

    main(sys.argv[1], sys.argv[2])
