import re

def sample_responses(input_text, name):
    #user_message = str(input_text).lower()

    #print(input_text)

    data_tabungan = re.search("tabungan", input_text)
    data_kredit  = re.search("kredit", input_text)

    data_ksm = re.search("ksm", input_text)
    data_kpr = re.search("kpr", input_text)
    data_kkb = re.search("kkb", input_text)
    data_cc = re.search("cc|kartu kredit", input_text)

    if data_tabungan:
        tutorial = """
        Tahapan utama pembukaan rekening Mandiri Tabungan NOW melalui New Livin'by Mandiri:
        1. Tap Belum Punya Rekening : 
        Setelah download Livin’ by Mandiri, Nasabah dapat memilih menu Buka Rekening

        2. Pilih Jenis Kartu Debit: 
        Pilih jenis kartu Debit yang sesuai dengan kebutuhan Nasabah

        3. Verifikasi ID: 
        Upload dokumen identitas yang dibutuhkan seperti KTP

        4. Melengkapi Data: 
        Lengkapi data No. Handphone, Email, Tujuan Pembukaan Rekening, Pendidikan, dll

        5. Verifikasi Wajah: 
        Lanjutkan dengan verifikasi wajah & masukkan OTP

        6.Rekening Jadi: 
        Rekening langsung jadi! Proses pengiriman kartu bisa dipantau langsung via aplikasi Livin’
        """
        return tutorial

    elif data_kredit:
        credit_product = """
        Silahkan Ketik Kode Salah Satu ini:
        1. KSM (Kredit Serbaguna Mandiri)
        2. KPR (Kredit Kepemilikan Rumah)
        3. KKB (Kredit Kendaraan Bermotor)
        4. CC  (Credit Card)
        """
        return credit_product

    elif data_ksm:
        ksm = """
        Mandiri KSM adalah fasilitas kredit yang diberikan kepada pegawai yang memiliki penghasilan tetap atau profesi tetap, pensiunan atau kepada target market tertentu untuk membiayai berbagai macam kebutuhannya.
        
        Fasilitas kredit ini dapat digunakan untuk berbagai kebutuhan antara lain; pendidikan, pernikahan, kesehatan, renovasi rumah dan lainnya.

        Persyaratan Umum:
        - WNI atau berdomisili di Indonesia
        - Usia minimal 21 tahun
        - Usia maksimal pada saat kredit lunas, 55 tahun (pegawai) dan 60 tahun (profesional/wiraswasta)
        - Masa kerja pegawai tetap min. 1 tahun
        - Penghasilan minimum 3 juta

        Dokumen yang diperlukan:
        1. KTP
        2. NPWP
        3. ID Pegawai
        4. Slip Gaji
        5. Rekening Koran selama 3 Bulan Terakhir

        Jika tertarik silahkan hubungi:
        - Rully (wa.me/6285891074756)
        - Jeki  (wa.me/6281311301778)
        - Rini  (wa.me/6281514420595)
        """
        return ksm

    elif data_kpr:
        kpr = """
        Mandiri KPR adalah fasilitas yang diberikan kepada perorangan untuk pembelian rumah baru maupun rumah lama berupa rumah tinggal/apartemen/ruko/rukan yang dijual melalui developer dan non developer.

        Persyaratan Umum:
        - WNI atau berdomisili di Indonesia
        - Usia minimal 21 tahun
        - Usia maksimal pada saat kredit lunas, 55 tahun (pegawai) dan 60 tahun (profesional/wiraswasta)
        - Masa kerja pegawai tetap min. 1 tahun
        - Penghasilan minimum 2,5 juta (Jabodetabek)/ 2 juta (luar Jabodetabek)

        Dokumen yang diperlukan:
        1. KTP
        2. Kartu Keluarga
        3. NPWP
        4. Surat Nikah/Cerai (Bagi yang telah menikah/cerai)
        5. ID Pegawai
        6. Slip Gaji
        7. Rekening Koran selama 3 Bulan Terakhir
        8. Dokumen kepemilikan agunan SHM/SHGB, IMB & PBB

        Jika tertarik silahkan hubungi:
        - Rully (wa.me/6285891074756)
        - Jeki  (wa.me/6281311301778)
        - Rini  (wa.me/6281514420595)
        """
        return kpr

    elif data_kkb:
        kkb = """
        Mandiri KSM adalah fasilitas kredit yang diberikan untuk pembelian new car passenger (mobil penumpang baru) dan commercial car (pick-up only)
        
        Persyaratan Umum:
        - WNI atau berdomisili di Indonesia
        - Usia minimal 21 tahun
        - Usia maksimal pada saat kredit lunas, 55 tahun (pegawai) dan 60 tahun (profesional/wiraswasta)
        - Masa kerja pegawai tetap min. 1 tahun
        - Penghasilan minimum 3 juta

        Dokumen yang diperlukan:
        1. KTP
        2. NPWP
        3. Kartu Keluarga
        4. Slip Gaji
        5. Rekening Koran selama 3 Bulan Terakhir

        Jika tertarik silahkan hubungi:
        - Rully (wa.me/6285891074756)
        - Jeki  (wa.me/6281311301778)
        - Rini  (wa.me/6281514420595)
        """
        return kkb

    elif data_cc:
        cc = """
        Segmen Travel:
        1. Mandiri Signature
        2. Mandiri Traveloka
        3. Mandiri SKYZ

        Segmen Automotives:
        1. Mandiri Co Brand Pertamina

        Segmen Golf:
        1. Mandiri Golf Signature
        2. Mandiri Golf Platinum

        Segmen Lifestyle:
        1. Mandiri Platinum
        2. Mandiri Precious
        3. Mandiri Kartu Kredit Shopee

        Jika tertarik silahkan hubungi:
        - Rully (wa.me/6285891074756)
        - Jeki  (wa.me/6281311301778)
        - Rini  (wa.me/6281514420595)
        """
        return cc

    else:
        return "Maaf Konten Belum Tersedia"

