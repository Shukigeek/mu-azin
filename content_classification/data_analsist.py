from base64_decode import *
from logger.logger import Logger
logger = Logger.get_logger()


class AnalyzeText:
    def __init__(self,text):
        logger.info("creating two list from giving string ")
        self.vary_hostile = decode(vary_hostile).split(",")
        self.less_hostile = decode(less_hostile).split(",")
        self.text = text
        self.bds_precent = self.check_text()
    def check_text(self):
        count = 0
        score = 0
        logger.info("calculating bds level")
        for hostile in self.vary_hostile:
            hostile_len = len(hostile.split(" "))
            for i in range(len(self.text)):
                if hostile == self.text[i:i+hostile_len]:
                    count += 1
                    score += 2

        for sami_hostile in self.less_hostile:
            sami_hostile_len = len(sami_hostile.split(" "))
            for i in range(len(self.text)):
                if sami_hostile == self.text[i:i + sami_hostile_len]:
                    count += 1
                    score += 1
        score *= (count/len(self.text))
        return score


    def is_bds(self):
        return self.bds_precent > 2

    def bds_threat_level(self):
        if 2 < self.bds_precent > 1:
            threat = "medium"
        elif self.bds_precent > 2:
            threat = "high"
        else:
            threat = "none"
        return threat