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

        self.points = int(os.getenv("POINTS",1))
        self.high = int(os.getenv("HIGH_SCORE_THREAT_LEVEL",15))
        self.medium = int(os.getenv("MEDIUM_SCORE_THREAT_LEVEL",7))

    def check_text(self):
        count = 0
        score = 0
        logger.info("calculating bds level")
        for hostile in self.vary_hostile:
            if hostile in self.text:
                    count += 1
                    score += (self.points * 2)
        for sami_hostile in self.less_hostile:
                if sami_hostile in self.text:
                    count += 1
                    score += self.points
        res = (score+(score-count)) / (self.text_len+(score-count))
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
    print(res)