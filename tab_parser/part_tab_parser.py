# depend on .tab file, because there are colunm names and column contet not separated by anything but human logic
# so if you want to recognize them you have to set column sizes depend on what you see in different srtings of .tab file
COL_SIZES = [60, 12, 12, 12, 12, 12, 6, 6, 6, 6, 6, 18, 12, 6, 6, 6, 6, 12, 24, 36, 60] 

TAKE_COL_NUM = [0, 1, 12 ]

if __name__ == "__main__":

        file_desc = open('orig_data/Sirena-export-fixed.tab', 'r', encoding='UTF8')

        new_file_desc = open('orig_data/out/Sirena-export-fixed-part.csv','w', encoding='UTF8')

        unnamed_columns = 0
        i = 0 # nomer stroki

        for line in file_desc:
                new_line = ''
                j = 0 # nomer stolbca
                for lenth in COL_SIZES:
                        col_content = line[:lenth]
                        line = line[lenth:]
                        if j in TAKE_COL_NUM: #нужная колонка
                                col_content = col_content.strip()
                                if not j: #фио надо разделить
                                        if not i: # имена колонок
                                                col_content = 'famil;name;otchestvo'
                                        else: # данные
                                                lst = col_content.split()
                                                col_content = lst[0] + ';' + lst[1] + ';' + lst[2]
                                elif not col_content or col_content == 'N/A':
                                        if not i:
                                                unnamed_columns += 1
                                                col_content = 'UnnamedColumn' + str(unnamed_columns)
                                        else:
                                                col_content = ''
                                if not new_line:
                                        new_line = col_content
                                else:
                                        new_line = new_line + ';' + col_content
                        j += 1
                if not i:
                        new_file_desc.write(new_line + '\n\n')
                        i = 1
                else:
                        new_file_desc.write(new_line + '\n')

        file_desc.close()
        new_file_desc.close()
