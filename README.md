# QR Code Generator

A modern, stylish QR code generator built with FastAPI and vanilla JavaScript.

![QR Code Generator](static/favicon.png)

## Features

- 🎨 Custom QR code colors
- 📐 Multiple size options (Small, Medium, Large)
- 📶 WiFi QR code support with secure password handling
- 💾 Download QR codes as PNG
- 📱 Fully responsive design
- ✨ Modern glassmorphism UI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python run.py
```

4. Open your browser and go to:
```
http://localhost:8000
```

## API Endpoint

```
GET /api/generate_qr_code?data=...&fill_color=...&back_color=...&box_size=...
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| data | string | required | Content to encode |
| fill_color | string | #000000 | QR code color |
| back_color | string | #ffffff | Background color |
| box_size | int | 10 | Size (5, 10, or 20) |

## Tech Stack

- **Backend:** FastAPI, Python
- **Frontend:** HTML, CSS, JavaScript
- **QR Generation:** qrcode + Pillow

## License

MIT
"# qr-code-generator-website" 
