from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

# Koneksi ke database MongoDB
connection_string = "mongodb+srv://test:sparta@cluster0.9kunvma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client.dbfotografi

app = Flask(__name__)

# Route untuk halaman user
@app.route('/')
def beranda():
    return render_template('user/beranda.html')

@app.route('/katalog')
def katalog():
    return render_template('user/katalog.html')

@app.route('/kategori')
def kategori():
    return render_template('user/kategori.html')

@app.route('/paket')
def paket():
    return render_template('user/paket.html')

@app.route('/detail-paket/<int:id>')
def detail_paket(id):
    return render_template('user/detail_paket.html', id=id)

@app.route('/booking')
def booking():
    return render_template('user/booking.html')

@app.route('/pembayaran')
def pembayaran():
    return render_template('user/pembayaran.html')

@app.route('/ulasan')
def ulasan():
    return render_template('user/ulasan.html')

@app.route('/riwayat-pemesanan')
def riwayat_pemesanan():
    return render_template('user/riwayat_pemesanan.html')

@app.route('/galeri')
def galeri():
    return render_template('user/galeri.html')

@app.route('/profil')
def profil_user():
    return render_template('user/profil_user.html')

@app.route('/tentang-kami')
def tentang_kami():
    return render_template('user/tentang_kami.html')

@app.route('/kontak')
def kontak():
    return render_template('user/kontak.html')

@app.route('/login-user')
def user_login():
    return render_template('user/login_user.html')

@app.route('/register')
def user_register():
    return render_template('user/register.html')

# Route untuk halaman admin
@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/kelola-katalog')
def kelola_katalog():
    return render_template('admin/kelola_katalog.html')

@app.route('/admin/kelola-paket')
def kelola_paket():
    return render_template('admin/kelola_paket.html')

@app.route('/admin/kelola-pesanan')
def kelola_pesanan():
    return render_template('admin/kelola_pesanan.html')

@app.route('/admin/kelola-jadwal')
def kelola_jadwal():
    return render_template('admin/kelola_jadwal.html')

@app.route('/admin/kelola-galeri')
def kelola_galeri():
    return render_template('admin/kelola_galeri.html')

@app.route('/admin/kelola-user')
def kelola_user():
    return render_template('admin/kelola_user.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login_admin.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
