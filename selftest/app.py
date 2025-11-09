from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from pyzbar import pyzbar
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('scanner.html')

@app.route('/face-tracker')
def face_tracker():
    """Serve the face tracker page"""
    return render_template('face_tracker.html')

@app.route('/scan_barcode', methods=['POST'])
def scan_barcode():
    """Process image frame for barcode detection using OpenCV and pyzbar"""
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Decode base64 image
        image_data = data['image']
        if ',' in image_data:
            image_data = image_data.split(',')[1]  # Remove data:image/png;base64, prefix
        
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({'error': 'Invalid image data'}), 400
        
        # Detect barcodes using pyzbar (uses OpenCV internally)
        barcodes = pyzbar.decode(image)
        
        results = []
        for barcode in barcodes:
            # Extract barcode data
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            
            # Get bounding box
            points = barcode.polygon
            if len(points) == 4:
                # Get rectangle coordinates
                x = min([p.x for p in points])
                y = min([p.y for p in points])
                w = max([p.x for p in points]) - x
                h = max([p.y for p in points]) - y
            else:
                rect = barcode.rect
                x, y, w, h = rect.left, rect.top, rect.width, rect.height
            
            results.append({
                'data': barcode_data,
                'type': barcode_type,
                'x': int(x),
                'y': int(y),
                'w': int(w),
                'h': int(h)
            })
        
        if results:
            return jsonify({
                'success': True,
                'barcodes': results
            })
        else:
            return jsonify({
                'success': False,
                'message': 'No barcode detected'
            })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
