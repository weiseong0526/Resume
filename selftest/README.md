# Real-Time Barcode Scanner

A web-based real-time barcode and QR code scanner using OpenCV and ZXing.js. Scan barcodes directly from your camera - no image upload needed!

## Features

- 📷 **Real-time camera scanning** - No image upload required
- 🔍 **Barcode & QR Code detection** - Supports all common formats
- 📦 **Visual tracking** - Green box follows detected barcodes
- 🎨 **Modern web interface** - Clean and responsive design
- ⚡ **Instant results** - See barcode numbers immediately
- 📱 **Mobile friendly** - Works on phones and tablets

## Requirements

- Python 3.7+
- Web browser with camera access (Chrome, Firefox, Edge, Safari)
- Internet connection (for ZXing.js library)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note:** For Windows, you may need to install `pyzbar` dependencies:
- Download Visual C++ Redistributable if needed
- Or install from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyzbar

### 2. Start the Server

**Windows:**
```bash
python app.py
```

Or use the batch file:
```bash
start_server.bat
```

**Linux/Mac:**
```bash
python3 app.py
```

Or use the shell script:
```bash
chmod +x start_server.sh
./start_server.sh
```

### 3. Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

## How to Use

1. **Click "Start Camera"** - Allow camera permission when prompted
2. **Point camera at barcode/QR code** - Hold steady, 6-12 inches away
3. **See results instantly** - Barcode number appears in results panel
4. **Visual tracking** - Green box shows detected barcode location
5. **Click "Stop Camera"** - When finished scanning

## Supported Barcode Formats

- QR Code
- CODE_128
- CODE_39
- EAN-13
- EAN-8
- UPC-A
- UPC-E
- And more!

## Tips for Best Results

- ✅ Hold barcode steady and flat
- ✅ Ensure good lighting
- ✅ Keep barcode in focus
- ✅ Try different distances (6-12 inches usually works best)
- ✅ Make sure entire barcode is visible in camera view

## Troubleshooting

### Camera not working
- Make sure you're using HTTPS or localhost (required for camera access)
- Check browser permissions (allow camera access)
- Try a different browser (Chrome, Firefox, Edge)
- Make sure no other app is using the camera

### No barcode detected
- Ensure good lighting
- Hold barcode steady
- Try different angles
- Make sure barcode is not damaged or dirty

### Port already in use
- Change the port in `app.py`: `app.run(port=5001)`

## API Endpoints

### POST /scan_barcode
Process image frame for barcode detection (used internally).

**Request:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGgo..."
}
```

**Response:**
```json
{
  "success": true,
  "barcodes": [
    {
      "data": "1234567890",
      "type": "CODE_128",
      "x": 100,
      "y": 50,
      "w": 200,
      "h": 50
    }
  ]
}
```

## License

MIT License
