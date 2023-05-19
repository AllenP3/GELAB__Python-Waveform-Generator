import playfunction as pf

Speed = 100


def main():
    func = "sine"
    pf.playNote("C4", "quarter", Speed, func)
    pf.playNote("D4", "quarter", Speed, func)
    pf.playNote("E4", "quarter", Speed, func)
    pf.playNote("F4", "quarter", Speed, func)
    pf.playNote("G4", "quarter", Speed, func)
    pf.playNote("A4", "quarter", Speed, func)
    pf.playNote("B4", "quarter", Speed, func)
    pf.playNote("C5", "quarter", Speed, func)



if __name__ == '__main__':
    main()