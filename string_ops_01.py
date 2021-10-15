
'''
1.Read string, split & format
2.

'''

#string data
result="1.2|1.3|1.5|1.336565|1.26|1.28|1.45|1.56^2.3|2.5|2.6|2.1355435|null|2.43|2.55|2.56^3.4|3.5|3.9|3.14|3.27|3.25|3.34|3.42^"
#result=""

replace_chars = "[(',)]"
for ch in replace_chars:
    result = result.replace(ch, '')

def generate_message_body(raw_string):
    rows = [x for x in result.split('^') if x]
    print(rows)
    msg_body = "\n"
    msg_body += "\n\nHEADERS\n"
    if len(rows)>0:
        for itm in sorted(rows):
            itm_cols = itm.split('|')
            msg_body += "{},{},{}, *{}*,{},{},{},{} \n".format(itm_cols[0], itm_cols[1], itm_cols[2], round(float(itm_cols[3]), 3) if itm_cols[3].replace('.', '', 1).isdigit() else itm_cols[3],
                                                    itm_cols[4], itm_cols[5], itm_cols[6], itm_cols[7])
        msg_body += "\n"
    else:
        msg_body = "NONE"
    print(f"FINAL MESSAGE: {msg_body}")
    return(msg_body)

#'' if 'null' in itm_cols[4] else itm_cols[4]

#    print("{},{},{},{},{},{},{},{} \n".format(itm_cols[0], itm_cols[1], itm_cols[2], round(float(itm_cols[3]),3) if itm_cols[3].replace('.','',1).isdigit() else itm_cols[3],
#                                              itm_cols[4], itm_cols[5],  itm_cols[6], itm_cols[7]))

generate_message_body(result)