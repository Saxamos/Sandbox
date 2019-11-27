import csv
import re


def _clean(s):
    return ' '.join(re.findall(r'\w+', s, flags=re.UNICODE)).lower()


def convert_to_vw(dataset_part='train'):
    assert dataset_part in ['test', 'train']

    k = 1 if dataset_part == 'test' else 0
    i = 0

    with open(f'{dataset_part}_titanic.csv', 'r') as infile, open(f'{dataset_part}.vw', 'w') as outfile:
        for line in csv.reader(infile):
            i += 1
            if i > 1:
                vw_line = ''

                if dataset_part == 'train':
                    if str(line[1]) == '1':
                        vw_line += '1 \''
                    else:
                        vw_line += '-1 \''
                elif dataset_part == 'test':
                    vw_line += '1 \''

                vw_line += str(line[0]) + ' |f '
                vw_line += 'passenger_class_' + str(line[2 - k]) + ' '

                vw_line += 'last_name_' + _clean(line[3 - k].split(',')[0]).replace(' ', '_') + ' '
                vw_line += 'title_' + _clean(line[3 - k].split(',')[1]).split()[0] + ' '
                vw_line += 'sex_' + _clean(line[4 - k]) + ' '
                if len(str(line[5 - k])) > 0:
                    vw_line += 'age:' + str(line[5 - k]) + ' '
                vw_line += 'siblings_onboard:' + str(line[6 - k]) + ' '
                vw_line += 'family_members_onboard:' + str(line[7 - k]) + ' '
                vw_line += 'embarked_' + str(line[11 - k]) + ' '
                outfile.write(vw_line[:-1] + '\n')


convert_to_vw('test')
convert_to_vw()
