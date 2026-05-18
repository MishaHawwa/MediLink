from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import random
import time
from datetime import datetime
import math
from geopy.distance import geodesic
import numpy as np
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Sample hospital database
hospitals = [
    {
        "id": 1,
        "name": "CityCare Hospital",
        "location": {"lat": 12.9716, "lng": 77.5946},
        "cardiac_icu": True,
        "neuro_icu": True,
        "trauma_center": True,
        "burn_unit": True,
        "maternity_ward": True,
        "beds_available": 15,
        "specialists": ["cardiologist", "neurologist", "trauma", "burn", "obstetrician"]
    },
    {
        "id": 2,
        "name": "MediPlus Hospital",
        "location": {"lat": 12.9352, "lng": 77.6245},
        "cardiac_icu": True,
        "neuro_icu": False,
        "trauma_center": True,
        "burn_unit": False,
        "maternity_ward": True,
        "beds_available": 8,
        "specialists": ["cardiologist", "trauma", "obstetrician"]
    },
    {
        "id": 3,
        "name": "LifeLine Medical Center",
        "location": {"lat": 12.9141, "lng": 77.6411},
        "cardiac_icu": False,
        "neuro_icu": True,
        "trauma_center": True,
        "burn_unit": True,
        "maternity_ward": False,
        "beds_available": 12,
        "specialists": ["neurologist", "trauma", "burn"]
    },
    {
        "id": 4,
        "name": "Apollo Emergency Care",
        "location": {"lat": 13.0358, "lng": 77.5970},
        "cardiac_icu": True,
        "neuro_icu": True,
        "trauma_center": True,
        "burn_unit": True,
        "maternity_ward": True,
        "beds_available": 20,
        "specialists": ["cardiologist", "neurologist", "trauma", "burn", "obstetrician"]
    },
    {
        "id": 5,
        "name": "QuickCare Hospital",
        "location": {"lat": 12.8956, "lng": 77.6362},
        "cardiac_icu": False,
        "neuro_icu": False,
        "trauma_center": True,
        "burn_unit": False,
        "maternity_ward": True,
        "beds_available": 5,
        "specialists": ["trauma", "obstetrician"]
    }
]

# Sample ambulance database
ambulances = [
    {"id": "KA-01-EM-101", "location": {"lat": 12.9716, "lng": 77.5946}, "available": True},
    {"id": "KA-01-EM-102", "location": {"lat": 12.9352, "lng": 77.6245}, "available": True},
    {"id": "KA-01-EM-103", "location": {"lat": 12.9141, "lng": 77.6411}, "available": True},
    {"id": "KA-01-EM-104", "location": {"lat": 13.0358, "lng": 77.5970}, "available": True},
    {"id": "KA-01-EM-105", "location": {"lat": 12.8956, "lng": 77.6362}, "available": True}
]

# Emergency type requirements mapping
emergency_requirements = {
    "Heart Attack": {
        "severity": "Critical",
        "required_facility": "cardiac_icu",
        "required_specialist": "cardiologist",
        "priority_score": 10
    },
    "Stroke": {
        "severity": "Critical",
        "required_facility": "neuro_icu",
        "required_specialist": "neurologist",
        "priority_score": 10
    },
    "Accident": {
        "severity": "High",
        "required_facility": "trauma_center",
        "required_specialist": "trauma",
        "priority_score": 8
    },
    "Burns": {
        "severity": "High",
        "required_facility": "burn_unit",
        "required_specialist": "burn",
        "priority_score": 8
    },
    "Pregnancy Emergency": {
        "severity": "High",
        "required_facility": "maternity_ward",
        "required_specialist": "obstetrician",
        "priority_score": 9
    }
}

# AI suggestions for each emergency type
ai_suggestions = {
    "Heart Attack": {
        "immediate_actions": [
            "Call emergency services immediately (already done)",
            "Have the patient sit down and rest in a comfortable position",
            "If available, give aspirin (300mg) to chew slowly",
            "Loosen any tight clothing around neck and chest",
            "Stay calm and reassure the patient",
            "If patient becomes unconscious, prepare for CPR"
        ],
        "warning_signs": [
            "Chest pain or discomfort",
            "Pain in arms, neck, jaw, or back",
            "Shortness of breath",
            "Cold sweat, nausea"
        ],
        "do_not": [
            "Do not leave the patient alone",
            "Do not give food or water",
            "Do not wait to see if symptoms go away"
        ]
    },
    "Stroke": {
        "immediate_actions": [
            "Note the time when symptoms first appeared",
            "Keep the patient calm and lying down with head slightly elevated",
            "Do not give any food, drinks, or medication",
            "Loosen tight clothing",
            "Check if patient can smile, raise both arms, speak clearly (FAST test)",
            "Monitor breathing and consciousness"
        ],
        "warning_signs": [
            "Face drooping on one side",
            "Arm weakness or numbness",
            "Speech difficulty or slurred speech",
            "Sudden confusion or trouble seeing"
        ],
        "do_not": [
            "Do not give aspirin (unlike heart attack)",
            "Do not give food or water",
            "Do not let patient sleep"
        ]
    },
    "Accident": {
        "immediate_actions": [
            "Ensure scene safety before approaching",
            "Do not move the patient unless in immediate danger",
            "Control any visible bleeding with direct pressure",
            "Keep the patient still, especially if spinal injury suspected",
            "Cover the patient to prevent shock",
            "Monitor breathing and consciousness"
        ],
        "warning_signs": [
            "Severe bleeding",
            "Unconsciousness",
            "Difficulty breathing",
            "Suspected broken bones or spinal injury"
        ],
        "do_not": [
            "Do not move patient if spinal injury suspected",
            "Do not remove embedded objects",
            "Do not give food or water"
        ]
    },
    "Burns": {
        "immediate_actions": [
            "Remove patient from heat source safely",
            "Cool the burn with cool (not ice-cold) running water for 10-20 minutes",
            "Remove jewelry and tight clothing before swelling starts",
            "Cover burn with clean, dry cloth or sterile dressing",
            "Do not apply ice, butter, or ointments",
            "Keep patient warm to prevent shock"
        ],
        "warning_signs": [
            "Burns larger than 3 inches",
            "Burns on face, hands, feet, or genitals",
            "Third-degree burns (white or charred skin)",
            "Chemical or electrical burns"
        ],
        "do_not": [
            "Do not apply ice directly",
            "Do not break blisters",
            "Do not apply butter, oil, or ointments"
        ]
    },
    "Pregnancy Emergency": {
        "immediate_actions": [
            "Keep the mother calm and comfortable",
            "Position her on her left side if possible",
            "Do not give food or water",
            "Monitor contractions (frequency and duration)",
            "Check for bleeding or fluid leakage",
            "Prepare for possibility of delivery en route"
        ],
        "warning_signs": [
            "Severe abdominal pain",
            "Heavy bleeding",
            "Water breaking",
            "Contractions less than 5 minutes apart",
            "Decreased fetal movement"
        ],
        "do_not": [
            "Do not panic - stay calm",
            "Do not give medications without medical advice",
            "Do not attempt to delay delivery if imminent"
        ]
    }
}

# Simple ETA prediction function (replaces ML model for simplicity)
def predict_eta(distance_km, traffic_factor=0.5, time_of_day=0.5):
    """Predict ETA using simple calculation"""
    # Base time: 2 minutes per km
    base_time = distance_km * 2
    
    # Add traffic factor (0.5 = normal, 1.0 = heavy traffic)
    traffic_adjustment = base_time * traffic_factor * 0.5
    
    # Add time of day factor (rush hour adjustment)
    time_adjustment = base_time * time_of_day * 0.3
    
    total_time = base_time + traffic_adjustment + time_adjustment
    
    return max(3, int(total_time))  # Minimum 3 minutes

def calculate_distance(loc1, loc2):
    """Calculate distance between two coordinates in km"""
    return geodesic((loc1['lat'], loc1['lng']), (loc2['lat'], loc2['lng'])).km

def predict_eta(distance_km, traffic_factor=0.5, time_of_day=0.5):
    """Predict ETA using simple calculation"""
    # Base time: 2 minutes per km
    base_time = distance_km * 2
    
    # Add traffic factor (0.5 = normal, 1.0 = heavy traffic)
    traffic_adjustment = base_time * traffic_factor * 0.5
    
    # Add time of day factor (rush hour adjustment)
    time_adjustment = base_time * time_of_day * 0.3
    
    total_time = base_time + traffic_adjustment + time_adjustment
    
    return max(3, int(total_time))  # Minimum 3 minutes

def score_hospital(hospital, emergency_type, patient_location):
    """Score hospital based on multiple factors"""
    requirements = emergency_requirements.get(emergency_type, {})
    
    # Check if hospital has required facility
    required_facility = requirements.get('required_facility')
    if not hospital.get(required_facility, False):
        return -1  # Hospital not suitable
    
    # Check if hospital has required specialist
    required_specialist = requirements.get('required_specialist')
    if required_specialist not in hospital.get('specialists', []):
        return -1  # Hospital not suitable
    
    # Calculate distance
    distance = calculate_distance(patient_location, hospital['location'])
    
    # Calculate score (lower is better)
    # Factors: distance, bed availability, priority
    distance_score = distance * 2
    bed_score = max(0, 10 - hospital['beds_available'])
    
    total_score = distance_score + bed_score
    
    return total_score

@app.route('/api/emergency', methods=['POST'])
def handle_emergency():
    data = request.json
    emergency_type = data.get('type')
    patient_location = data.get('location')
    
    # Find best hospital
    suitable_hospitals = []
    for hospital in hospitals:
        score = score_hospital(hospital, emergency_type, patient_location)
        if score >= 0:  # Hospital is suitable
            distance = calculate_distance(patient_location, hospital['location'])
            suitable_hospitals.append({
                'hospital': hospital,
                'score': score,
                'distance': distance
            })
    
    if not suitable_hospitals:
        return jsonify({'error': 'No suitable hospital found'}), 404
    
    # Sort by score (lower is better)
    suitable_hospitals.sort(key=lambda x: x['score'])
    best_hospital = suitable_hospitals[0]['hospital']
    
    # Find nearest available ambulance
    available_ambulances = [a for a in ambulances if a['available']]
    if not available_ambulances:
        return jsonify({'error': 'No ambulance available'}), 404
    
    nearest_ambulance = min(
        available_ambulances,
        key=lambda a: calculate_distance(patient_location, a['location'])
    )
    
    # Mark ambulance as unavailable
    nearest_ambulance['available'] = False
    
    # Calculate ETA
    distance_to_patient = calculate_distance(nearest_ambulance['location'], patient_location)
    distance_to_hospital = calculate_distance(patient_location, best_hospital['location'])
    
    eta_to_patient = predict_eta(distance_to_patient)
    eta_to_hospital = predict_eta(distance_to_hospital)
    total_eta = eta_to_patient + eta_to_hospital
    
    # Get emergency details
    emergency_details = emergency_requirements.get(emergency_type, {})
    
    # Get AI suggestions
    suggestions = ai_suggestions.get(emergency_type, {})
    
    response = {
        'emergency_id': f"EMG-{int(time.time())}",
        'emergency_type': emergency_type,
        'severity': emergency_details.get('severity', 'High'),
        'hospital': {
            'id': best_hospital['id'],
            'name': best_hospital['name'],
            'location': best_hospital['location'],
            'beds_available': best_hospital['beds_available']
        },
        'ambulance': {
            'id': nearest_ambulance['id'],
            'location': nearest_ambulance['location']
        },
        'patient_location': patient_location,
        'eta': total_eta,
        'distance': round(distance_to_hospital, 2),
        'ai_suggestions': suggestions,
        'rejected_hospitals': [
            {
                'name': h['hospital']['name'],
                'reason': 'Missing required facility or specialist'
            }
            for h in suitable_hospitals[1:3]
        ] if len(suitable_hospitals) > 1 else []
    }
    
    return jsonify(response)

@app.route('/api/hospitals', methods=['GET'])
def get_hospitals():
    return jsonify(hospitals)

@app.route('/api/ambulances', methods=['GET'])
def get_ambulances():
    return jsonify(ambulances)

# WebSocket for live tracking
@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('connected', {'data': 'Connected to server'})

@socketio.on('start_tracking')
def handle_tracking(data):
    emergency_id = data.get('emergency_id')
    ambulance_location = data.get('ambulance_location')
    patient_location = data.get('patient_location')
    hospital_location = data.get('hospital_location')
    
    # Simulate ambulance movement
    def simulate_movement():
        current_location = ambulance_location.copy()
        
        # First move to patient
        steps = 20
        for i in range(steps):
            progress = (i + 1) / steps
            current_location['lat'] = ambulance_location['lat'] + (patient_location['lat'] - ambulance_location['lat']) * progress
            current_location['lng'] = ambulance_location['lng'] + (patient_location['lng'] - ambulance_location['lng']) * progress
            
            socketio.emit('ambulance_update', {
                'emergency_id': emergency_id,
                'location': current_location.copy(),
                'status': 'En Route to Patient',
                'progress': progress * 50  # 0-50%
            })
            socketio.sleep(0.5)
        
        # Then move to hospital
        for i in range(steps):
            progress = (i + 1) / steps
            current_location['lat'] = patient_location['lat'] + (hospital_location['lat'] - patient_location['lat']) * progress
            current_location['lng'] = patient_location['lng'] + (hospital_location['lng'] - patient_location['lng']) * progress
            
            socketio.emit('ambulance_update', {
                'emergency_id': emergency_id,
                'location': current_location.copy(),
                'status': 'En Route to Hospital',
                'progress': 50 + progress * 50  # 50-100%
            })
            socketio.sleep(0.5)
        
        socketio.emit('ambulance_arrived', {
            'emergency_id': emergency_id,
            'message': 'Ambulance arrived at hospital'
        })
    
    socketio.start_background_task(simulate_movement)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
