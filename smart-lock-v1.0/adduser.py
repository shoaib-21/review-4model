import noor_headshots as hs
import train_model as tm
#import faceRecog as fr
import fp_enroll as fp
import WWrite as rw
import userdb
import config


def enroll_new_user(uname,empId):
#     datacollected = hs.headshots(uname)
    if hs.headshots(uname):
        modelTrained = tm.trainmodel()
        if modelTrained == True:
            fingerEnrolled = fp.enroll_finger(empId)
            if fingerEnrolled ==True:
                rfidRegistered,rfid= rw.writeRFID(uname)
                if rfidRegistered == True:
                    #create a profile in userdb
                    print('user successfully registered')
                    userdb.enroll(config.db,uname,empId,rfid)
                else :
                    print('rfid error')
            else :
                    print('fp error')
        else :
                    print('train error')
    else :
                    print('dataset error')
#tm.trainmodel()
#fr.Face('yaba mallesh')



