import random
#定义变量
class MetaPathGenerator:
    def __init__(self):
        self.id_group = dict()
        self.id_software = dict()
        self.id_mitigation=dict()
        self.id_technique=dict()

        self.group_software=dict()
        self.software_technique=dict()
        self.technique_mitigation=dict()
        self.mitigation_technique=dict()
        self.technique_software=dict()
        self.software_group=dict()

        self.group_softwarelist=dict()
        self.software_techniquelist=dict()
        self.technique_mitigationlist=dict()
        self.mitigation_techniquelist=dict()
        self.technique_softwarelist=dict()
        self.software_grouplist=dict()

    def read_data(self, dirpath):
        #处理group
        with open(dirpath + "/G.txt", encoding="utf-8") as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_group[toks[0]] = toks[1].replace(" ", "")
        #处理software
        with open(dirpath + "/S.txt", encoding="utf-8") as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_software[toks[0]] = toks[1].replace(" ", "")
        #处理mitigation
        with open(dirpath + "/M.txt", encoding="utf-8") as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_mitigation[toks[0]] = toks[1].replace(" ", "")
        #处理mitigation
        with open(dirpath + "/T.txt", encoding="utf-8") as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_technique[toks[0]] = toks[1].replace(" ", "")

        #处理group、software
        with open(dirpath + "/GS.txt", encoding="utf-8") as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    p, a = toks[0], toks[1]
                    if p not in self.group_software:
                        self.group_software[p] = []
                    self.group_software[p].append(a)
                    if a not in self.software_group:
                        self.software_group[a] = []
                    self.software_group[a].append(p)

         #处理software、technique
        with open(dirpath + "/ST.txt", encoding="utf-8") as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    p, a = toks[0], toks[1]
                    if p not in self.software_technique:
                        self.software_technique[p] = []
                    self.software_technique[p].append(a)
                    if a not in self.technique_software:
                        self.technique_software[a] = []
                    self.technique_software[a].append(p)
        #处理technique、mitigation
        with open(dirpath + "/TM.txt", encoding="utf-8") as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    p, a = toks[0], toks[1]
                    if p not in self.technique_mitigation:
                        self.technique_mitigation[p] = []
                    self.technique_mitigation[p].append(a)
                    if a not in self.mitigation_technique:
                        self.mitigation_technique[a] = []
                    self.mitigation_technique[a].append(p)


    def generate_random_aca(self, outfilename, numwalks, walklength):
        outfile = open(outfilename, 'w+', encoding="utf-8")
        for group in self.group_software:
            for i in range(0,numwalks):
                outline=self.id_group[group]
                for j in range(0,walklength):
                    softs=self.group_software[group]
                    numa=len(softs)
                    if numa==0:
                        continue
                    softid=random.randrange(numa)
                    soft=softs[softid]
                    if soft not in self.id_software:
                        continue;
                    outline+=" "+self.id_software[soft]

                    if soft not in self.software_technique:
                        continue
                    techniques=self.software_technique[soft]
                    numa=len(techniques)
                    if numa==0:
                        continue
                    techniqueid=random.randrange(numa)
                    technique=techniques[techniqueid]
                    outline+=" "+self.id_technique[technique]

                    if technique not in self.technique_mitigation:
                        continue
                    mitigations=self.technique_mitigation[technique]
                    numa=len(mitigations)
                    if numa==0:
                        continue
                    mitigationid=random.randrange(numa)
                    mitigation=mitigations[mitigationid]
                    outline+=" "+self.id_mitigation[mitigation]

                    if mitigation not in self.mitigation_technique:
                        continue
                    techniques1=self.mitigation_technique[mitigation]
                    if technique in techniques1:
                        techniques1.remove(technique)
                    numa=len(techniques1)
                    if numa==0:
                        continue
                    techniqueid1=random.randrange(numa)
                    technique1=techniques1[techniqueid1]
                    outline+=" "+self.id_technique[technique1]

                    if technique1 not in self.technique_software:
                        continue
                    softs1=self.technique_software[technique1]
                    if soft in softs1:
                        softs1.remove(soft)
                    numa=len(softs1)
                    if numa==0:
                        continue
                    softid1=random.randrange(numa)
                    soft1=softs1[softid1]
                    outline+=" "+self.id_software[soft1]

                    if soft1 not in self.software_group:
                        continue
                    groups1=self.software_group[soft1]
                    if group in groups1:
                        groups1.remove(group)
                    numa=len(groups1)
                    if numa==0:
                        continue
                    groupid1=random.randrange(numa)
                    group1=groups1[groupid1]
                    outline+=' '+self.id_group[group1]
                outfile.write(outline + "\n")
        outfile.close()
dirpath = 'data'
outfilename = 'data/output.txt'
numwalks = 100
walklength = 100
def main():
    mpg = MetaPathGenerator()
    mpg.read_data(dirpath)
    mpg.generate_random_aca(outfilename,numwalks,walklength)
if __name__ == "__main__":
    main()