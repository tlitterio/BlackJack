import settings
class Log(object):
    def __init__(self,SectionId,Round,Log):
        self.SectionId = SectionId
        self.Set = settings.set
        self.Round = settings.round
        self.Log = Log
    def __iter__(self):
        yield 'SectionId', self.Section
        yield 'Set', self.Set
        yield 'Round', self.Round
        yield 'Log', self.Log

