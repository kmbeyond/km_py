from datetime import datetime, timedelta
import os
import re


def get_rpt_month_year():
    now = datetime.now()
    last_month = now.month - 1 if now.month > 1 else 12
    last_month_name = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'][
        last_month - 1]
    year = now.year - 1 if last_month == 12 else now.year
    return str(year) + "-" + last_month_name


print(get_rpt_month_year())

# string data
raw_string = "1.2|1.3|1.5^2.3|2.5|2.6^3.4|3.5|3.9"
raw_string = "PERFORMANCE_METRICS|RECORDS RECEIVED - xx|overall||4444444|^PERFORMANCE_METRICS|RECORDS DELIVERED|cust5||999999999|^PERFORMANCE_METRICS|RECORDS DELIVERED|cust1||10608287|^PERFORMANCE_METRICS|RECORDS RECEIVED - dd|overall||22222222|^SLA_FAILURES|cust1|COL1|COL1_CAT|100^"


def generate_message_body(raw_string):
    msg_body = "\nReport for Month: " + get_rpt_month_year() + "\n"
    rows = raw_string.split('^')
    # rows = re.split('\^', raw_string)
    print(rows)
    rec_recd = sorted([itm for itm in rows if 'RECORDS RECEIVED' in itm])
    print(rec_recd)
    rec_deld = sorted([itm for itm in rows if 'RECORDS DELIVERED' in itm])
    print(rec_deld)
    sla_flrs = sorted([itm for itm in rows if 'SLA_FAILURES' in itm])
    print(sla_flrs)
    msg_body += "\n*** METRICS: Records Received:\n"
    # columns=['METRIC_NAME', 'SUBSCRIBER_NAME', 'RECORDS']
    msg_body += "METRIC_NAME  - RECORDS \n "
    for itm in rec_recd:
        itm_cols = itm.split('|')
        # itm_cols = re.split('\|', itm)
        msg_body += "{}    - {:,} \n ".format(itm_cols[1].replace('RECORDS RECEIVED - ',''), int(itm_cols[4]))

    msg_body += "\n*** METRICS: Records Delivered:\n"
    # msg_body += "   -   ".join(columns) + " \n"
    msg_body += "SUBSCRIBER_NAME  - RECORDS \n "
    for itm in rec_deld:
        itm_cols = itm.split('|')
        msg_body += "{} - {:,} \n ".format(itm_cols[2], int(itm_cols[4]))

    msg_body += "\n*** SLA Failures:\n"
    # columns=['SUBSCRIBER', 'SLA_CATEGORY', 'SLA_SUBCATEGORY','QUANTITY']
    msg_body += "SUBSCRIBER - SLA_CATEGORY     -   SLA_SUBCATEGORY  - QUANTITY \n "
    for itm in sla_flrs:
        itm_cols = itm.split('|')
        msg_body += "{} - {} - {} - {:,} \n ".format(itm_cols[1], itm_cols[2], itm_cols[3], int(itm_cols[4]))

    msg_body += "\n"
    return msg_body


msg_body = generate_message_body(raw_string)
print(msg_body)


# using replace()
#newline_string"""
#"""
#msg_body2 = msg_body.replace('NEWLINE', newline_string)
# print(msg_body2)

# using regexp()
import re
#msg_body3 = re.sub(r"NEWLINE", newline_string, msg_body)
# print(msg_body3)


os.linesep
