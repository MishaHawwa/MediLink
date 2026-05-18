# AI-Driven Emergency and Hospital Optimization System
## Complete Installation & Setup Guide

---

## 🚀 Quick Start (4-Hour Build)

### Prerequisites
Before starting, ensure you have:
- **Node.js** (v16 or higher) - [Download here](https://nodejs.org/)
- **Python** (v3.8 or higher) - [Download here](https://www.python.org/)
- **pip** (Python package manager - comes with Python)
- **Git** (optional) - [Download here](https://git-scm.com/)

---

## 📦 Installation Steps

### Step 1: Verify Prerequisites

Open Command Prompt (cmd) and verify installations:

```cmd
node --version
npm --version
python --version
pip --version
```

### Step 2: Install Frontend Dependencies

Navigate to the project folder and install React dependencies:

```cmd
cd c:\Users\CITYcomp\Desktop\version1
npm install
```

This will install:
- React & React-DOM
- React-Leaflet (for maps)
- Socket.IO Client (for real-time tracking)
- Axios (for API calls)

### Step 3: Install Backend Dependencies

Install Python packages for the Flask backend:

```cmd
cd backend
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- Flask-CORS (cross-origin support)
- Flask-SocketIO (real-time communication)
- scikit-learn (ML for ETA prediction)
- geopy (distance calculations)
- numpy & pandas (data processing)

---

## 🏃 Running the Application

### Terminal 1: Start Backend Server

```cmd
cd c:\Users\CITYcomp\Desktop\version1\backend
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Restarting with stat
```

**Keep this terminal running!**

### Terminal 2: Start Frontend

Open a NEW Command Prompt window:

```cmd
cd c:\Users\CITYcomp\Desktop\version1
npm start
```

The app will automatically open in your browser at `http://localhost:3000`

**Keep this terminal running too!**

---

## 🎯 Testing the Application

1. **Dashboard Screen**: Click any emergency type (Heart Attack, Stroke, etc.)
2. **Loading Screen**: Watch AI analyze hospitals (3 seconds)
3. **Tracking Screen**: See live map with:
   - Patient location (red marker)
   - Ambulance location (blue marker - moves in real-time!)
   - Hospital location (green marker)
   - Route line connecting all points
   - AI emergency guidance below the map

---

## 🔧 Troubleshooting

### Issue: "npm: command not found"
**Solution**: Install Node.js from https://nodejs.org/

### Issue: "python: command not found"
**Solution**: Install Python and check "Add to PATH" during installation

### Issue: "Module not found" errors
**Solution**: 
```cmd
npm install
cd backend
pip install -r requirements.txt
```

### Issue: Backend connection error
**Solution**: Ensure backend is running on port 5000
```cmd
cd backend
python app.py
```

### Issue: Location not working
**Solution**: Allow location access when browser prompts, or app uses default Bangalore coordinates

---

## 📁 Project Structure

```
version1/
├── backend/
│   ├── app.py              # Flask server with AI logic
│   └── requirements.txt    # Python dependencies
├── src/
│   ├── components/
│   │   ├── Dashboard.js    # Emergency selection screen
│   │   ├── LoadingScreen.js # AI analysis animation
│   │   └── TrackingScreen.js # Live tracking with map
│   ├── App.js              # Main app logic
│   └── index.js            # React entry point
├── public/
│   └── index.html          # HTML template
└── package.json            # Node dependencies
```

---

## ✨ Key Features Implemented

### ✅ Priority 1 (MUST HAVE)
- [x] Emergency Dashboard with 5 buttons
- [x] Hospital Selection (nearest matching hospital)
- [x] Ambulance Assignment (nearest available)
- [x] Live Map (patient, ambulance, hospital markers)
- [x] Simulated Ambulance Movement (real-time)
- [x] Automatic location tracking

### ✅ Priority 2 (BONUS)
- [x] AI ETA prediction using Random Forest
- [x] Socket.IO real-time tracking
- [x] AI emergency guidance suggestions
- [x] Animated loading screen

---

## 🎨 Technologies Used

- **Frontend**: React.js
- **Maps**: Leaflet + OpenStreetMap
- **Backend**: Flask + Flask-SocketIO
- **Real-Time**: Socket.IO
- **AI/ML**: scikit-learn Random Forest
- **Database**: In-memory (Python dictionaries)

---

## 🚀 Demo Flow

1. User clicks "Heart Attack"
2. GPS location captured automatically
3. AI checks 5 hospitals
4. Closest hospital rejected (no cardiac ICU)
5. Better hospital selected (CityCare Hospital)
6. Nearest ambulance assigned
7. Live tracking starts
8. Hospital notified (simulated)
9. ETA updates dynamically
10. AI shows emergency guidance

---

## 📊 Sample Data

The system includes:
- **5 Hospitals** with different specialties
- **5 Ambulances** at various locations
- **5 Emergency Types** with AI guidance
- **ML Model** for ETA prediction

---

## 🎓 For Presentation

**Key Points to Highlight:**
1. AI-based hospital selection (not just nearest)
2. Real-time ambulance tracking
3. ML-powered ETA prediction
4. Emergency-specific AI guidance
5. Smart routing considering ICU availability

---

## 📝 Notes

- Backend runs on port 5000
- Frontend runs on port 3000
- Location permission required for accurate tracking
- All data is simulated (no real database)
- Ambulance movement is animated for demo

---

## 🆘 Need Help?

If you encounter issues:
1. Check both terminals are running
2. Verify all dependencies installed
3. Check browser console for errors (F12)
4. Ensure ports 3000 and 5000 are not in use

---

**Built in 4 hours for emergency response optimization! 🚑**
