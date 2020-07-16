import pymysql
import re
import os
import rake

def getData(sql):
    test_db = pymysql.connect('211.149.217.34','root','fdsjkl0123','hy')
    cursor = test_db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    test_db.close()
    return result
def arrly(list,data):
    flag=False
    for i in range(len(list)):
        if list[i][0]==data[0] and list[i][1]==data[1]:
            flag=True
            break;
    return flag
def replace(str):
    if str is None:
        return ""
    str=re.sub('\\<.*?\\>','',str)
    str=re.sub('\\[.*?\\]','',str)
    return str.replace("\n","").replace("  ","")
def getList(pre,ent,mob):
    list=[]
    for i in range(len(pre)):
        key=replace(pre[i][0])
        value=replace(pre[i][1])
        data=[key,value]
        if not arrly(list,data) and key!="" and value!="":
            list.append(data)

    for i in range(len(ent)):
        key=replace(ent[i][0])
        value=replace(ent[i][1])
        data=[key,value]
        if not arrly(list,data) and key!="" and value!="":
            list.append(data)
    for i in range(len(mob)):
        key=replace(mob[i][0])
        value=replace(mob[i][1])
        data=[key,value]
        if not arrly(list,data) and key!="" and value!="":
            list.append(data)
    return list
def Title():
    pre=getData("SELECT T_ID,T_Title FROM Technique_PRE_ATTCK")
    ent=getData("SELECT T_ID,T_Title FROM Technique_Enterprise")
    mob=getData("SELECT T_ID,T_Title FROM Technique_Mobile")

    list=getList(pre,ent,mob)
    for i in range(len(list)):
        with open("../../Data/Attributed/Technique/Title/"+list[i][0]+".txt", "w",encoding='utf-8') as f:
            f.write(list[i][1])
def Description():
    pre=getData("SELECT T_ID,T_Descripe FROM Technique_PRE_ATTCK")
    ent=getData("SELECT T_ID,T_Descripe FROM Technique_Enterprise")
    mob=getData("SELECT T_ID,T_Descripe FROM Technique_Mobile")
    list=getList(pre,ent,mob)
    for i in range(len(list)):
        with open("../../Data/Attributed/Technique/Description/"+list[i][0]+".txt", "w",encoding='utf-8') as f:
            f.write(list[i][1])
def Procedure():
    pre=getData("SELECT T_ID,`T_Procedure Examples Description` FROM Technique_PRE_ATTCK")
    ent=getData("SELECT T_ID,`T_Procedure Examples Description` FROM Technique_Enterprise")
    mob=getData("SELECT T_ID,`T_Procedure Examples Description` FROM Technique_Mobile")
    list=getList(pre,ent,mob)
    for i in range(len(list)):
        with open("../../Data/Attributed/Technique/Procedure/"+list[i][0]+".txt", "w",encoding='utf-8') as f:
            f.write(list[i][1])
def line(list):
    st=[]
    for i in range(len(list)):
        key=list[i][0]
        value=str(list[i][1])
        st.append(key+","+value)
    return st;
def key():
    stoppath = '../../Data/KeyStoplist/SmartStoplist.txt'

    rake_object = rake.Rake(stoppath, 1, 5, 1)
    dits=['Procedure','Title','Description']
    for j in range(len(dits)):
        files=file("../../Data/Attributed/Technique/"+dits[j]+"/")
        for i in range(len(files)):
            sample_file = open("../../Data/Attributed/Technique/"+dits[j]+"/"+files[i], 'r', encoding="utf-8")
            text = sample_file.read()

            keywords = rake_object.run(text)
            str=line(keywords)
            filename=files[i];
            filename=filename[:filename.find(".")]
            with open("../../Data/Key/Technique/"+dits[j]+"/"+filename+"_key.txt", "w",encoding='utf-8') as f:
                f.write(":".join(str))
def file(path):
    list=[]
    for root, dirs, files in os.walk(path):
        for f in files:
            list.append(f)
    return list
if __name__=="__main__":
    #Title()
    #Description()
    #Procedure()
    key()
    #file("../../Data/Procedure/")