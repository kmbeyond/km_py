
'''
1.Read data string, split & format
 (a):generate_message_body(): as simple text
 (b):generate_message_body_report(): as HTML table
 (c):generate_message_body_report_grouping(): as HTML table with grouping
2.Save HTML formatted string to file

'''

#string data
result="1.2|1.3|1.5|1.336565|1.26|1.28|1.45|1.56^2.3|2.5|2.6|2.1355435|null|2.43|2.55|2.56^3.4|3.5|3.9|3.14|3.27|3.25|3.34|3.42^"
result="TYPE1|CAT1|SUBCAT1|1.336565|1.42|1.28|1.45|1.56^TYPE1|CAT1|SUBCAT1|1.336565|1.42|1.28|1.45|1.56^TYPE2|CAT1|SUBCAT1|2.3355435|null|2.43|2.55|2.56^TYPE1|CAT2|SUBCAT2|3.44|3.27|3.25|3.34|3.42^TYPE1|CAT3|SUBCAT1|4.33|4.27|4.25|4.34|4.42^"
#result=""

replace_chars = "[(',)]"
for ch in replace_chars:
    result = result.replace(ch, '')

def get_report_datetime():
    from datetime import datetime
    dtNow = datetime.today()
    return str(dtNow.strftime('%m/%d/%Y %H:%M:%S'))

def get_report_year_month():
    from datetime import datetime
    dtNow = datetime.today()
    months=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    return "-".join([str(dtNow.year), months[dtNow.month-1]])

def generate_message_body(raw_string):
    rows = [x for x in raw_string.split('^') if x]
    #rows = list(set(rows))
    print(rows)
    msg_body = f"Report: {get_report_year_month()}"
    msg_body += "\n\nTYPE,CATEGORY,SUB-CATEGORY,THRESHOLD,MEASURE1,MEASURE2,MEASURE3,MEASURE4\n"
    if len(rows)>0:
        for itm in sorted(rows):
            itm_cols = itm.split('|')
            msg_body += "{},{},{}, *{}*,{},{},{},{} \n".format(itm_cols[0], itm_cols[1], itm_cols[2], round(float(itm_cols[3]), 3) if itm_cols[3].replace('.', '', 1).isdigit() else itm_cols[3],
                                                               ('' if 'null' in itm_cols[4] else itm_cols[4]), itm_cols[5], itm_cols[6], itm_cols[7])
        msg_body += "\n"
    else:
        msg_body += "NONE"
    print(f"FINAL MESSAGE: {msg_body}")
    return(msg_body)

#msg_body = generate_message_body(result)
#print(msg_body)

def generate_message_body_report(raw_string):
    rows = [x for x in raw_string.split('^') if x]
    print(rows)
    msg_body = f"<br><br><h3>Report: {get_report_year_month()}</h3>"
    columns = ['<th>TYPE','<th>CATEGORY','<th>SUB-CATEGORY','<th>THRESHOLD','<th>MEASURE1','<th>MEASURE2','<th>MEASURE3','<th>MEASURE4']
    msg_body += "<table border=1 cellspacing=0><tr bgcolor='abd674'>"+"".join(columns)+"</tr>"
    if len(rows)>0:
        for itm in sorted(rows):
            itm_cols = itm.split('|')
            msg_body += "<tr><td>{}<td>{}<td>{}<td align=right>{}<td align=right>{}<td align=right>{}<td align=right>{}<td align=right>{}</tr>".format(itm_cols[0], itm_cols[1], itm_cols[2],
                                                                                             round(float(itm_cols[3]), 3) if itm_cols[3].replace('.', '', 1).isdigit() else itm_cols[3],
                                                                                             ('' if 'null' in itm_cols[4] else itm_cols[4]), itm_cols[5], itm_cols[6], itm_cols[7])
            #msg_body += "<tr><td>" + "<td>".join([itm_cols[0], itm_cols[1], itm_cols[2],
            #                                  str(round(float(itm_cols[3]), 3) if itm_cols[3].replace('.', '',1).isdigit() else itm_cols[3]),
            #                                  str('' if 'null' in itm_cols[4] else itm_cols[4]), itm_cols[5],
            #                                  itm_cols[6], itm_cols[7]]) + "</tr>"
    else:
        msg_body += f"<tr><td colspan={len(columns)}>NO RECORDS</td></tr>"
    msg_body += "</table>"
    print(f"FINAL MESSAGE: {msg_body}")
    return(msg_body)

#msg_body = generate_message_body_report(result)
#print(msg_body)

def generate_message_body_report_grouping(raw_string):
    rows = [x for x in raw_string.split('^') if x]
    print(rows)
    for itm in sorted(rows):
        print(itm.split('|')[0] + " -> " + str(itm.split('|')[1:]))
    group_by_1 = {}
    for itm in sorted(rows):
        itm_cols = itm.split('|')
        #if itm_cols[0] in group_by_1:
        #    group_by_1[itm_cols[0]].append(itm_cols[1:])
        #else:
        #    group_by_1[itm_cols[0]] = [itm_cols[1:]]
        group_by_1[itm_cols[0]] = group_by_1[itm_cols[0]]+[itm_cols[1:]] if itm_cols[0] in group_by_1 else [itm_cols[1:]]
    print(group_by_1)
    #print(len(group_by_1))
    msg_body = f"<br><br><h3>Report: {get_report_year_month()}</h3>"
    columns = ['<th width=100>TYPE', '<th width=150>CATEGORY', '<th>SUB-CATEGORY', '<th align=center>THRESHOLD', '<th>MEASURE1', '<th>MEASURE2', '<th>MEASURE3', '<th>MEASURE4']
    msg_body += "<table border=1 cellspacing=0><tr bgcolor='abd674'>"+"".join(columns)+"</tr>"
    if len(group_by_1) > 0:
        for k,val in group_by_1.items():
            # print(f'key:{k} -> {len(group_by_1[k])}')
            grp1_spacing = f"<td valign=top rowspan={len(group_by_1[k])}>{k}"
            for itm in val:
                #print(f"->{itm}")
                msg_body += "<tr>"+grp1_spacing+ f"<td>{itm[0]}<td>{itm[1]}<td align=right>{round(float(itm[2]), 3) if itm[2].replace('.', '', 1).isdigit() else itm[2]}<td align=right>{('' if 'null' in itm[3] else float(itm[3]) if itm[3].replace('.', '', 1).isdigit() else itm[3])}<td align=right>{itm[4]}<td align=right>{itm[5]}<td>{float(itm[6]):.2f}</tr>"
                #msg_body += "<tr>"+grp1_spacing+ "<td>{}<td>{}<td align=right>{}<td align=right>{}<td align=right>{}<td align=right>{}<td>{}</tr>".format(itm[0], itm[1],
                #                                                                             round(float(itm[2]), 3) if itm[2].replace('.', '', 1).isdigit() else itm[2],
                #                                                                             ('' if 'null' in itm[3] else itm[3]), itm[4], itm[5], itm[6] )
                grp1_spacing = ""
    else:
        msg_body += f"<tr><td colspan={len(columns)}>NO RECORDS</td></tr>"
    msg_body += "</table>"
    print(f"FINAL MESSAGE: {msg_body}")
    return(msg_body)

#msg_body = generate_message_body_report_grouping(result)
#print(msg_body)

def generate_message_body_report_2groupings(raw_string):
    rows = [x for x in result.split('^') if x]
    print(rows)
    for itm in sorted(rows):
        print(itm.split('|')[0] + " -> " + str(itm.split('|')[1:]))
    group1 = {}
    for itm in sorted(rows):
        itm_cols = itm.split('|')
        grp1_itm = itm_cols[0]
        grp2_itm = itm_cols[1]
        print(f"* {grp1_itm} -> {grp2_itm}")
        if grp1_itm in group1:
            for itm2 in group1[grp1_itm]:
                print(f"** {group1[grp1_itm]} / {itm2}")
                itm_index=0
                if grp2_itm in itm2:
                    print(f"---> APPEND grp2: {grp2_itm} => {group1}")
                    group1[grp1_itm][itm_index][grp2_itm].append(itm_cols[2:])
                else:
                    print(f"---> NEW grp2: {grp2_itm} => {group1}")
                    group1[grp1_itm][0] = [{grp2_itm: itm_cols[2:]}]
                itm_index += 1
        else:
            print(f"---> NEW grp1: {grp1_itm} & {grp2_itm} => {group1}")
            group1[grp1_itm] = [{grp2_itm: itm_cols[2:]}]

        #group1[itm_cols[0]] = group1[itm_cols[0]] + [itm_cols[1:]] if itm_cols[0] in group1 else [itm_cols[1:]]
        #group1[grp1_itm] = group1.get(grp1_itm, []) + [itm_cols[1:]]
    print(group1)
    #print(len(group1))
    msg_body = f"<br><br><h3>Report: {get_report_year_month()}</h3>"
    columns = ['TYPE', 'CATEGORY', 'SUB-CATEGORY', 'VAL', 'THRESHOLD', 'MEASURE1', 'MEASURE2', 'MEASURE3']
    msg_body += "<table border=1 cellspacing=0><tr bgcolor='green'><th width=100>TYPE<th width=150>CATEGORY<th>SUB-CATEGORY<th>VAL<th>THRESHOLD<th>MEASURE1<th>MEASURE2<th>MEASURE3</tr>"
    if len(group1) > 0:
        for k,val in group1.items():
            # print(f'key:{k} -> {len(group1[k])}')
            grp1_spacing = f"<td valign=top rowspan={len(group1[k])}>{k}"
            for itm in val:
                #print(f"->{itm}")
                msg_body += "<tr>"+grp1_spacing+ f"<td>{itm[0]}<td>{itm[1]}<td align=right>{round(float(itm[2]), 3) if itm[2].replace('.', '', 1).isdigit() else itm[2]}<td align=right>{('' if 'null' in itm[3] else float(itm[3]) if itm[3].replace('.', '', 1).isdigit() else itm[3])}<td align=right>{itm[4]}<td align=right>{itm[5]}<td>{float(itm[6]):.2f}</tr>"
                #msg_body += "<tr>"+grp1_spacing+ "<td>{}<td>{}<td align=right>{}<td align=right>{}<td align=right>{}<td align=right>{}<td>{}</tr>".format(itm[0], itm[1],
                #                                                                             round(float(itm[2]), 3) if itm[2].replace('.', '', 1).isdigit() else itm[2],
                #                                                                             ('' if 'null' in itm[3] else itm[3]), itm[4], itm[5], itm[6] )
                grp1_spacing = ""
    else:
        msg_body += f"<tr><td colspan={len(columns)}>NO RECORDS</td></tr>"
    msg_body += "</table>"
    #print(f"FINAL MESSAGE: {msg_body}")
    return(msg_body)

msg_body = generate_message_body_report_2groupings(result)
print(msg_body)

#write to HTML file
file_path = "/home/km/km/"
with open("zz_report.html", 'w') as file:
    file.write(msg_body)




