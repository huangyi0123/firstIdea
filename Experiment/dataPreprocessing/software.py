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
    result=getData('select S_ID,S_Name from Software')
    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):#range(sheet.nrows)读工作表数据
        dit[result[i][0]] = result[i][1]#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，
    #将数据存入Excel
    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("software")#创建工作表
    #统计
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit)-1)
    # 表头
    sheet1.write(1, 0, "S_ID")
    sheet1.write(1, 1, "S_Name")
    #将字典写入工作表
    r = 2;
    for d in dit:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit[d])
        r += 1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataDuplication/softwarelew.xls")

def softwareAssociation():
    result=getData("select * from Software")
    technique=[]
    group=[]
    for i in range(len(result)):#range(sheet.nrows)
        if result[i][7]!=None and result[i][8]!=None:
            technique.append({
                "Id":result[i][0],
                "Name":result[i][1],
                "TechniqueId":result[i][7][:result[i][7].find("<")],
                "TechniqueName":result[i][8][:result[i][8].find("<")]
            })
        if result[i][10]!=None and result[i][11]!=None:
            group.append({
                "Id":result[i][0],
                "Name":result[i][1],
                "GroupsId":result[i][10][:result[i][10].find("<")],
                "GroupsName":result[i][11][:result[i][11].find("<")]
            })

    book1 = xlwt.Workbook()
    sheet1 = book1.add_sheet("Technique")
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(technique)-1)
    sheet1.write(1,0,"S_ID")
    sheet1.write(1,1,"S_Name")
    sheet1.write(1,2,"S_Technique_ID")
    sheet1.write(1,3,"S_Technique_Name")
    i=1
    for item in technique:
        if i==1:
            i+=1;
            continue
        sheet1.write(i,0,item["Id"])
        sheet1.write(i,1,item["Name"])
        sheet1.write(i,2,item["TechniqueId"])
        sheet1.write(i,3,item["TechniqueName"])
        i+=1

    sheet2 = book1.add_sheet("Groups")
    sheet2.write(0, 0, "合计")
    sheet2.write(0, 1, len(group)-1)
    sheet2.write(1,0,"S_ID")
    sheet2.write(1,1,"S_Name")
    sheet2.write(1,2,"S_Groups_ID")
    sheet2.write(1,3,"S_Groups_Name")
    i=1
    for item in group:
        if i==1:
            i+=1;
            continue
        sheet2.write(i,0,item["Id"])
        sheet2.write(i,1,item["Name"])
        sheet2.write(i,2,item["GroupsId"])
        sheet2.write(i,3,item["GroupsName"])
        i+=1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/softwareAssociation.xls")

def softwareAssociationTxt():
    book = xlrd.open_workbook("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/softwareAssociation.xls")
    sheet = book.sheets()[0]  # 获取第一个工作表
    dit1 = {}
    dit2={}
    for r in range(sheet.nrows):
        if r<=1:
            continue
        key1=strReplace(sheet.row_values(r)[0])
        if key1 not in dit1.keys():
            dit1[key1]=[]
        value1=strReplace(sheet.row_values(r)[2])
        if value1 not in dit1[key1]:
            dit1[key1].append(value1)
        key2=strReplace(sheet.row_values(r)[1])
        if key2 not in dit2.keys():
            dit2[key2]=[]
        value2=strReplace(sheet.row_values(r)[3])
        if value2 not in dit2[key2]:
            dit2[key2].append(value2)
    with open("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/S_T_ID.txt", "w", encoding="utf-8") as f:
        for key in dit1:
            f.write(key+":"+', '.join(str(n) for n in dit1[key])+"\n")
    with open("F:/研究生毕设/experimentalCode/firstIdea/Data/DataAssociation/S_G_Name.txt","w", encoding="utf-8") as f:
        for key in dit2:
            f.write(key+":"+', '.join(str(n) for n in dit2[key])+"\n", )

def strReplace(str):
    return str.replace(" ","").replace("\n","")


if __name__=="__main__":
    main()
    softwareAssociation()
    softwareAssociationTxt()