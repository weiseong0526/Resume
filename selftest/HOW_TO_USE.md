# How to Use the Barcode Scanner

## Quick Start Guide

### Step 1: Install Python (if not installed)

**Windows:**
1. Download Python from: https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Install Python 3.8 or newer

### Step 2: Install Required Packages

Open Command Prompt or PowerShell in this folder and run:

```bash
python -m pip install Flask opencv-python pyzbar Pillow numpy
```

Or if you have `pip` directly:
```bash
pip install -r requirements.txt
```

### Step 3: Start the Server

**Option A - Double-click the batch file:**
- Double-click `start_server.bat`

**Option B - Run from command line:**
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 4: Open in Browser

1. Open your web browser (Chrome, Firefox, or Edge)
2. Go to: **http://localhost:5000**
3. You should see the scanner page

### Step 5: Start Scanning

1. **Click "Start Camera"** button
2. **Allow camera permission** when browser asks
3. **Point your camera at a barcode or QR code**
4. **Hold steady** - keep the barcode 6-12 inches away
5. **See results instantly** - barcode number appears in the right panel!

### Step 6: Stop Scanning

- Click **"Stop Camera"** when finished

---

## Troubleshooting

### ❌ "Python not found"
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### ❌ "pip not recognized"
- Try: `python -m pip install Flask opencv-python pyzbar Pillow numpy`
- Or: `py -m pip install Flask opencv-python pyzbar Pillow numpy`

### ❌ "Camera not working"
- Make sure you're using **http://localhost:5000** (not file://)
- Allow camera permission in browser
- Try a different browser (Chrome works best)
- Make sure no other app is using the camera

### ❌ "No barcode detected"
- Ensure good lighting
- Hold barcode steady
- Try different distances (6-12 inches)
- Make sure entire barcode is visible

### ❌ "Port 5000 already in use"
- Close other programs using port 5000
- Or change port in `app.py` line: `app.run(port=5001)`

---

## Tips for Best Results

✅ **Good lighting** - Make sure barcode is well-lit  
✅ **Hold steady** - Don't move camera too fast  
✅ **Right distance** - 6-12 inches usually works best  
✅ **Clean barcode** - Make sure barcode is not damaged  
✅ **Full view** - Entire barcode should be visible in camera  

---

## What You'll See

- **Left side**: Camera view with green scanning overlay
- **Right side**: Results panel showing detected barcode numbers
- **Green box**: Appears around detected barcodes
- **Status indicator**: Shows if camera is active (green) or stopped (red)

---

## Supported Barcode Types

- ✅ QR Code
- ✅ CODE_128
- ✅ CODE_39
- ✅ EAN-13
- ✅ EAN-8
- ✅ UPC-A
- ✅ UPC-E
- ✅ And more!

---

## Need Help?

1. Make sure Python is installed: `python --version`
2. Make sure packages are installed: `python -m pip list`
3. Check if server is running: Look for "Running on http://..." message
4. Try refreshing the browser page
5. Check browser console (F12) for errors

