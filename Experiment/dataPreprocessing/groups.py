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
    result=getData('select G_ID,G_Name from Groups')
    dit = {}
    # 通过for循环遍历取出excel表中数据
    for i in range(len(result)):#range(sheet.nrows)读工作表数据
        dit[result[i][0]] = result[i][1]#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，
    #将数据存入Excel
    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("groups")#创建工作表
    #统计
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit)-1)
    # 表头
    sheet1.write(1, 0, "G_ID")
    sheet1.write(1, 1, "G_Name")
    #sheet1.write(1, 2, "TA_Tactic")
    #将字典写入工作表
    r = 2;
    for d in dit:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit[d])
        r += 1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataDuplication/groups.xls")

def groupAssociation():
    result=getData("select * from Groups")
    technique=[]
    software=[]
    for i in range(len(result)):#range(sheet.nrows)
        if result[i][9]!=None and result[i][10]!=None:
            technique.append({
                "Id":result[i][0],
                "Name":result[i][1],
                "TechniqueId":result[i][9][:result[i][9].find("<")],
                "TechniqueName":result[i][10][:result[i][10].find("<")]
            })
        if result[i][12]!=None and result[i][13]!=None:
            software.append({
                "Id":result[i][0],
                "Name":result[i][1],
                "SoftwareId":result[i][12][:result[i][12].find("<")],
                "SoftwareName":result[i][13][:result[i][13].find("<")]
            })

    book1 = xlwt.Workbook()
    sheet1 = book1.add_sheet("Technique")
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(technique)-1)
    sheet1.write(1,0,"G_ID")
    sheet1.write(1,1,"G_Name")
    sheet1.write(1,2,"G_Technique_ID")
    sheet1.write(1,3,"G_Technique_Name")
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

    sheet2 = book1.add_sheet("Software")
    sheet2.write(0, 0, "合计")
    sheet2.write(0, 1, len(software)-1)
    sheet2.write(1,0,"G_ID")
    sheet2.write(1,1,"G_Name")
    sheet2.write(1,2,"G_Software_ID")
    sheet2.write(1,3,"G_Software_Name")
    i=1
    for item in software:
        if i==1:
            i+=1;
            continue
        sheet2.write(i,0,item["Id"])
        sheet2.write(i,1,item["Name"])
        sheet2.write(i,2,item["SoftwareId"])
        sheet2.write(i,3,item["SoftwareName"])
        i+=1
    book1.save("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/groupsAssociation.xls")

def groupAssociationTxt():
    book = xlrd.open_workbook("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/groupsAssociation.xls")
    sheet = book.sheets()[0]  # 获取第一个工作表
    dit1 = {}
    dit2={}
    for r in range(sheet.nrows):
        if r<=1:
            continue
        key1=strutil(sheet.row_values(r)[0])
        if key1 not in dit1.keys():
            dit1[key1]=[]
        value1=strutil(sheet.row_values(r)[2])
        if value1 not in dit1[key1]:
            dit1[key1].append(value1)
        key2=strutil(sheet.row_values(r)[1])
        if key2 not in dit2.keys():
            dit2[key2]=[]
        value2=strutil(sheet.row_values(r)[3])
        if value2 not in dit2[key2]:
            dit2[key2].append(value2)
    with open("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/IdTechnique.txt", "w") as f:
        for key in dit1:
            f.write(key+":"+','.join(str(n) for n in dit1[key])+"\n")
    with open("F:/研究生毕设/experimentalCode/firstIdea/Data/dataAssociation/TechniqueName.txt","w") as f:
        for key in dit2:
            f.write(key+":"+','.join(str(n) for n in dit2[key])+"\n")
def strutil(str):
    return str.replace(" ","").replace("\n","")
if __name__=="__main__":
    #main()
    #groupAssociation()
    groupAssociationTxt()