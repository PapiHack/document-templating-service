from fastapi import Body, FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import Json
from docxtpl import DocxTemplate
import aiofiles
from utils import remove_temporary_files, get_env
import requests

app = FastAPI(
    title="Document Template Processing Service",
    description="""
        This is the documentation of the REST API exposed by the document template processing microservice.
        This will allow you to inject data in a specific word document template and get the pdf format as a result. 🚀🚀🚀
    """,
    version="1.0.0"
)

SERVICE_STATUS = {'status': 'Service is healthy !'}

@app.get('/')
async def livenessprobe():
    remove_temporary_files()
    return SERVICE_STATUS

@app.get('/health-check')
async def healthcheck():
    remove_temporary_files()
    return SERVICE_STATUS

@app.post('/api/v1/process-template-document')
async def process_document_template(data: Json = Body(...), file: UploadFile = File(...)):
    if file.filename == '':
        return JSONResponse({'status': 'error', 'message': 'file is required'}, status_code=400)
    if data is None or len(data) == 0:
        return JSONResponse({'status': 'error', 'message': 'data is required'}, status_code=400)
    resourceURL = get_env('GOTENBERG_API_URL') + '/forms/libreoffice/convert'
    file_path = 'temp/{}'.format(file.filename)
    pdf_file_path = 'temp/{}.pdf'.format(file.filename.split('.')[0])
    async with aiofiles.open(file_path, 'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    document = DocxTemplate(file_path)
    document.render(data)
    document.save(file_path)
    response = requests.post(url=resourceURL, files={'file': open(file_path, 'rb')})
    async with aiofiles.open(pdf_file_path, 'wb') as out_file:
        await out_file.write(response.content)
    return FileResponse(pdf_file_path, media_type='application/pdf')