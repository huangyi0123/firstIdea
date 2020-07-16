import pymysql

def getData(sql):
    test_db = pymysql.connect('211.149.217.34','root','fdsjkl0123','hy')
    cursor = test_db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    test_db.close()
    return result
def strReplace(str):
    return str.replace(" ","").replace("\n","")
def result(sql,txtname):
    data=getData(sql)
    dit={}
    for r in range(len(data)):
        if data[r][0] is None or data[r][1] is None:
            continue
        key=strReplace(data[r][0])
        if key not in dit.keys():
            dit[key]=[]
        value=strReplace(data[r][1])
        value=value[:value.find("<")]
        if value not in dit[key]:
            dit[key].append(value)

    with open(txtname, "w") as f:
        for key in dit:
            f.write(key+":"+', '.join(str(n) for n in dit[key])+"\n")
def ST():
    result("SELECT S_ID,`S_Technique Used ID` FROM Software","../../Data/MITRE_ATTCK/s_t_list.txt")
def GS():
    result("SELECT G_ID,`G_Software ID` FROM Groups","../../Data/MITRE_ATTCK/g_s_list.txt")
def GT():
    result("SELECT G_ID,`G_Technique Used ID` FROM Groups","../../Data/MITRE_ATTCK/g_t_list.txt")
def GG():
    result("SELECT G_ID,`G_Associated Groups` FROM Groups","../../Data/MITRE_ATTCK/g_g_list.txt")
def SS():
    result("SELECT S_ID,`S_Associated Software` FROM Software","../../Data/MITRE_ATTCK/s_s_list.txt")
def MT():
    data1=getData("SELECT M_ID,`M_Techniques Addressed by Mitigation ID` FROM Mitigation_Enterprise")
    data2=getData("SELECT M_ID,`M_Techniques Addressed by Mitigation ID` FROM Mitigation_Mobile")

    dit={}
    for r in range(len(data1)):
        if data1[r][0] is None or data1[r][1] is None:
            continue
        key=strReplace(data1[r][0])
        if key not in dit.keys():
            dit[key]=[]
        value=strReplace(data1[r][1])
        value=value[:value.find("<")]
        if value not in dit[key]:
            dit[key].append(value)

    for r in range(len(data2)):
        if data2[r][0] is None or data2[2][1] is None:
            continue
        key=strReplace(data2[r][0])
        if key not in dit.keys():
            dit[key]=[]
        value=strReplace(data2[r][1])
        value=value[:value.find("<")]
        if value not in dit[key]:
            dit[key].append(value)
    with open("../../Data/MITRE_ATTCK/m_t_list.txt", "w") as f:
        for key in dit:
            f.write(key+":"+', '.join(str(n) for n in dit[key])+"\n")
if __name__ ==  "__main__" :
    MT()
    ST()
    GS()
    GT()
    GG()
    SS()
