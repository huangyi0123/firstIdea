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



def tacticMerge():
    pre=getData('SELECT TA_ID,TA_Name FROM Tactic_PRE_ATTCK')
    ent=getData('SELECT TA_ID,TA_Name FROM Tactic_Enterprise')
    mob=getData('SELECT TA_ID,TA_Name FROM Tactic_Mobile')

    dit_pre={}
    dit_ent={}
    dit_mob={}

    for i in range(len(pre)):#range(sheet.nrows)读工作表数据
        id=pre[i][0]
        name=pre[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_pre[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    for i in range(len(ent)):#range(sheet.nrows)读工作表数据
        id=ent[i][0]
        name=ent[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_ent[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    for i in range(len(mob)):#range(sheet.nrows)读工作表数据
        id=mob[i][0]
        name=mob[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_mob[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("Tactic_Merge")#创建工作表

    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit_mob)+len(dit_ent)+len(dit_pre))
    # 表头
    sheet1.write(1, 0, "TA_ID")
    sheet1.write(1, 1, "TA_Name")
    sheet1.write(1, 2, "DoMain")
    r = 2;

    for d in dit_pre:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_pre[d])
        sheet1.write(r, 2, 'PRE_ATTCK')
        r += 1

    for d in dit_ent:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_ent[d])
        sheet1.write(r, 2, 'Enterprise')
        r += 1

    for d in dit_mob:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_mob[d])
        sheet1.write(r, 2, 'Mobile')
        r += 1

    book1.save("../../Data/dataDuplication/Tactic_Merge.xls")


def mitigationMerge():
    ent=getData('SELECT M_ID,M_Name FROM Mitigation_Enterprise')
    mob=getData('SELECT M_ID,M_Name FROM Mitigation_Mobile')

    dit_ent={}
    dit_mob={}

    for i in range(len(ent)):#range(sheet.nrows)读工作表数据
        id=ent[i][0]
        name=ent[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_ent[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    for i in range(len(mob)):#range(sheet.nrows)读工作表数据
        id=mob[i][0]
        name=mob[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_mob[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("Mitigation_Merge")#创建工作表

    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit_mob)+len(dit_ent))
    # 表头
    sheet1.write(1, 0, "M_ID")
    sheet1.write(1, 1, "M_Name")
    sheet1.write(1, 2, "DoMain")
    r = 2;

    for d in dit_ent:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_ent[d])
        sheet1.write(r, 2, 'Enterprise')
        r += 1

    for d in dit_mob:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_mob[d])
        sheet1.write(r, 2, 'Mobile')
        r += 1

    book1.save("../../Data/dataDuplication/Mitigation_Merge.xls")


def techniqueMerge():
    pre=getData('SELECT T_ID,T_Title FROM Technique_PRE_ATTCK')
    ent=getData('SELECT T_ID,T_Title FROM Technique_Enterprise')
    mob=getData('SELECT T_ID,T_Title FROM Technique_Mobile')

    dit_pre={}
    dit_ent={}
    dit_mob={}

    for i in range(len(pre)):#range(sheet.nrows)读工作表数据
        id=pre[i][0]
        name=pre[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_pre[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    for i in range(len(ent)):#range(sheet.nrows)读工作表数据
        id=ent[i][0]
        name=ent[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_ent[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    for i in range(len(mob)):#range(sheet.nrows)读工作表数据
        id=mob[i][0]
        name=mob[i][1]
        id=id[:id.find('<')].replace(' ','').replace("\n","")
        name=name[:name.find('<')].replace(' ','').replace("\n","")
        dit_mob[id] = name#将工作表的第一列作为key,第二列作为value存入字典，使用字典key唯一性达到去重目的，

    book1 = xlwt.Workbook()#创建excel
    sheet1 = book1.add_sheet("Technique_Merge")#创建工作表

    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(dit_mob)+len(dit_ent)+len(dit_pre))
    # 表头
    sheet1.write(1, 0, "T_ID")
    sheet1.write(1, 1, "T_Name")
    sheet1.write(1, 2, "DoMain")
    r = 2;

    for d in dit_pre:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_pre[d])
        sheet1.write(r, 2, 'PRE_ATTCK')
        r += 1

    for d in dit_ent:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_ent[d])
        sheet1.write(r, 2, 'Enterprise')
        r += 1

    for d in dit_mob:
        sheet1.write(r, 0, d)
        sheet1.write(r, 1, dit_mob[d])
        sheet1.write(r, 2, 'Mobile')
        r += 1

    book1.save("../../Data/dataDuplication/Technique_Merge.xls")


def mitigationAssociation():
    result=getData("select * from Mitigation_Enterprise")
    technique=[]

    for i in range(len(result)):#range(sheet.nrows)
        if result[i][5]!=None and result[i][6]!=None:
            technique.append({
                "Id":result[i][0],
                "Name":result[i][1],
                "HomologousId":result[i][5][:result[i][5].find("<")],
                "HomologousName":result[i][6][:result[i][6].find("<")]
            })

    result1=getData("select * from Mitigation_Mobile")
    technique1 = []

    for i in range(len(result1)):#range(sheet.nrows)
        if result1[i][5]!=None and result1[i][6]!=None:
            technique1.append({
                "Id":result1[i][0],
                "Name":result1[i][1],
                "HomologousId":result1[i][5][:result1[i][5].find("<")],
                "HomologousName":result1[i][6][:result1[i][6].find("<")]
            })

    technique.extend(technique1)
    technique = distinct_list(technique)
    book1 = xlwt.Workbook()
    sheet1 = book1.add_sheet("Technique")
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(technique))
    sheet1.write(1,0,"M_ID")
    sheet1.write(1,1,"M_Name")
    sheet1.write(1,2,"M_Technique_ID")
    sheet1.write(1,3,"M_Technique_Name")
    i=2
    for item in technique:
        sheet1.write(i,0,item["Id"])
        sheet1.write(i,1,item["Name"])
        sheet1.write(i,2,item["HomologousId"])
        sheet1.write(i,3,item["HomologousName"])
        i+=1



    book1.save("../../Data/dataAssociation/Mitigation_Association.xls")


def distinct_list(datas):
    data_list = []
    data_list.append(datas[0])
    for dict in datas:
        k = 0
        for item in data_list:
            if dict['Id'] == item['Id'] and dict['Name'] == item['Name'] and dict['HomologousId'] == item['HomologousId'] and dict['HomologousName'] == item['HomologousName']:
                break
            else:
                k = k + 1
            if k == len(data_list):
                data_list.append(dict)
    return  data_list


def techniqueAssociation():
    result=getData("select * from Tactic_Enterprise")
    technique=[]

    for i in range(len(result)):#range(sheet.nrows)
        if result[i][0]!=None and result[i][1]!=None:
            technique.append({
                "Id": result[i][3][:result[i][3].find("<")].replace("  ",""),
                "Name": result[i][4][:result[i][4].find("<")].replace("  ",""),
                "HomologousId": result[i][0][:result[i][0].find("<")][:result[i][0].find("<")].replace("  ",""),
                "HomologousName": result[i][1][:result[i][1].find("<")][:result[i][1].find("<")].replace("  ","")
            })

    result1=getData("select * from Tactic_Mobile")
    technique1 = []

    for i in range(len(result1)):#range(sheet.nrows)
        if result1[i][0]!=None and result1[i][1]!=None:
            technique1.append({
                "Id":result1[i][3][:result[i][3].find("<")].replace("  ",""),
                "Name":result1[i][4][:result[i][4].find("<")].replace("  ",""),
                "HomologousId":result1[i][0][:result1[i][0].find("<")][:result[i][0].find("<")].replace("  ",""),
                "HomologousName":result1[i][1][:result1[i][1].find("<")][:result[i][1].find("<")].replace("  ","")
            })

    result2 = getData("select * from Tactic_PRE_ATTCK")
    technique2 = []

    for i in range(len(result2)):  # range(sheet.nrows)
        if result2[i][0] != None and result2[i][1] != None:
            technique2.append({
                "Id": result2[i][3][:result[i][3].find("<")].replace("  ",""),
                "Name": result2[i][4][:result[i][4].find("<")].replace("  ",""),
                "HomologousId": result2[i][0][:result2[i][0].find("<")][:result[i][0].find("<")].replace("  ",""),
                "HomologousName": result2[i][1][:result2[i][1].find("<")][:result[i][1].find("<")].replace("  ","")
            })

    technique.extend(technique1)
    technique.extend(technique2)
    technique = distinct_list(technique)
    book1 = xlwt.Workbook()
    sheet1 = book1.add_sheet("Technique")
    sheet1.write(0, 0, "合计")
    sheet1.write(0, 1, len(technique))
    sheet1.write(1,0,"M_ID")
    sheet1.write(1,1,"M_Name")
    sheet1.write(1,2,"M_Technique_ID")
    sheet1.write(1,3,"M_Technique_Name")
    i=2
    for item in technique:
        sheet1.write(i,0,item["Id"])
        sheet1.write(i,1,item["Name"])
        sheet1.write(i,2,item["HomologousId"])
        sheet1.write(i,3,item["HomologousName"])
        i+=1



    book1.save("../../Data/dataAssociation/technique_Association.xls")


# def distinct_list(datas):
#     data_list = []
#     data_list.append(datas[0])
#     for dict in datas:
#         k = 0
#         for item in data_list:
#             if dict['Id'] == item['Id'] and dict['Name'] == item['Name'] and dict['HomologousId'] == item['HomologousId'] and dict['HomologousName'] == item['HomologousName']:
#                 break
#             else:
#                 k = k + 1
#             if k == len(data_list):
#                 data_list.append(dict)
#     return  data_list

if __name__ ==  "__main__" :
    tacticMerge()
    mitigationMerge()
    techniqueMerge()
    mitigationAssociation()
    techniqueAssociation()
