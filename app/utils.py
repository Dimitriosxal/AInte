import uuid
from pathlib import Path
import aiofiles

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

async def save_upload_file(file) -> str:
    file_id = str(uuid.uuid4())
    ext = file.filename.split(".")[-1] if "." in file.filename else "dat"
    out_path = UPLOAD_DIR / f"{file_id}.{ext}"

    async with aiofiles.open(out_path, "wb") as out:
        content = await file.read()
        await out.write(content)

    return str(out_path)
