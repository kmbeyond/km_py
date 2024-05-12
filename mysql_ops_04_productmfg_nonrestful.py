
#Requirements:
#--install pymysql (MySQLdb for Python 2.x)


#-----get database config from config script
import mysql_ops_config as mysqlconf

import pymysql
conn2 = pymysql.connect(host = mysqlconf.mysql_host,
                        user = mysqlconf.mysql_user, passwd = mysqlconf.mysql_passwd,
                        db = mysqlconf.mysql_db)
cursor = conn2.cursor()


def getID(cursor, tablename, rowdict):
    #Returns ID column from given table
    #Columns filter in Dictionary
    lstCols=set(rowdict)

    columnsList = ", ".join(lstCols)

    sConditions=""
    for key in lstCols:
        sConditions = sConditions + key + '=%s AND '
    sConditions = sConditions[:-5]

    sql = "SELECT ID FROM %s where %s" % (
            tablename, sConditions)
    print("SQL***** {}".format(sql))
    values = tuple(rowdict[key] for key in lstCols)
    print("values***** {}".format(values))
    rows = cursor.execute(sql, values)
    if rows>=1:
        return cur.fetchone()[0]
    else:
        return None

def addRow(cursor, tablename, rowdict):
    #Inserts new record in given table
    #column names & values in Dictionary
    lstCols=set(rowdict)
    #print("Columns: {}".format(keys))
    columns = ", ".join(lstCols)
    #print("Columns: {}".format(columns))
    values_template = ", ".join(["%s"] * len(lstCols))
    #print("Values_template: {}".format(values_template))

    sql = "insert into %s (%s) values (%s)" % (
            tablename, columns, values_template)
    print("SQL***** {}".format(sql))

    values = tuple(rowdict[key] for key in lstCols)
    print("values***** {}".format(values))
    try:
        cursor.execute(sql, values)
        return cursor.lastrowid
    except Exception as e:
        print("Exception in addRow:"+ str(e))
        return None

def updateSingleColRec(cursor, tablename, columnName, columnValue, columnValueType, rowdict):
    #updates a column of given table
    #Columns filter in Dictionary
    lstCols=set(rowdict)

    columnsList = ", ".join(lstCols)
    sConditions=""
    for key in lstCols:
        sConditions = sConditions + key + '=%s AND '
    sConditions = sConditions[:-5]

    sql = "update %s set %s=%s where (%s)" % (
            tablename, columnName, (columnValue if columnValueType=='Expr' else "'"+columnValue+"'"), sConditions)
    print("SQL***** {}".format(sql))

    values = tuple(rowdict[key] for key in lstCols)
    print("values***** {}".format(values))
    try:
        cursor.execute(sql, values)
        return cursor.lastrowid
    except Exception as e:
        print("Exception in updateRec:"+ str(e))
        return None



conn = pymysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="Iamroo@9090",     # password
                     db="mycompany")   # name of the database

# Create a Cursor object to execute queries.
cur = conn.cursor()

prd={ "product_cd": "1006",
	"qty": "5",
	"mfg_dt": "11/11/2017",
	"mfg_unit_cd": "MU-DT-001",
	"machine_cd": "SCR-001",
    "warehouse_cd": "Warehouse"
}
#Check if Warehouse exists
sWHId = getID(cur, "T_WAREHOUSE", { "WH_CODE": prd["warehouse_cd"] })
if sWHId:
    print("WH Id: {}".format(sWHId))
else:
    print("WH NOT found.")
    #return "Error: Warehouse is not valid"

#Check if Product exists
sProdId = getID(cur, "T_PRODUCTS", { "UPC_CD": prd["product_cd"] })
if sProdId:
    print("ProdId: {}".format(sProdId))

    #Get Mfg Unit Id
    sMfgUnitId = getID(cur, "T_MFG_UNIT", {"MFG_UNIT_CD": prd["mfg_unit_cd"]})
    if sMfgUnitId:
        print("ManufUnitId: {}".format(sMfgUnitId))

        #Get Mfg Machine ID
        sMachineId = getID(cur, "T_MFG_MACHINE", {"MACHINE_CD": prd["machine_cd"]})
        if sMachineId:
            print("Manuf MachineId: {}".format(sMachineId))

            #Get T_INVT_DTL_SRC ID (Create if not exists)
            sInvDtlSrcId = getID(cur, "T_INVT_DTL_SRC", {"MACHINE_ID": sMachineId, "MFG_UNIT_ID": sMfgUnitId})

            conn.autocommit(False)
            try:
                if sInvDtlSrcId == None:
                    print("Invt Source record Id NOT found")
                    #insert a new RecordId
                    sInvDtlSrcId = addRow(cur, "T_INVT_DTL_SRC", {"TYPE": "Factory", "MACHINE_ID": sMachineId, "MFG_UNIT_ID": sMfgUnitId})
                    print("Invt Source record Id added: {}".format(sInvDtlSrcId))
                if sInvDtlSrcId == None:
                    print("Error: DB exception")
                    #return "Error"

                #create/update S_INVT
                #Check if inventory rec exists
                sInvtId = getID(cur, "T_INVT", {"PROD_ID": sProdId, "WH_ID": sWHId})
                print("Invt record Id: {}".format(sInvtId))
                if sInvtId:
                    updateSingleColRec(cur, "T_INVT", "QTY", "QTY+"+prd["qty"], "Expr", {"ID": sInvtId})
                    print("updated existing record.")
                else:
                    sInvtId = addRow(cur, "T_INVT", {"PROD_ID": sProdId, "WH_ID": sWHId, "QTY": prd["qty"]})
                    print("New Inv record created; Id: {}".format(sInvtId))

                #insert record in S_INVT_DTL
                sInvtDtlId = addRow(cur, "T_INVT_DTL", {"INVT_ID": sInvtId, "QTY": prd["qty"], "OPERATION": "IN-STK-MFG", "SRC_ID": sInvDtlSrcId})
                print("Invt Dtl record Id: {}".format(sInvtDtlId))

                #Commit if all success
                #conn.commit()
            except:
                conn.rollback()
        else:
            print("Manuf Machine NOT found")

    else:
        print("Manuf Unit NOT found")
else:
    print("Product NOT found")



cur.close()
conn.close()
