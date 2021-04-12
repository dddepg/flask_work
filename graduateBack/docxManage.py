from docxtpl import DocxTemplate
import graduateBack.sql as sql


def creatTable(id,filename):
    doc = DocxTemplate("graduateBack\\templates\\gjsh_templates.docx")
    conn = sql.getConn()
    cur = sql.getCur(conn)
    sql_word = "SELECT * FROM type1table WHERE thetableid=%s"
    cur.execute(sql_word,id)
    results = cur.fetchall()
    context = {'xueke': results[0][1], 'xiangmu': results[0][2],'keti':results[0][3],'shengqrxm':results[0][4],'tbrq':results[0][5],
        'ketim2':results[0][6],'guanjianci':results[0][7],'xmlb':results[0][8],'xkfl':results[0][9],'yjlc':results[0][10],'ktfzr':results[0][11],
        'xb':results[0][12],'mz':results[0][13],'csrq':results[0][14],'xzzw':results[0][15],'zyzc':results[0][16],
        'yjzc':results[0][17],'zhxl':results[0][18],
        'zhxw':results[0][19],'drds':results[0][20],'szs1':results[0][21],'szs2':results[0][22],'ssxt1':results[0][23],'ssxt2':results[0][24],
        'gzdw':results[0][25],'lxdw':results[0][26],'sfzlx':results[0][27],
        'sfzhw':results[0][28],'sf':results[0][29],'yqcg':results[0][30],'zs':results[0][31],
        'sqjf':results[0][32],'jhsj':results[0][33],'ktsjlz':results[0][34],
        'yjjc':results[0][35]}
    doc.render(context)
    doc.save("graduateBack\\static\\word\\"+filename+".docx")
    sql.closeCur(cur, conn)
