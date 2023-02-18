print('about to convert csv to qif')
input_file_names = ["C:\\Users\\Jim\\Downloads\\savings1.csv","C:\\Users\\Jim\\Downloads\\savings2.csv","C:\\Users\\Jim\\Downloads\\checking.csv"]
output_file_names = ["C:\\Users\\Jim\Downloads\\savings1.qif","C:\\Users\\Jim\\Downloads\\savings2.qif","C:\\Users\\Jim\\Downloads\\checking.qif"]
for filenum in range(0,3):
    fileobject = open(input_file_names[filenum])
    print("input file {} opened:".format(input_file_names[filenum]))
    qif_file = open(output_file_names[filenum],"w+")
    print("output file {} opened:".format(output_file_names[filenum]))
    linesfromfile = fileobject.read()
    print(linesfromfile)
    print('printing again')
    linesarray = linesfromfile.splitlines()
    print(linesarray)
    number_of_entries = len(linesarray)
    print(number_of_entries)
    for line_entry in range (1,number_of_entries):
        print(linesarray[line_entry])
        sample_line = linesarray[line_entry]
        print("printing sample line...")
        print(sample_line)
        date_field, ref_field, type_field, desc_field,debit_field,credit_field,checkno_field,balance_field = sample_line.split(",")
        print('date',date_field)
        print('ref', ref_field)
        print('type', type_field)
        print('desc', desc_field)
        print('debit', debit_field)
        print('credit', credit_field)
        print('check no', checkno_field)
        print('balance', balance_field)
        #

        qif_file.write("!Type:Bank\n")
        qt, numx, qt = date_field.split('"')
        line_to_write = 'D{}\n'.format(numx)
        qif_file.write(line_to_write)
        #
        if type_field == '"CREDIT"':
            print('credit field')
            qt, numx, qt = credit_field.split('"')
            print(numx)
            line_to_write = 'T+{}\n'.format(numx)
            qif_file.write(line_to_write)
            qt, numx, qt = desc_field.split('"')
            print(numx)
            if numx == "EXPRESS SCRIPTS":
                line_to_write = 'LWages & Salary\n'
                qif_file.write(line_to_write)
            if numx == "Trs Des Ppms":
                line_to_write = 'Wages & Salary:Net Pay\n'
                qif_file.write(line_to_write)
        else:
            print('debit field')
            qt, numx, qt = debit_field.split('"')
            print(numx)
            line_to_write = 'T{}\n'.format(numx)
            qif_file.write(line_to_write)
            qt, numx, qt = desc_field.split('"')
            if numx == "ROCKLAND ELECTR":
                line_to_write = 'LUtilities:electricity\n'
                qif_file.write(line_to_write)
            if numx == "SUEZ WATER NEW J":
                line_to_write = 'LUtilities:water\n'
                qif_file.write(line_to_write)    
            if numx == "PUBLIC SERVICE":
                line_to_write = 'LUtilities:gas\n'
                qif_file.write(line_to_write)  
  
            if numx == "Amatrula":
                line_to_write = 'Home Improvement:gardener\n'
                qif_file.write(line_to_write)    


        #
        qt, numx, qt = desc_field.split('"')
        line_to_write = 'P{}\n'.format(numx)
        qif_file.write(line_to_write)
        qif_file.write('^\n')
    fileobject.close()
    qif_file.close()
    print("file: {} converted\n".format(input_file_names[filenum]))
