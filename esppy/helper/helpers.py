#Helpfer Function:
def create_scoring_schema(number_objects):
    _field = "id*:int64,image:blob,_image_:blob,_nObjects_:double,"
    for obj in range(0,number_objects):
        _field += "_Object" + str(obj) + "_:string,"
        _field += "_P_Object" + str(obj) + "_:double,"
        _field += "_Object" + str(obj) + "_x:double,"
        _field += "_Object" + str(obj) + "_y:double,"
        _field += "_Object" + str(obj) + "_width:double,"
        _field += "_Object" + str(obj) + "_height:double,"
    return _field[:-1]

def create_scoring_schema(number_objects):
    _field = "id*:int64,image:blob,_image_:blob,_nObjects_:double,"
    for obj in range(0,number_objects):
        _field += "_Object" + str(obj) + "_:string,"
        _field += "_P_Object" + str(obj) + "_:double,"
        _field += "_Object" + str(obj) + "_x:double,"
        _field += "_Object" + str(obj) + "_y:double,"
        _field += "_Object" + str(obj) + "_width:double,"
        _field += "_Object" + str(obj) + "_height:double,"
    return _field[:-1]
