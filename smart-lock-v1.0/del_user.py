import os
import shutil
import fp_enroll
import userdb
import config
import time
db = config.db
# deleting a user photos dataset
def delete_dataset(username,empId):
    print('in delete user')
    time.sleep(2)
    parentdir = "/home/pi/facial-recognition-main/dataset/"
    path = os.path.join(parentdir,username)
#     try:
    shutil.rmtree(path)
    print("% s removed successfully" % path)
    time.sleep(2)
    fpDeleted = fp_enroll.delete_fp(empId)
    print(fpDeleted)
    if fpDeleted:
        userdb.delete_entry(db,empId)
            
#     except OSError as error:
#         print(error)
#         print("File path can not be removed")
        
#delete_dataset('modi',6)