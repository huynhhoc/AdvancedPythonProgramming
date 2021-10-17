from flask import Flask


ungdung = Flask(__name__)

@ungdung.route('/')
def hello():
    tentruong = ' Dai hoc Van Lang!'
    lienket = '<a href="https://www.vanlanguni.edu.vn">' +tentruong+' </a> <br>'
    chuoi = lienket 
    import datetime
    nam = datetime.date.today().year
    chuoi = chuoi + ' <b>Xin <i>chao</i> Tan sinh vien nam ' + str(nam) + '!</b> '
    return chuoi

@ungdung.route('/monhoc/')
def learn():
    chuoi = "Day la trang mon hoc!"
    return chuoi

@ungdung.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Day la trang mon hoc"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi


@ungdung.route('/sinhvien/')
def students():
    chuoi = "Day la trang cac khoa hoc!"
    return chuoi

@ungdung.route('/sinhvien/<int:namhoc>')
def school_year(namhoc):
    chuoi = "Day la nam hoc"
    nam = str(namhoc).upper()
    if nam == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + nam
    return chuoi

if __name__ == "__main__":
    ungdung.run(port=5050)



