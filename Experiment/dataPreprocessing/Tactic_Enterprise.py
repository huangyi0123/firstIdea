import xlwt
import xlrd
import pymysql

def getData(sql):
    test_db = pymysql.connect('211.149.217.34','root','fdsjkl0123','hy')
    cursor = test_db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    test_db.close()
    return result

def main():
    result=getData('select TA_ID,TA_Name from Tactic_Enterprise')
    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):  # range(sheet.nrows)读工作表数据
        id = result[i][0]
        name = result[i][1]
        id = id[:id.find('<')].replace(' ', '').replace("\n", "")
        name = name[:name.find('<')].replace(' ', '').replace("\n", "")
        dit[id] = name  # 将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    #将数据存入Excel
    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("Tactic_Enterprise")#创建工作表
    #统计
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit))
    # 表头
    sheet1.write(1, 0, "TA_ID")
    sheet1.write(1, 1, "TA_Name")
    #sheet1.write(1, 2, "TA_Tactic")
    #将字典写入工作表
    r = 2;
    for d in dit:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit[d])
        r += 1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataDuplication/Tactic_Enterprise.xls")


def techniqueTacticEnterpriseAssociation():
    result=getData("select * from Tactic_Enterprise")
    technique=[]

    for i in range(len(result)):#range(sheet.nrows)
        if result[i][3]!=None and result[i][4]!=None:
            technique.append({
                "Id":result[i][3][:result[i][3].find("<")].replace("  ",""),
                "Name":result[i][4][:result[i][4].find("<")].replace("  ",""),
                "HomologousId":result[i][0][:result[i][0].find("<")].replace("  ",""),
                "HomologousName":result[i][1][:result[i][1].find("<")].replace("  ","")
            })


    book1 = xlwt.Workbook()
    sheet1 = book1.add_sheet("Technique")
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(technique))
    sheet1.write(1,0,"T_ID")
    sheet1.write(1,1,"T_Name")
    sheet1.write(1,2,"T_Tactic_ID")
    sheet1.write(1,3,"T_Tactic_Name")
    i=1
    for item in technique:
        if i==1:
            i+=1;
            continue
        sheet1.write(i,0,item["Id"])
        sheet1.write(i,1,item["Name"])
        sheet1.write(i,2,item["HomologousId"])
        sheet1.write(i,3,item["HomologousName"])
        i+=1

    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/techniqueTacticEnterpriseAssociation.xls")


if __name__=="__main__":
    main()
    techniqueTacticEnterpriseAssociation()