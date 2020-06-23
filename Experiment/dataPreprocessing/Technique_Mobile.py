import xlwt
import pymysql

def getData(sql):
    test_db = pymysql.connect('211.149.217.34','root','fdsjkl0123','hy')
    cursor = test_db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    test_db.close()
    return result
def main():
    result=getData('select T_ID,T_Title from Technique_Mobile')
    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):#range(sheet.nrows)读工作表数据
        dit[result[i][0]] = result[i][1]#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，
    #将数据存入Excel
    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("Technique_Mobile")#创建工作表
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
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataDuplication/Technique_Mobile.xls")

# def mitigationMobileAssociation():
#     result=getData("select * from Mitigation_Mobile")
#     technique=[]
#
#     for i in range(len(result)):#range(sheet.nrows)
#         if result[i][5]!=None and result[i][6]!=None:
#             technique.append({
#                 "Id":result[i][0],
#                 "Name":result[i][1],
#                 "TechniqueId":result[i][5][:result[i][5].find("<")],
#                 "TechniqueName":result[i][6][:result[i][6].find("<")]
#             })
#
#
#     book1 = xlwt.Workbook()
#     sheet1 = book1.add_sheet("Technique")
#     sheet1.write(0, 0, "合计")
#     sheet1.write(0, 1, len(technique)-1)
#     sheet1.write(1,0,"M_ID")
#     sheet1.write(1,1,"M_Name")
#     sheet1.write(1,2,"M_Technique_ID")
#     sheet1.write(1,3,"M_Technique_Name")
#     i=1
#     for item in technique:
#         if i==1:
#             i+=1;
#             continue
#         sheet1.write(i,0,item["Id"])
#         sheet1.write(i,1,item["Name"])
#         sheet1.write(i,2,item["TechniqueId"])
#         sheet1.write(i,3,item["TechniqueName"])
#         i+=1
#
#
#
#     book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/Mitigation_Mobile_Association.xls")

def techniqueMobileAssociation():
    result = getData('SELECT T_ID,T_Title,T_Tactic FROM Technique_Mobile')

    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):  # range(sheet.nrows)读工作表数据
        dit[result[i][0]] = {
            "title": result[i][1],
            "tactic": result[i][2]
        }  # 将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    book1 = xlwt.Workbook()  # 创建excel
    sheet1 = book1.add_sheet("TechniqueMobile_Association")  # 创建工作表
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
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/TechniqueMobile_Association.xls")


if __name__=="__main__":
    main()
    techniqueMobileAssociation()