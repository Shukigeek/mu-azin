from content_classification.base64_decode import *
import os
from services.logger.logger import Logger

logger = Logger.get_logger(index="analysis-logs")


class AnalyzeText:
    def __init__(self, text):
        logger.info("creating two list from giving string ")
        self.vary_hostile = decode(vary_hostile).split(",")
        self.less_hostile = decode(less_hostile).split(",")
        self.text = text
        self.text_len = len(text.split(" "))
        self.bds_precent = self.check_text()
        self.points = os.getenv("POINTS")
        self.high = os.getenv("HIGH_SCORE_THREAT_LEVEL")
        self.medium = os.getenv("MEDIUM_SCORE_THREAT_LEVEL")

    def check_text(self):
        count = 0
        score = 0
        logger.info("calculating bds level")
        for hostile in self.vary_hostile:
            hostile_len = len(hostile.split(" "))
            for i in range(self.text_len):
                if hostile == self.text[i:i + hostile_len]:
                    count += 1
                    score += (self.points * 2)
        for sami_hostile in self.less_hostile:
            sami_hostile_len = len(sami_hostile.split(" "))
            for i in range(self.text_len):
                if sami_hostile == self.text[i:i + sami_hostile_len]:
                    count += 1
                    score += self.points
        res = ((score+(score-count)) / (self.text_len+(score-count)))
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
