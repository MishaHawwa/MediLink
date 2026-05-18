# 🎨 System Diagrams & Visual Guide

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                         │
│                     (http://localhost:3000)                 │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                    REACT APPLICATION                   │ │
│  │                                                        │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │ │
│  │  │  Dashboard   │→ │LoadingScreen │→ │  Tracking   │ │ │
│  │  │   Screen     │  │   Screen     │  │   Screen    │ │ │
│  │  │              │  │              │  │             │ │ │
│  │  │ 5 Emergency  │  │ AI Analysis  │  │ Live Map +  │ │ │
│  │  │   Buttons    │  │  Animation   │  │ Real-time   │ │ │
│  │  └──────────────┘  └──────────────┘  └─────────────┘ │ │
│  │                                                        │ │
│  │  Libraries:                                            │ │
│  │  • React 18.2.0                                        │ │
│  │  • React-Leaflet (Maps)                                │ │
│  │  • Socket.IO Client (Real-time)                        │ │
│  │  • Axios (HTTP)                                        │ │
│  └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                            ↓ ↑
                    HTTP + WebSocket
                            ↓ ↑
┌─────────────────────────────────────────────────────────────┐
│                      FLASK BACKEND                          │
│                   (http://localhost:5000)                   │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                   API ENDPOINTS                        │ │
│  │                                                        │ │
│  │  POST /api/emergency  ← Handle emergency request      │ │
│  │  GET  /api/hospitals  ← List all hospitals            │ │
│  │  GET  /api/ambulances ← List all ambulances           │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                  DATA LAYER                            │ │
│  │                                                        │ │
│  │  ┌──────────────┐         ┌──────────────┐           │ │
│  │  │  Hospitals   │         │  Ambulances  │           │ │
│  │  │  Database    │         │   Tracker    │           │ │
│  │  │              │         │              │           │ │
│  │  │ • 5 Hospitals│         │ • 5 Ambulances│          │ │
│  │  │ • Specialties│         │ • Locations  │           │ │
│  │  │ • ICU Types  │         │ • Availability│          │ │
│  │  │ • Beds       │         │              │           │ │
│  │  └──────────────┘         └──────────────┘           │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                  AI/ML LAYER                           │ │
│  │                                                        │ │
│  │  ┌──────────────────────────────────────────────┐    │ │
│  │  │     Random Forest Regressor (ETA Model)      │    │ │
│  │  │                                              │    │ │
│  │  │  Input: [distance, traffic, time_of_day]    │    │ │
│  │  │  Output: Predicted ETA in minutes           │    │ │
│  │  │  Training: 100 samples, 50 estimators        │    │ │
│  │  └──────────────────────────────────────────────┘    │ │
│  │                                                        │ │
│  │  ┌──────────────────────────────────────────────┐    │ │
│  │  │     Hospital Scoring Algorithm               │    │ │
│  │  │                                              │    │ │
│  │  │  1. Check required facility (ICU type)       │    │ │
│  │  │  2. Check specialist availability            │    │ │
│  │  │  3. Calculate: distance×2 + (10-beds)        │    │ │
│  │  │  4. Select lowest score                      │    │ │
│  │  └──────────────────────────────────────────────┘    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │              REAL-TIME LAYER (Socket.IO)              │ │
│  │                                                        │ │
│  │  Events:                                               │ │
│  │  • connect          ← Client connects                 │ │
│  │  • start_tracking   ← Begin ambulance tracking        │ │
│  │  • ambulance_update → Send location (every 0.5s)      │ │
│  │  • ambulance_arrived→ Destination reached             │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  Libraries:                                                 │
│  • Flask 3.0.0                                              │
│  • Flask-SocketIO 5.3.5                                     │
│  • scikit-learn 1.3.2                                       │
│  • geopy 2.4.1                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Diagram

```
┌─────────────┐
│    USER     │
│ Clicks      │
│ "Heart      │
│  Attack"    │
└──────┬──────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 1: Capture Location            │
│  • GPS automatically captures        │
│  • Fallback to default if denied     │
│  Location: {lat: 12.9716, lng: 77.5946}│
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 2: Show Loading Screen         │
│  • Display animated AI analysis      │
│  • 5-step progress indicator         │
│  • Duration: 3 seconds               │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 3: API Call to Backend         │
│  POST /api/emergency                 │
│  {                                   │
│    type: "Heart Attack",             │
│    location: {lat, lng}              │
│  }                                   │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 4: Backend Processing          │
│                                      │
│  A. Score All Hospitals              │
│     ┌─────────────────────────┐     │
│     │ For each hospital:      │     │
│     │ 1. Has cardiac ICU? ✓   │     │
│     │ 2. Has cardiologist? ✓  │     │
│     │ 3. Calculate distance   │     │
│     │ 4. Check beds available │     │
│     │ 5. Compute score        │     │
│     └─────────────────────────┘     │
│                                      │
│  B. Select Best Hospital             │
│     CityCare Hospital (Score: 5.2)   │
│                                      │
│  C. Assign Nearest Ambulance         │
│     KA-01-EM-102 (2.3 km away)       │
│                                      │
│  D. Predict ETA (ML Model)           │
│     Input: [2.3, 0.5, 0.6]           │
│     Output: 8 minutes                │
│                                      │
│  E. Get AI Suggestions               │
│     • Immediate actions              │
│     • Warning signs                  │
│     • Do not instructions            │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 5: Return Response             │
│  {                                   │
│    emergency_id: "EMG-1234567890",   │
│    hospital: {...},                  │
│    ambulance: {...},                 │
│    eta: 8,                           │
│    ai_suggestions: {...}             │
│  }                                   │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 6: Display Tracking Screen     │
│  • Show map with 3 markers           │
│  • Display ETA and info              │
│  • Show AI guidance                  │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 7: WebSocket Connection        │
│  • Client emits 'start_tracking'     │
│  • Server begins simulation          │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 8: Real-Time Updates           │
│  Every 0.5 seconds:                  │
│  • Calculate new position            │
│  • Emit 'ambulance_update'           │
│  • Frontend updates marker           │
│  • Smooth animation                  │
└──────┬───────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────┐
│  STEP 9: Arrival                     │
│  • Ambulance reaches hospital        │
│  • Emit 'ambulance_arrived'          │
│  • Update status to "Arrived"        │
└──────────────────────────────────────┘
```

---

## 🧠 Hospital Scoring Algorithm

```
┌─────────────────────────────────────────┐
│  INPUT: Emergency Type + Patient Location│
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│  Get Requirements for Emergency Type    │
│                                         │
│  Heart Attack:                          │
│  • Required Facility: cardiac_icu       │
│  • Required Specialist: cardiologist    │
│  • Severity: Critical                   │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│  For Each Hospital (5 hospitals):       │
└─────────────────┬───────────────────────┘
                  │
                  ↓
         ┌────────┴────────┐
         │                 │
         ↓                 ↓
┌─────────────────┐  ┌─────────────────┐
│ CHECK FACILITY  │  │ CHECK SPECIALIST│
│                 │  │                 │
│ Has cardiac_icu?│  │ Has cardiologist?│
│                 │  │                 │
│ YES → Continue  │  │ YES → Continue  │
│ NO  → Reject    │  │ NO  → Reject    │
└────────┬────────┘  └────────┬────────┘
         │                    │
         └────────┬───────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│  CALCULATE SCORE                        │
│                                         │
│  distance = geodesic(patient, hospital) │
│  distance_score = distance × 2          │
│  bed_score = max(0, 10 - beds_available)│
│                                         │
│  total_score = distance_score + bed_score│
│                                         │
│  Lower score = Better hospital          │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│  EXAMPLE SCORES:                        │
│                                         │
│  CityCare Hospital:                     │
│  • Distance: 2.5 km → 5.0               │
│  • Beds: 15 → 0                         │
│  • Total: 5.0 ✓ BEST                    │
│                                         │
│  MediPlus Hospital:                     │
│  • Distance: 3.2 km → 6.4               │
│  • Beds: 8 → 2                          │
│  • Total: 8.4                           │
│                                         │
│  QuickCare Hospital:                    │
│  • No cardiac ICU → REJECTED            │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│  OUTPUT: Best Hospital Selected         │
│  CityCare Hospital (Score: 5.0)         │
└─────────────────────────────────────────┘
```

---

## 🤖 ML Model Flow

```
┌─────────────────────────────────────────┐
│  TRAINING PHASE (On Server Start)       │
│                                         │
│  Generate Training Data:                │
│  • 100 samples                          │
│  • Features: [distance, traffic, time]  │
│  • Target: actual_time                  │
│                                         │
│  Train Model:                           │
│  • Algorithm: Random Forest             │
│  • Estimators: 50 trees                 │
│  • Random State: 42                     │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│  PREDICTION PHASE (Per Request)         │
│                                         │
│  Input Features:                        │
│  • distance_km / 10 = 0.23              │
│  • traffic_factor = 0.5 (medium)        │
│  • time_of_day = 0.6 (afternoon)        │
│                                         │
│  Model Prediction:                      │
│  features = [[0.23, 0.5, 0.6]]          │
│  eta = model.predict(features)          │
│  eta = max(3, int(eta))  # Min 3 mins   │
│                                         │
│  Output: 8 minutes                      │
└─────────────────────────────────────────┘
```

---

## 🗺️ Map Component Structure

```
<MapContainer center={[lat, lng]} zoom={13}>
  │
  ├─ <TileLayer>
  │    └─ OpenStreetMap tiles
  │
  ├─ <Marker position={patientLocation} icon={patientIcon}>
  │    └─ <Popup>Patient Location</Popup>
  │
  ├─ <Marker position={ambulanceLocation} icon={ambulanceIcon}>
  │    └─ <Popup>Ambulance - {status}</Popup>
  │
  ├─ <Marker position={hospitalLocation} icon={hospitalIcon}>
  │    └─ <Popup>{hospitalName}</Popup>
  │
  └─ <Polyline positions={routeCoordinates} color="#3a86ff">
       └─ Route line connecting all points
```

---

## 🔌 WebSocket Event Flow

```
CLIENT                          SERVER
  │                               │
  │──── connect ──────────────────>│
  │                               │
  │<─── connected ────────────────│
  │     {data: "Connected"}       │
  │                               │
  │──── start_tracking ──────────>│
  │     {emergency_id,            │
  │      ambulance_location,      │
  │      patient_location,        │
  │      hospital_location}       │
  │                               │
  │                               │ Start Background Task
  │                               │ Simulate Movement
  │                               │
  │<─── ambulance_update ─────────│ (Every 0.5s)
  │     {location: {lat, lng},    │
  │      status: "En Route",      │
  │      progress: 25%}           │
  │                               │
  │<─── ambulance_update ─────────│
  │     {location: {lat, lng},    │
  │      status: "En Route",      │
  │      progress: 50%}           │
  │                               │
  │<─── ambulance_update ─────────│
  │     {location: {lat, lng},    │
  │      status: "En Route",      │
  │      progress: 75%}           │
  │                               │
  │<─── ambulance_arrived ────────│
  │     {message: "Arrived"}      │
  │                               │
```

---

## 📱 Screen Flow

```
┌─────────────────────────────────────────┐
│         SCREEN 1: DASHBOARD             │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  🚨 Emergency Response System   │   │
│  │  AI-Powered Hospital Optimization│   │
│  │  ● System Active                │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌──────────┐  ┌──────────┐           │
│  │ ❤️       │  │ 🚗       │           │
│  │ Heart    │  │ Accident │           │
│  │ Attack   │  │          │           │
│  └──────────┘  └──────────┘           │
│                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────┐ │
│  │ 🧠       │  │ 🔥       │  │ 🤰   │ │
│  │ Stroke   │  │ Burns    │  │Preg. │ │
│  └──────────┘  └──────────┘  └──────┘ │
│                                         │
│  📍 Location enabled • 🏥 5 hospitals  │
└─────────────────┬───────────────────────┘
                  │ Click Emergency
                  ↓
┌─────────────────────────────────────────┐
│      SCREEN 2: LOADING/ANALYSIS         │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │  ● Heart Attack                 │   │
│  └─────────────────────────────────┘   │
│                                         │
│         ⭕ Loading Spinner               │
│                                         │
│  ✓ Analyzing your location...          │
│  ✓ Scanning nearby hospitals...        │
│  ⭕ Checking ICU availability...        │
│  ○ Assigning nearest ambulance...      │
│  ○ AI optimizing route...              │
│                                         │
│  Please wait while we find the best    │
│  hospital for you...                   │
└─────────────────┬───────────────────────┘
                  │ 3 seconds
                  ↓
┌─────────────────────────────────────────┐
│       SCREEN 3: LIVE TRACKING           │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │Heart │ │Critic│ │CityCa│ │ 8    │  │
│  │Attack│ │ al   │ │ re   │ │ mins │  │
│  └──────┘ └──────┘ └──────┘ └──────┘  │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │         🗺️ MAP VIEW             │   │
│  │                                 │   │
│  │  🏥 Hospital (green)            │   │
│  │         ↑                       │   │
│  │         │ Route line            │   │
│  │         │                       │   │
│  │  🚑 Ambulance (blue, moving)    │   │
│  │         ↑                       │   │
│  │         │                       │   │
│  │  🤕 Patient (red)               │   │
│  └─────────────────────────────────┘   │
│                                         │
│  🚑 KA-01-EM-102  📍 En Route          │
│  ✅ Hospital Prepared  📏 3.5 km       │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ 🤖 AI Emergency Guidance        │   │
│  │ ⚡ Immediate Actions             │   │
│  │ ⚠️ Warning Signs                │   │
│  │ 🚫 Do NOT                       │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

## 🎨 Color Scheme

```
Emergency Types:
├─ Heart Attack:    #ff4757 (Red)
├─ Accident:        #ffa502 (Orange)
├─ Stroke:          #ff6348 (Coral)
├─ Burns:           #ff7f50 (Orange-Red)
└─ Pregnancy:       #ff6b9d (Pink)

Map Markers:
├─ Patient:         #ff4757 (Red)
├─ Ambulance:       #3a86ff (Blue)
└─ Hospital:        #2ecc71 (Green)

UI Elements:
├─ Primary:         #667eea (Purple)
├─ Secondary:       #764ba2 (Dark Purple)
├─ Success:         #2ecc71 (Green)
├─ Warning:         #ffa502 (Orange)
└─ Danger:          #ff4757 (Red)
```

---

**This visual guide helps understand the complete system architecture!** 🎨
