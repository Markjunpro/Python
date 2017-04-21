@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with (yield from __pool) as coon:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.excute(sql.replace('?','%s'),args or ())
        if size :
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
         yield from cur.close()
         logging.info('rows returned :%s ' % len(rs))
         return rs
     

