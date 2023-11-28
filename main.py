from typing import Annotated, Optional
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import RedirectResponse
import starlette.status as status
# from fastapi.templating import Jinja2Templates
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import uuid
import os
from datetime import datetime
import uuid
import mysql.connector

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# MySQL database configuration
db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "ukpbj_db",
}

# Create a connection to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

@app.get("/")
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("beranda.html", context)

@app.post("/tambah_pekerjaan", status_code=201)
async def tambah_pekerjaan(
    request: Request,
    nama_unit: Annotated[str, Form(...)],
    nama_pekerjaan: Annotated[str, Form(...)],
    pagu: Annotated[str, Form(...)],
    tgl_pengajuan: Annotated[str, Form(...)],
    nama_ppk: Annotated[str, Form(...)],
):
    new_uuid = uuid.uuid1()
    tgl_pengajuan_sql = datetime.strptime(tgl_pengajuan, "%Y-%m-%d").strftime("%Y-%m-%d 00:00:00")
    
    folder_path = os.path.join("/files", str(new_uuid))
    os.makedirs(folder_path)

    data = (
        new_uuid.bytes,
        nama_unit,
        nama_pekerjaan,
        pagu,
        tgl_pengajuan_sql,
        nama_ppk,
    )

    query = """
    INSERT INTO pekerjaan (uuid, nama_unit, nama_pekerjaan, pagu, tgl_pengajuan, nama_ppk)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, data)
    conn.commit()

    payload = {
        "uuid": uuid,
        "nama_unit": nama_unit,
        "nama_pekerjaan": nama_pekerjaan,
        "pagu": pagu,
        "tgl_pengajuan": tgl_pengajuan_sql,
        "nama_ppk": nama_ppk,
        "folder_path": folder_path,
    }
    
    return templates.TemplateResponse(f"detail.html", context={"request": request, "data": payload})

def query_pekerjaan(uuid_pekerjaan=None):
    if not uuid_pekerjaan:
        query = "SELECT uuid, nama_unit, nama_pekerjaan, tgl_pengajuan, nama_ppk FROM pekerjaan"
        cursor.execute(query)
    else:
        query = "SELECT uuid, nama_unit, nama_pekerjaan, pagu, tgl_pengajuan, nama_ppk FROM pekerjaan WHERE uuid = %s"
        cursor.execute(query, (uuid_pekerjaan.bytes,))

    return cursor.fetchall()

@app.post("/edit_pekerjaan", status_code=201)
async def edit_pekerjaan_2(
    request: Request,
    nama_unit: Annotated[Optional[str], Form()],
    nama_pekerjaan: Annotated[Optional[str], Form()],
    pagu: Annotated[Optional[str], Form()],
    tgl_pengajuan: Annotated[Optional[str], Form()],
    nama_ppk: Annotated[Optional[str], Form()],
    nama_pp: Annotated[Optional[str], Form()],
    nama_pokja: Annotated[Optional[str], Form()],
    kak: Annotated[Optional[UploadFile], File()],
    hps: Annotated[Optional[UploadFile], File()],
    spesifikasi_teknis: Annotated[Optional[UploadFile], File()],
    r_kontrak: Annotated[Optional[UploadFile], File()],
    dokum_penyedia: Annotated[Optional[UploadFile], File()],
    data_pemilihan: Annotated[Optional[UploadFile], File()],
    daftar_harga: Annotated[Optional[UploadFile], File()],
    jadwal: Annotated[Optional[UploadFile], File()],
    rancangan_kerja: Annotated[Optional[UploadFile], File()],
    dc_studi_kelayakan: Annotated[Optional[UploadFile], File()],
    dc_penawaran: Annotated[Optional[UploadFile], File()],
    surat_penawaran: Annotated[Optional[UploadFile], File()],
    sertifikat: Annotated[Optional[UploadFile], File()],
    ba_pemberian: Annotated[Optional[UploadFile], File()],
    ba_pengumuman: Annotated[Optional[UploadFile], File()],
    ba_sanggah: Annotated[Optional[UploadFile], File()],
    ba_penetapan: Annotated[Optional[UploadFile], File()],
    laporan_hasil: Annotated[Optional[UploadFile], File()],
    dc_kontrak: Annotated[Optional[UploadFile], File()],
    surat_pemerintah: Annotated[Optional[UploadFile], File()],
    surat_jaminan: Annotated[Optional[UploadFile], File()],
    surat_jaminan_uang: Annotated[Optional[UploadFile], File()],
    surat_jaminan_pemeliharaan: Annotated[Optional[UploadFile], File()],
    surat_tagihan: Annotated[Optional[UploadFile], File()],
    surat_pesanan_epurchasing: Annotated[Optional[UploadFile], File()],
    surat_perintah_membayar: Annotated[Optional[UploadFile], File()],
    surat_perintah_pencairan_dana: Annotated[Optional[UploadFile], File()],
    laporan_pelaksanaan: Annotated[Optional[UploadFile], File()],
    laporan_penyelesaian: Annotated[Optional[UploadFile], File()],
    ba_pemeriksa_hasil: Annotated[Optional[UploadFile], File()],
    ba_serah_terima_sementara: Annotated[Optional[UploadFile], File()],
    ba_serah_terima: Annotated[Optional[UploadFile], File()],
):
    payload = {
        "uuid": uuid,
        "nama_unit": nama_unit,
        "nama_pekerjaan": nama_pekerjaan,
        "pagu": pagu,
        "tgl_pengajuan": tgl_pengajuan_sql,
        "nama_ppk": nama_ppk,
        "nama_pp": nama_pp,
        "nama_pokja": nama_pokja,
        "folder_path": folder_path,
        "kak_filename": kak.filename,
        "hps_filename": hps.filename,
        "spesifikasi_teknis_filename": spesifikasi_teknis.filename,
        "r_kontrak_filename": r_kontrak.filename,
        "dokum_penyedia_filename": dokum_penyedia.filename,
        "data_pemilihan_filename": data_pemilihan.filename,
        "daftar_harga_filename": daftar_harga.filename,
        "jadwal_filename": jadwal.filename,
        "rancangan_kerja_filename": rancangan_kerja.filename,
        "dc_studi_kelayakan_filename": dc_studi_kelayakan.filename,
        "dc_penawaran_filename": dc_penawaran.filename,
        "surat_penawaran_filename": surat_penawaran.filename,
        "sertifikat_filename": sertifikat.filename,
        "ba_pemberian_filename": ba_pemberian.filename,
        "ba_pengumuman_filename": ba_pengumuman.filename,
        "ba_sanggah_filename": ba_sanggah.filename,
        "ba_penetapan_filename": ba_penetapan.filename,
        "laporan_hasil_filename": laporan_hasil.filename,
        "dc_kontrak_filename": dc_kontrak.filename,
        "surat_pemerintah_filename": surat_pemerintah.filename,
        "surat_jaminan_filename": surat_jaminan.filename,
        "surat_jaminan_uang_filename": surat_jaminan_uang.filename,
        "surat_jaminan_pemeliharaan_filename": surat_jaminan_pemeliharaan.filename,
        "surat_tagihan_filename": surat_tagihan.filename,
        "surat_pesanan_epurchasing_filename": surat_pesanan_epurchasing.filename,
        "surat_perintah_membayar_filename": surat_perintah_membayar.filename,
        "surat_perintah_pencairan_dana_filename": surat_perintah_pencairan_dana.filename,
        "laporan_pelaksanaan_filename": laporan_pelaksanaan.filename,
        "laporan_penyelesaian_filename": laporan_penyelesaian.filename,
        "ba_pemeriksa_hasil_filename": ba_pemeriksa_hasil.filename,
        "ba_serah_terima_sementara_filename": ba_serah_terima_sementara.filename,
        "ba_serah_terima_filename": ba_serah_terima.filename,
    }
    return templates.TemplateResponse(f"detail.html", context={"request": request, "data": payload})

@app.get("/detail/{uuid_pekerjaan}", status_code=200)
async def detail_pekerjaan(request: Request, uuid_pekerjaan: uuid.UUID):
    temp_data = query_pekerjaan(uuid_pekerjaan=uuid_pekerjaan)[0]
    if not temp_data:
        raise("NOT FOUND")
    columns = ["uuid", "nama_unit", "nama_pekerjaan", "pagu", "tgl_pengajuan", "nama_ppk"]
    payload = {columns[i]: temp_data[i] for i in range(len(columns))}
    payload["uuid"] = uuid.UUID(bytes=bytes(payload["uuid"]))
    payload["tgl_pengajuan"] = str(payload["tgl_pengajuan"])[:10]
    return templates.TemplateResponse(f"detail.html", context={"request": request, "data": payload})

@app.post("/simpan/{uuid_pekerjaan}", status_code=201)
async def simpan_pekerjaan(
    request: Request,
    uuid_pekerjaan: uuid.UUID,
    nama_unit: Annotated[str, Form(...)],
    nama_pekerjaan: Annotated[str, Form(...)],
    pagu: Annotated[str, Form(...)],
    tgl_pengajuan: Annotated[str, Form(...)],
    nama_ppk: Annotated[str, Form(...)],
):
    tgl_pengajuan_sql = datetime.strptime(tgl_pengajuan, "%Y-%m-%d").strftime("%Y-%m-%d 00:00:00")
    
    folder_path = os.path.join("/files", str(uuid_pekerjaan))

    data = (
        nama_unit,
        nama_pekerjaan,
        pagu,
        tgl_pengajuan_sql,
        nama_ppk,
        uuid_pekerjaan.bytes,
    )

    query = """
    UPDATE pekerjaan SET
        nama_unit = %s,
        nama_pekerjaan = %s,
        pagu = %s,
        tgl_pengajuan = %s,
        nama_ppk = %s
    WHERE uuid = %s
    """

    cursor.execute(query, data)
    conn.commit()
    
    return RedirectResponse(url=f'/detail/{uuid_pekerjaan}', status_code=status.HTTP_302_FOUND)


@app.get("/edit/{uuid_pekerjaan}", status_code=200)
async def edit_pekerjaan(request: Request, uuid_pekerjaan: uuid.UUID):
    temp_data = query_pekerjaan(uuid_pekerjaan=uuid_pekerjaan)[0]
    if not temp_data:
        raise("NOT FOUND")
    columns = ["uuid", "nama_unit", "nama_pekerjaan", "pagu", "tgl_pengajuan", "nama_ppk"]
    payload = {columns[i]: temp_data[i] for i in range(len(columns))}
    payload["uuid"] = uuid.UUID(bytes=bytes(payload["uuid"]))
    payload["tgl_pengajuan"] = str(payload["tgl_pengajuan"])[:10]
    return templates.TemplateResponse(f"edit.html", context={"request": request, "data": payload})

@app.get("/{page_name}", status_code=200)
async def any_page(request: Request, page_name: str):
    payload = {}
    if page_name == "beranda":
        temp_data = query_pekerjaan()
        payload = [(uuid.UUID(bytes=bytes(d[0])), d[1], d[2], str(d[3])[:10], d[4]) for d in temp_data]
    elif page_name == "rekap":
        temp_data = query_pekerjaan()
        payload = [(uuid.UUID(bytes=bytes(d[0])), d[1], d[2], str(d[3])[:10], d[4]) for d in temp_data]
    elif page_name == "pekerjaan":
        temp_data = query_pekerjaan()
        payload = [(uuid.UUID(bytes=bytes(d[0])), d[1], d[2], str(d[3])[:10], d[4]) for d in temp_data]
    return templates.TemplateResponse(f"{page_name}.html", context={"request": request, "data": payload})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)