from content_classification.base64_decode import *
import os
from services.logger.logger import Logger

logger = Logger.get_logger(index="analysis-logs")


class AnalyzeText:
    def __init__(self, text):
        logger.info("creating two list from giving string ")
        self.vary_hostile = decode(vary_hostile).split(",")
        logger.info(f"hostile = {self.vary_hostile}")
        self.less_hostile = decode(less_hostile).split(",")
        self.text = text
        self.text_len = len(text.split(" "))
        logger.info(f"len= {self.text_len}")
        self.bds_precent = self.check_text()
        logger.info(f"from analyse text \n##\nbds_precent= {self.bds_precent}")
        self.points = float(os.getenv("POINTS"))
        self.high = float(os.getenv("HIGH_SCORE_THREAT_LEVEL"))
        self.medium = float(os.getenv("MEDIUM_SCORE_THREAT_LEVEL"))

    def check_text(self):
        count = 0
        score = 0
        text = self.text.split()
        logger.info("calculating bds level")
        for hostile in self.vary_hostile:
            hostile_len = len(hostile.split())
            logger.info(f"len hostile ---> {hostile_len}")
            for i in range(self.text_len):

                if (hostile.lower() == text[i:i + hostile_len]
                        or hostile == text[i:i + hostile_len]):
                    count += 1
                    score += (self.points * 2)
        for sami_hostile in self.less_hostile:
            sami_hostile_len = len(sami_hostile.split())
            for i in range(self.text_len):
                if sami_hostile.lower() == text[i:i + sami_hostile_len]\
                        or sami_hostile == text[i:i+sami_hostile_len]:
                    count += 1
                    score += self.points
        res = (score+(score-count)) / (self.text_len+(score-count))
        logger.info(f"res ==== {res}")
        return res * 100

    def is_bds(self):
        return self.bds_precent > self.high

    def bds_threat_level(self):
        if self.high < self.bds_precent > self.medium:
            threat = "medium"
        elif self.bds_precent > self.high:
            threat = "high"
        else:
            threat = "none"
        return threat

if __name__ == '__main__':
    res = (2+(1)) / (200)
    print(res*100)