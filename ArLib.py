from ArBd import ArBd1
class ArLib:
    try:
        # CLASS VARIBLE SO THAT IT CAN BE COMMON FOR ALL INSTANCES , WILL BE USED IN OTHER CLASSES
        board = ArBd1()
    except:
        print(' BOARD ERROR')