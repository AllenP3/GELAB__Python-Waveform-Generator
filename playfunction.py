import importlib
import noteDictionary_v2 as nd
from functionDictionary import Fd

import pyvisa 
from time import sleep



amplitude = "30mVpp"
offset = "0"

rm = pyvisa.ResourceManager()   # create a resource manager object
device = rm.open_resource("TCPIP0::169.254.5.21::inst0::INSTR")   


device.timeout = 1000      

device.write("OUTP1:LOAD 33")   
device.write("OUTP2:LOAD 50")   


def playNote(note, noteDuration, playspeed = 100, function = "sine"):

    beat = 60/playspeed   
    durationDictionary = {
        "full" : 4*beat,
        "half" : 2*beat,
        "half_pointed" : 3*beat,
        "quarter" : beat,
        "quarter_pointed" : 1.5*beat,
        "eighth" : beat/2 ,
        "eighth_pointed" : 3*beat/4,
        "sixteenth": beat/4, 
    }

    #device.write(fd.funcDict[function] + nd.noteDict[note] + ", {}, {}".format(amplitude, offset))
    ch = Fd(1)
    device.write(ch.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0")    #---> insert Magnitude and the offset
    print(ch.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0")
    
    ch2 = Fd(2)
    device.write(ch2.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0")
    print(ch2.funcDict[function] + nd.noteDict[note] + ", 30mVpp, 0")

    device.write("OUTP1 ON")
    device.write("OUTP2 ON")
    

    duration = durationDictionary[noteDuration]   #note duration from dict

    sleep(duration)
    

    device.write("OUTP1 OFF" )
    device.write("OUTP2 OFF" )

    sleep(0.05)