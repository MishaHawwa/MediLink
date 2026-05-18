# 📁 Project Structure

## Complete File Tree

```
version1/
│
├── 📄 START_HERE.md                    ← Read this first!
├── 📄 INSTALLATION_GUIDE.md            ← Detailed installation steps
├── 📄 QUICK_START_CHECKLIST.md         ← Pre-demo checklist
├── 📄 README_PROJECT.md                ← Project overview
├── 📄 PROJECT_SUMMARY.md               ← Technical deep dive
├── 📄 readme.md                        ← Original requirements
│
├── 🔧 package.json                     ← Frontend dependencies
├── 🔧 .gitignore                       ← Git ignore rules
│
├── ⚡ install-all.bat                  ← One-click install
├── ⚡ start-backend.bat                ← Start Flask server
├── ⚡ start-frontend.bat               ← Start React app
│
├── 📂 backend/                         ← Python Flask Backend
│   ├── app.py                          ← Main server (400+ lines)
│   │   ├── Hospital database
│   │   ├── Ambulance tracker
│   │   ├── ML model (Random Forest)
│   │   ├── Smart routing algorithm
│   │   ├── WebSocket server
│   │   └── API endpoints
│   │
│   └── requirements.txt                ← Python dependencies
│       ├── Flask
│       ├── Flask-SocketIO
│       ├── scikit-learn
│       ├── geopy
│       └── more...
│
├── 📂 src/                             ← React Frontend
│   ├── index.js                        ← React entry point
│   ├── index.css                       ← Global styles
│   │
│   ├── App.js                          ← Main app logic
│   │   ├── Screen management
│   │   ├── Location tracking
│   │   ├── API calls
│   │   └── State management
│   │
│   ├── App.css                         ← App styles
│   │
│   └── 📂 components/                  ← React Components
│       │
│       ├── Dashboard.js                ← Screen 1: Emergency Selection
│       │   ├── 5 emergency cards
│       │   ├── System status
│       │   └── Stats display
│       │
│       ├── Dashboard.css               ← Dashboard styles
│       │   ├── Card animations
│       │   ├── Color schemes
│       │   └── Responsive grid
│       │
│       ├── LoadingScreen.js            ← Screen 2: AI Analysis
│       │   ├── Animated spinner
│       │   ├── 5-step progress
│       │   └── Loading messages
│       │
│       ├── LoadingScreen.css           ← Loading styles
│       │   ├── Spinner animation
│       │   ├── Step transitions
│       │   └── Pulse effects
│       │
│       ├── TrackingScreen.js           ← Screen 3: Live Tracking
│       │   ├── Interactive map
│       │   ├── Real-time updates
│       │   ├── WebSocket connection
│       │   ├── AI guidance display
│       │   └── Status cards
│       │
│       └── TrackingScreen.css          ← Tracking styles
│           ├── Map container
│           ├── Info cards
│           ├── Suggestions section
│           └── Responsive layout
│
└── 📂 public/                          ← Static Files
    └── index.html                      ← HTML template
        ├── Meta tags
        ├── Leaflet CSS
        └── Root div
```

---

## File Purposes

### 📄 Documentation Files

| File | Purpose | When to Read |
|------|---------|--------------|
| START_HERE.md | Quick start guide | First time setup |
| INSTALLATION_GUIDE.md | Detailed installation | Having issues |
| QUICK_START_CHECKLIST.md | Pre-demo checklist | Before presenting |
| README_PROJECT.md | Project overview | Understanding features |
| PROJECT_SUMMARY.md | Technical details | Deep dive |
| PROJECT_STRUCTURE.md | This file | Understanding organization |

### ⚡ Batch Files (Windows)

| File | Purpose | When to Use |
|------|---------|-------------|
| install-all.bat | Install all dependencies | First time only |
| start-backend.bat | Start Flask server | Every time (Terminal 1) |
| start-frontend.bat | Start React app | Every time (Terminal 2) |

### 🔧 Configuration Files

| File | Purpose |
|------|---------|
| package.json | Frontend dependencies & scripts |
| requirements.txt | Backend Python packages |
| .gitignore | Files to exclude from Git |

---

## Code Organization

### Backend (app.py)

```python
# Imports & Setup
Flask, SocketIO, ML libraries

# Data Structures
├── hospitals[]          # 5 hospitals with specialties
├── ambulances[]         # 5 ambulances with locations
├── emergency_requirements{}  # Emergency type mappings
└── ai_suggestions{}     # First aid guidance

# ML Model
└── train_eta_model()    # Random Forest training

# Helper Functions
├── calculate_distance() # Geospatial calculations
├── predict_eta()        # ML-based ETA prediction
└── score_hospital()     # Smart hospital scoring

# API Endpoints
├── POST /api/emergency  # Handle emergency request
├── GET /api/hospitals   # List all hospitals
└── GET /api/ambulances  # List all ambulances

# WebSocket Events
├── @socketio.on('connect')
├── @socketio.on('start_tracking')
└── emit('ambulance_update')  # Real-time updates
```

### Frontend (React)

```javascript
// App.js - Main Controller
├── State Management
│   ├── screen (dashboard/loading/tracking)
│   ├── emergencyData
│   ├── selectedEmergency
│   └── userLocation
│
├── Effects
│   └── useEffect() → Get GPS location
│
├── Handlers
│   ├── handleEmergencySelect()
│   └── handleBackToDashboard()
│
└── Render Logic
    ├── <Dashboard />
    ├── <LoadingScreen />
    └── <TrackingScreen />

// Dashboard.js - Emergency Selection
├── emergencies[] array
├── Emergency cards grid
└── onClick → onEmergencySelect()

// LoadingScreen.js - AI Analysis
├── loadingSteps[] array
├── currentStep state
├── useEffect() → Step progression
└── Animated UI

// TrackingScreen.js - Live Tracking
├── Socket.IO connection
├── Leaflet map setup
├── Real-time location updates
├── AI suggestions display
└── Status cards
```

---

## Data Flow

```
User Action (Click Emergency)
        ↓
App.js (handleEmergencySelect)
        ↓
LoadingScreen (3 seconds)
        ↓
API Call to Backend
        ↓
Backend Processing:
  ├── Score hospitals
  ├── Assign ambulance
  ├── Calculate ETA (ML)
  └── Get AI suggestions
        ↓
Response to Frontend
        ↓
TrackingScreen Displays
        ↓
WebSocket Connection
        ↓
Real-time Updates
        ↓
Ambulance Movement Animation
```

---

## Component Hierarchy

```
<App>
  │
  ├── <Dashboard>
  │     └── Emergency Cards (5)
  │
  ├── <LoadingScreen>
  │     ├── Emergency Badge
  │     ├── Spinner
  │     └── Loading Steps (5)
  │
  └── <TrackingScreen>
        ├── Header (Back button)
        ├── Info Section (4 cards)
        ├── Map Section
        │   ├── <MapContainer>
        │   ├── <TileLayer>
        │   ├── <Marker> × 3
        │   └── <Polyline>
        ├── Details Section (4 cards)
        └── AI Suggestions Section
            ├── Immediate Actions
            ├── Warning Signs
            └── Do Not
```

---

## Styling Architecture

```
Global Styles (index.css)
  ├── Reset
  ├── Body gradient
  └── Font family

Component Styles
  ├── Dashboard.css
  │   ├── Grid layout
  │   ├── Card styles
  │   ├── Hover effects
  │   └── Animations
  │
  ├── LoadingScreen.css
  │   ├── Spinner animation
  │   ├── Step transitions
  │   └── Pulse effects
  │
  └── TrackingScreen.css
      ├── Map container
      ├── Info cards
      ├── Detail cards
      └── Suggestions section
```

---

## Dependencies

### Frontend (package.json)
```json
{
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "react-leaflet": "^4.2.1",
  "leaflet": "^1.9.4",
  "socket.io-client": "^4.6.1",
  "axios": "^1.6.0"
}
```

### Backend (requirements.txt)
```
Flask==3.0.0
Flask-CORS==4.0.0
Flask-SocketIO==5.3.5
scikit-learn==1.3.2
geopy==2.4.1
numpy==1.26.2
pandas==2.1.4
```

---

## API Endpoints

### POST /api/emergency
**Request:**
```json
{
  "type": "Heart Attack",
  "location": {"lat": 12.9716, "lng": 77.5946}
}
```

**Response:**
```json
{
  "emergency_id": "EMG-1234567890",
  "emergency_type": "Heart Attack",
  "severity": "Critical",
  "hospital": {...},
  "ambulance": {...},
  "patient_location": {...},
  "eta": 8,
  "distance": 3.5,
  "ai_suggestions": {...}
}
```

### GET /api/hospitals
Returns array of all hospitals

### GET /api/ambulances
Returns array of all ambulances

---

## WebSocket Events

### Client → Server
- `connect` - Initial connection
- `start_tracking` - Begin ambulance tracking

### Server → Client
- `connected` - Connection confirmed
- `ambulance_update` - Location update (every 0.5s)
- `ambulance_arrived` - Destination reached

---

## Build & Run Commands

### Development
```cmd
# Install
npm install
pip install -r requirements.txt

# Run
python backend/app.py  # Port 5000
npm start              # Port 3000
```

### Production (Future)
```cmd
# Build
npm run build

# Deploy
# Frontend → Static hosting (Netlify, Vercel)
# Backend → Cloud (AWS, Azure, Heroku)
```

---

## File Sizes (Approximate)

```
app.py              ~15 KB  (400+ lines)
Dashboard.js        ~2 KB   (80 lines)
LoadingScreen.js    ~2 KB   (60 lines)
TrackingScreen.js   ~6 KB   (180 lines)
Dashboard.css       ~2 KB   (80 lines)
LoadingScreen.css   ~2 KB   (80 lines)
TrackingScreen.css  ~4 KB   (150 lines)
App.js              ~3 KB   (90 lines)

Total Code: ~36 KB (1500+ lines)
```

---

## Key Algorithms

### Hospital Scoring
```
score = (distance × 2) + (10 - beds_available)
Lower score = Better hospital
```

### ETA Prediction
```
features = [distance/10, traffic_factor, time_of_day]
eta = RandomForestRegressor.predict(features)
```

### Ambulance Movement
```
For each step (20 steps):
  progress = step / total_steps
  new_lat = start_lat + (end_lat - start_lat) × progress
  new_lng = start_lng + (end_lng - start_lng) × progress
  emit update every 0.5 seconds
```

---

## Testing Checklist

- [ ] All files present
- [ ] Dependencies installed
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Dashboard displays correctly
- [ ] Can click emergency type
- [ ] Loading screen animates
- [ ] Tracking screen displays
- [ ] Map loads with markers
- [ ] Ambulance moves in real-time
- [ ] AI suggestions display
- [ ] Can return to dashboard

---

**This structure supports a complete, production-ready emergency response system!** 🚑
