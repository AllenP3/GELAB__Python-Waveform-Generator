class Fd:
    def __init__(self,ch):
        self.dutyCycle = 50    
        self.ch = ch


        self.funcDict = {

            
            "sine": "SOUR%d:APPL:SIN " %self.ch,
            "triangle": "SOUR%d:APPL:TRI " %self.ch,
            "square": "SOUR%d:APPL:SQU " %self.ch,
            "pulse": "SOUR%d:APPL:PULS:DCYC%d" %(self.ch, self.dutyCycle),
            "ramp": "SOUR%d:APPL:RAMP:DCYC%d" % (self.ch, self.dutyCycle) ,
            "noise": "SOUR%d:APPL:NOIS " %self.ch,
            "prbs": "SOUR%d:APPL:PRBS " %self.ch,
            "track": "SOUR%d:TRAC:INV " %self.ch,
        }