class Siswa:
    def __init__(self, nama, kelas, nilai_semester, ikut_eskul):
        self.nama = nama
        self.kelas = kelas
        self.nilai_semester = nilai_semester
        self.ikut_eskul = ikut_eskul

    def hitung_rata_rata(self):
        rata = sum(self.nilai_semester) / len(self.nilai_semester)
        if self.ikut_eskul:
            rata += 5
        return rata


class Universitas:
    def __init__(self, nama, nilai_minimum):
        self.nama = nama
        self.nilai_minimum = nilai_minimum

    def cek(self, rata):
        return "LOLOS" if rata >= self.nilai_minimum else "TIDAK LOLOS"
    
   