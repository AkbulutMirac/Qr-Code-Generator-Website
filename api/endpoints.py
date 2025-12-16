from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from .services import generate_qr_code

router = APIRouter()

@router.get("/generate_qr_code")
def get_qr_code(data: str, fill_color: str = "black", back_color: str = "white", box_size: int = 10):
    """
    Endpoint to generate a QR code image.

    Parameters:
    data (str): The data to encode in the QR code.
    fill_color (str): The color of the QR code dots.
    back_color (str): The background color of the QR code.
    box_size (int): Pixel size of each QR code box (default: 10).

    Returns:
    StreamingResponse: The generated QR code image as a PNG file.
    """
    try:
        image_bytes = generate_qr_code(data, fill_color, back_color, box_size)
        return StreamingResponse(image_bytes, media_type="image/png", headers={"Content-Disposition": "attachment; filename=qrcode.png"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
