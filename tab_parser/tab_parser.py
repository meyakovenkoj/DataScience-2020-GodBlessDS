# depend on .tab file, because there are colunm names and column contet not separated by anything but human logic
# so if you want to recognize them you have to set column sizes depend on what you see in different srtings of .tab file
COL_SIZES = [60, 12, 12, 12, 12, 12, 6, 6, 6, 6, 6, 18, 12, 6, 6, 6, 6, 12, 24, 36, 60] 

if __name__ == "__main__":

        file_desc = open('orig_data/Sirena-export-fixed.tab', 'r')

        new_file_desc = open('orig_data/out/Sirena-export-fixed.csv','w')

        unnamed_columns = 0
        i = 0

        for line in file_desc:
                new_line = ''
                for lenth in COL_SIZES:
                        col_content = line[:lenth]
                        line = line[lenth:]
                        col_content = col_content.strip()
                        if not col_content:
                                if not i:
                                        unnamed_columns += 1
                                        col_content = 'UnnamedColumn' + str(unnamed_columns)
                                else:
                                        col_content = 'Null'
                        if not new_line:
                                new_line = col_content
                        else:
                                new_line = new_line + ';' + col_content
                if not i:
                        new_file_desc.write(new_line + '\n\n')
                        i = 1
                else:
                        new_file_desc.write(new_line + '\n')

        file_desc.close()
        new_file_desc.close()
