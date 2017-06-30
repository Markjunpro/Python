class Model(dict, metaclass=ModelMetaclass):

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key]=value

    def getValue(self,key):
        return getattr(self,key,None)

    def getValueOrDefault(self,key):
        value = getattr(self,self,None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s:%s' % (key,str(value)))
                setattr(self,key,value)
        return value

    @classmethod
    @asyncio.coroutine
    def find(cls,pk):
        ' find object by primary key.'
        rs = yield from select(' %s where '%s '= ?' % (cls.__select__,cls.__primary_key__), [pk],1)
        if len(rs)==0:
            return None
        return cls(**rs[0])

    @asyncio.curoutine
    def save(self):
        args = list (map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = yield from excute(self.__insert__,args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s ' % rows)

