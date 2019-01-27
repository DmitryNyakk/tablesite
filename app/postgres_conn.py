import psycopg2


def check_val(dica_row):
    dict_post=[]
    dict_check = {'city':['ILIKE','gorod','%'],
    'idi':['=','id',''],
    'name':['ILIKE','name_p','%'],
    'sem_pol':['=','sem_pol',''],
    'age':['=','age',''],
    'rodn_gorod':['ILIKE','r_gorod','%']}
    cnt=0
    selen='SELECT id,name_p,gorod,url,sem_pol,age,r_gorod FROM vk_tb '
    for k,v in dica_row.items():
        if dict_check.get(k) and v:
            cnt+=1
       #     print('CHECK {} {}'.format(dict_check[k],v))
            if cnt>1:selen+=""" and {0} {1} '{3}{2}{3}' """.format(dict_check[k][1],dict_check[k][0],v,dict_check[k][2])
            else: selen+=""" WHERE {0} {1} '{3}{2}{3}' """.format(dict_check[k][1],dict_check[k][0],v,dict_check[k][2])
  # print(selen)
    if cnt>0:return '{} LIMIT 325'.format(selen)
    return """SELECT id,name_p,gorod,url,sem_pol,age,r_gorod FROM vk_tb  LIMIT 325"""

def postgr_req(dica_row):
    #print(dica_row)
    try:
        conn= psycopg2.connect("dbname='vk_db' user='postgres' host='localhost' password='55555' connect_timeout=2")
    except:
        print("DB postgres notreacheable")

    query=check_val(dica_row)
    print(query)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    users=[]
    en=-1
    for en,row in enumerate(rows):
        user = {
                'id': row[0],
                'name_p':row[1],
                'gorod':row[2],
                'url':row[3],
                'sem_pol':row[4],
                'age':row[5],
                'r_gorod':row[6]
                }
        users.append(user)
    conn.close()
    newusers = sorted(users, key=lambda k: k['id']) 
    return en+1,newusers
