import re

class AndroidLogParser:
    def __init__(self, logType="threadtime"):
        #print "AndroidLogParser init"
        self.parser = re.compile(r'([\d]+)-([\d]+) ([\d]+):([\d]+):([\d]+).([\d]+)  ([\d]+)  ([\d]+) ([IVDE]+) ([\w ]*): ([\w .]*)')
        self.keys = ["month", "date", "hour", "minute", "second", "microsecond", "pid", "tid", "type", "tag", "log"]
        self.result = {}

    def parse(self, line):
        #print "AndroidLogParser parse"
        result = self.parser.search(line)
        if result:
            #print result.group(0)
            for i in range(len(self.keys)):
                self.result[self.keys[i]] = result.group(i+1)
        else:
            self.result = {}
        #print self.result
        return self.result

    def getKeys(self):
        #print "AndroidLogParser getKeys"
        return self.keys

