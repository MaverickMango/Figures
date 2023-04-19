from tabulate import tabulate
import pandas as pd
import utils.read_file_tools as rft
from astor import beans_clz as clz


def read_bug_infos(bug_tuple_lst: list) -> list:
    bug_infos = []  # [(bug, bug_info)]
    for bug in bug_tuple_lst:
        proj = bug[0]
        version = bug[1]
        target_dir = "VBAPRMain-" + proj + "_" + version + "/"
        target_file = "astor_output.json"
        json_file_path = base_dir + work_dir + proj + "/" + target_dir + target_file
        # json_data = rft.read_json_file(json_file_path)  # dict
        # clz.BugInfoDecoder().decode(json.dumps(json_data))
        bug_info = rft.read_json_to_object(json_file_path, clz.BugInfoDecoder)
        if bug_info is None:
            continue
        bug_infos.append((bug, bug_info))
        # print(bug_info)
    return bug_infos


def print_table_example():
    a = [1, 1, 1, 1]
    b = [2, 2, 2, 2]
    c = [3, 3, 3, 3]
    A = pd.DataFrame([b, a, c], index=['b', 'a', 'c'])
    A.columns = ['1', '2', '3', '4']
    A.index.names = ['proj_id']
    A.columns.names = ['info']
    h = [A.index.names[0] + '/' + A.columns.names[0]] + list(A.columns)
    print(tabulate(A, headers=h, tablefmt='grid'))


def print_table(line=[], line_index=[], column_index=[], index_name=[], column_name=[], table_format="grid"):
    A = pd.DataFrame(line, index=line_index)
    A.columns = column_index
    A.index.names = index_name
    A.columns.names = column_name
    h = [A.index.names[0] + '/' + A.columns.names[0]] + list(A.columns)
    '''tablefmt
    "plain" "simple" "github" "grid" "fancy_grid" "pipe"
    "orgtbl" "jira" "presto" "psql" "rst" "mediawiki" "moinmoin"
    "youtrack" "html" "latex" "latex_raw" "latex_booktabs" "textile"
    '''
    print(tabulate(A, headers=h, tablefmt=table_format))


def get_general_csv(bug_info_lst):
    if len(bug_info_lst) == 0:
        return ""
    lines = []
    line_index = []
    column_index = bug_info_lst[0][1].general.__dir__()
    column_index.append("patches_num")
    index_name = ["proj_id"]
    column_name = ["info"]
    csv = ",".join([index_name[0] + "/" + column_name[0], ",".join(column_index)])
    for bug_info in bug_info_lst:
        general_info = bug_info[1].general.to_list()
        general_info.append(str(len(bug_info[1].patches)))
        lines.append(general_info)
        index = bug_info[0][0] + "_" + bug_info[0][1]
        line_index.append(index)
        current_line = ",".join([index, ",".join(general_info)])
        csv = "\n".join([csv, current_line])
    return csv, lines, line_index, column_index


if __name__ == '__main__':
    base_dir = "/home/liumengjiao/Desktop/"
    work_dir = "VBAPRResult/"
    bugs_file = "vbaprinfo/bugs4.txt"
    # print_table_example()
    bugs = rft.split_proj_ids_file(base_dir + bugs_file)  # list: [(proj, id)]
    bug_info_lst = read_bug_infos(bugs)
    csv, lines, line_index, column_index = get_general_csv(bug_info_lst)
    info_file = "".join([base_dir, work_dir, "info.csv"])
    rft.write_to_file(info_file, csv)
    print_table(lines, line_index, column_index, ["proj_id"], ["info"], "pipe")