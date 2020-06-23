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
    result=getData('select T_ID,T_Title from Technique_Enterprise')
    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):#range(sheet.nrows)读工作表数据
        dit[result[i][0]] = result[i][1]#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，
    #将数据存入Excel
    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("Technique_Enterprise")#创建工作表
    #统计
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit))
    # 表头
    sheet1.write(1, 0, "T_ID")
    sheet1.write(1, 1, "T_Name")
    #sheet1.write(1, 2, "TA_Tactic")
    #将字典写入工作表
    r = 2;
    for d in dit:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit[d])
        r += 1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataDuplication/Technique_Enterprise.xls")


def techniqueEnterpriseAssociation():
    result = getData('SELECT T_ID,T_Title,T_Tactic FROM Technique_Enterprise')

    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):  # range(sheet.nrows)读工作表数据
        dit[result[i][0]] = {
            "title": result[i][1],
            "tactic": result[i][2]
        }  # 将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    book1 = xlwt.Workbook()  # 创建excel
    sheet1 = book1.add_sheet("TechniqueEnterprise_Association")  # 创建工作表
    # 统计
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit))
    #表头
    sheet1.write(1,0,"T_ID")
    sheet1.write(1,1,"T_Name")
    sheet1.write(1,2,"TA_Tactic")
    # 将字典写入工作表
    r = 2
    for d in dit:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit[d]["title"])
        sheet1.write(r, 2, dit[d]["tactic"].replace(" ", "").replace(",", ""))
        r += 1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/TechniqueEnterprise_Association.xls")

def techniqueEnterpriseAssociationTxt():
    book = xlrd.open_workbook("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/TechniqueEnterprise_Association.xls")
    sheet = book.sheets()[0]  # 获取第一个工作表
    dit1 = {}
    #dit2={}
    for r in range(sheet.nrows):
        if r<=1:
            continue
        key1=strReplace(sheet.row_values(r)[0])
        if key1 not in dit1.keys():
            dit1[key1]=[]
        value1=strReplace(sheet.row_values(r)[2])
        if value1 not in dit1[key1]:
            dit1[key1].append(value1)
        # key2=strReplace(sheet.row_values(r)[1])
        # if key2 not in dit2.keys():
        #     dit2[key2]=[]
        # value2=strReplace(sheet.row_values(r)[3])
        # if value2 not in dit2[key2]:
        #     dit2[key2].append(value2)
    with open("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/M_T_M_ID.txt", "w") as f:
        for key in dit1:
            f.write(key+":"+', '.join(str(n) for n in dit1[key])+"\n")
    # with open("F:/研究生毕设/experimentalCode/firstIdea/Data/DataAssociation/G_T_Name.txt","w") as f:
    #     for key in dit2:
    #         f.write(key+":"+', '.join(str(n) for n in dit2[key])+"\n")

def strReplace(str):
    return str.replace(" ","").replace("\n","")


if __name__=="__main__":
    main()
    techniqueEnterpriseAssociation()