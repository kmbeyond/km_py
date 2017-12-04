# -*- coding: utf-8 -*-
"""
Created on Wed Nov  10 09:14:46 2017

@author: Kiran
"""
#Requirements:
#--install pymysql (MySQLdb for Python 2.x)
#

#import MySQLdb #This is for Python 2.x
import pymysql
#from collections import OrderedDict

class ProductsMfgModel:

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
            return cursor.fetchone()[0]
        else:
            return None

    def addRow(cursor, tablename, rowdict):
        #Inserts new record in given table
        #column names & values in Dictionary
        lstCols=set(rowdict)
        #print("Columns: {}".format(lstCols))
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
        #updates a column of given table (tablename.columnName = columnValue)
        #Columns filter in Dictionary
        lstCols=set(rowdict)
        print("Columns: {}".format(lstCols))
        #columnsList = ", ".join(lstCols)
        sConditions=""
        for key in lstCols:
            sConditions = sConditions + key + '=%s AND '
        sConditions = sConditions[:-5]

        sql = "update %s set %s=%s where (%s)" % (
                tablename, columnName, (columnValue if columnValueType=='Expr' else "'"+columnValue+"'"), sConditions)
        print("SQL***** {}".format(sql))

        values = tuple(rowdict[key] for key in lstCols)
        print("values***** {}".format(values))
        #try:
        cursor.execute(sql, values)
        return cursor.lastrowid
        #except Exception as e:
            #print("Exception in updateRec:"+ str(e))
            #return None


    @classmethod
    def addToInventory(self, prd):

        conn = pymysql.connect(host="localhost",  # your host
                             user="root",       # username
                             passwd="Iamroo@9090",     # password
                             db="mycompany")   # name of the database

        # Create a Cursor object to execute queries.
        cur = conn.cursor()

        #prd={ "product_cd": "1006",
        #	"qty": "5",
        #	"mfg_dt": "11/11/2017",
        #	"mfg_unit_cd": "MU-DT-001",
        #	"machine_cd": "SCR-001",
        #   "warehouse_cd": "Warehouse"
        #}

        #Check if Warehouse exists
        sWHId = self.getID(cur, "T_WAREHOUSE", { "WH_CODE": prd["warehouse_cd"] })
        if sWHId:
            print("WH Id: {}".format(sWHId))
        else:
            #print("WH NOT found.")
            return {"Error": "Warehouse is not valid"}

        #Check if Product exists
        sProdId = self.getID(cur, "T_PRODUCTS", { "UPC_CD": prd["product_cd"] })
        if sProdId:
            print("ProdId: {}".format(sProdId))

            #Get Mfg Unit Id
            sMfgUnitId = self.getID(cur, "T_MFG_UNIT", {"MFG_UNIT_CD": prd["mfg_unit_cd"]})
            if sMfgUnitId:
                print("ManufUnitId: {}".format(sMfgUnitId))

                #Get Mfg Machine ID
                sMachineId = self.getID(cur, "T_MFG_MACHINE", {"MACHINE_CD": prd["machine_cd"]})
                if sMachineId:
                    print("Manuf MachineId: {}".format(sMachineId))

                    #Get T_INVT_DTL_SRC ID (Create if not exists)
                    sInvDtlSrcId = self.getID(cur, "T_INVT_DTL_SRC", {"MACHINE_ID": sMachineId, "MFG_UNIT_ID": sMfgUnitId})

                    conn.autocommit(False)
                    try:
                        if sInvDtlSrcId == None:
                            print("Invt Source record Id NOT found")
                            #insert a new RecordId
                            sInvDtlSrcId = self.addRow(cur, "T_INVT_DTL_SRC", {"TYPE": "Factory", "MACHINE_ID": sMachineId, "MFG_UNIT_ID": sMfgUnitId})
                            print("Invt Source record Id added: {}".format(sInvDtlSrcId))
                        if sInvDtlSrcId == None:
                            print("Error: DB exception")
                            return {"Success": "Error: DB exception"}

                        #create/update S_INVT
                        #Check if inventory rec exists
                        sInvtId = self.getID(cur, "T_INVT", {"PROD_ID": sProdId, "WH_ID": sWHId})
                        print("Invt record Id: {}".format(sInvtId))
                        if sInvtId:
                            self.updateSingleColRec(cur, "T_INVT", "QTY", "QTY+"+str(prd["qty"]), "Expr", {"ID": sInvtId})
                            print("updated existing record.")
                        else:
                            sInvtId = addRow(cur, "T_INVT", {"PROD_ID": sProdId, "WH_ID": sWHId, "QTY": prd["qty"]})
                            print("New Inv record created; Id: {}".format(sInvtId))

                        #insert record in S_INVT_DTL
                        sInvtDtlId = self.addRow(cur, "T_INVT_DTL", {"INVT_ID": sInvtId, "QTY": prd["qty"], "OPERATION": "IN-STK-MFG", "SRC_ID": sInvDtlSrcId})
                        print("Invt Dtl record Id: {}".format(sInvtDtlId))

                        #Commit if all success
                        conn.commit()
                    except Exception as e:
                        print("Exception in transaction:"+ str(e))
                        conn.rollback()
                        return {"Success": "Not created"}
                else:
                    print("Manuf Machine NOT found")
                    return {"Success": "Error: DB exception"}
            else:
                print("Manuf Unit NOT found")
                return {"Success": "Error: DB exception"}
        else:
            print("Product NOT found")
            return {"Success": "Error: DB exception"}


        cur.close()
        conn.close()
        return {"Success": "Y"}
