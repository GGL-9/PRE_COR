# 初始化存储数据的字典
ground_dict = {}
vege_dict = {}
#1.根据脉冲索引号，合并每个脉冲对应的Rg和Rv
# 读取ground.txt文件
with open(r'D:\part1\progress_data\subsample\point_density5_cylinder\60\ground_correction_final.txt', 'r') as ground_file:
    for line in ground_file:
        parts = line.strip().split()
        if len(parts) >= 9:
            seventh_col = parts[6]
            ninth_col = float(parts[8])
            if seventh_col not in ground_dict:
                ground_dict[seventh_col] = {'first_line': line, 'ninth_sum': ninth_col}
            else:
                ground_dict[seventh_col]['ninth_sum'] += ninth_col

# 读取vege.txt文件
with open(r'D:\part1\progress_data\subsample\point_density5_cylinder\60\vege_correction_final.txt', 'r') as vege_file:
    for line in vege_file:
        parts = line.strip().split()
        if len(parts) >= 9:
            seventh_col = parts[6]
            ninth_col = float(parts[8])
            if seventh_col not in vege_dict:
                vege_dict[seventh_col] = {'first_line': line, 'ninth_sum': ninth_col}
            else:
                vege_dict[seventh_col]['ninth_sum'] += ninth_col

def output_result(data_dict, output_filename):
    with open(output_filename, 'w') as output_file:
        for key, value in data_dict.items():
            first_line = value['first_line']
            ninth_sum = value['ninth_sum']
            line_parts = first_line.split()
            line_parts[8] = str(ninth_sum)
            output_file.write('\t'.join(line_parts) + '\n')
output_result(ground_dict, r'D:\part1\progress_data\subsample\point_density5_cylinder\60\ground_correction_final_Rg.txt')
output_result(vege_dict, r'D:\part1\progress_data\subsample\point_density5_cylinder\60\vege_correction_final_Rv.txt')

#下面的代码根据脉冲索引号，找到地面——植被脉冲，并给出每个脉冲对应的Rg和Rv

def read_file_to_dict_by_seventh_col(filename):
    data_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 9:
                seventh_col = parts[6]
                data_dict[seventh_col] = parts
    return data_dict

def process_and_write_combined_file(ground_filename, vege_filename, output_filename):
    ground_dict = read_file_to_dict_by_seventh_col(ground_filename)
    vege_dict = read_file_to_dict_by_seventh_col(vege_filename)

    with open(output_filename, 'w') as output_file:
        for seventh_col, ground_row in ground_dict.items():
            if seventh_col in vege_dict:
                vege_ninth_col = vege_dict[seventh_col][8]
                combined_row = ground_row + [vege_ninth_col]
                output_file.write('\t'.join(combined_row) + '\n')

process_and_write_combined_file(
    r'D:\part1\progress_data\subsample\point_density5_cylinder\60\ground_correction_final_Rg.txt',
    r'D:\part1\progress_data\subsample\point_density5_cylinder\60\vege_correction_final_Rv.txt',
    r'D:\part1\progress_data\subsample\point_density5_cylinder\60\correction_location_Rg_Rv.txt'
)