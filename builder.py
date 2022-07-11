class Storage:
    def __init__(self):

        self.sagnir_file = "sagnir.txt"

        # veikar sagnir flokkar
        self.vf1 = {}
        self.vf2 = {}
        self.vf3 = {}

        # sterkar sagnir flokkar
        self.sf1 = {}
        self.sf2 = {}
        self.sf3 = {}
        self.sf4 = {}
        self.sf5 = {}
        self.sf6 = {}
        self.sf7 = {}

        self.group_list = [self.vf1, self.vf2, self.vf3, self.sf1, self.sf2, 
                           self.sf3, self.sf4, self.sf5, self.sf6, self.sf7]

    def choose_flokkur(self, code: str) -> dict:
        if code == "vf1":
            return self.vf1
        elif code == "vf2":
            return self.vf2
        elif code == "vf3":
            return self.vf3
        elif code == "sf1":
            return self.sf1
        elif code == "sf2":
            return self.sf2
        elif code == "sf3":
            return self.sf3
        elif code == "sf4":
            return self.sf4
        elif code == "sf5":
            return self.sf5
        elif code == "sf6":
            return self.sf6
        elif code == "sf7":
            return self.sf7

    def parse(self):
        '''
        takes in the sagnir.txt file and builds the group ('flokkur') data
        structures from it

        throws: raises an error if a line doesn't have 14 elements (i.e. 
                something is missing from the conjugation info)
        '''
        with open(self.sagnir_file, "r") as sagnir_file:
            for line in sagnir_file:
                split_line = line.split(", ")
                # determines the group the verb is in
                flokkur = self.choose_flokkur(split_line[0])
                # create verb in appropriate dict and fill nútið and þátíð
                flokkur[split_line[1]] = [[split_line[2], split_line[3],
                                           split_line[4], split_line[5], 
                                           split_line[6], split_line[7]], 
                                          [split_line[8], split_line[9], 
                                           split_line[10], split_line[11], 
                                           split_line[12], split_line[13]]]
    
