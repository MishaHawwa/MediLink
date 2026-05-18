import React from 'react';
import './Dashboard.css';

const emergencies = [
  { 
    type: 'Heart Attack', 
    icon: '❤️', 
    color: '#ff4757',
    description: 'Cardiac emergency'
  },
  { 
    type: 'Accident', 
    icon: '🚗', 
    color: '#ffa502',
    description: 'Traffic accident or injury'
  },
  { 
    type: 'Stroke', 
    icon: '🧠', 
    color: '#ff6348',
    description: 'Neurological emergency'
  },
  { 
    type: 'Burns', 
    icon: '🔥', 
    color: '#ff7f50',
    description: 'Burn injuries'
  },
  { 
    type: 'Pregnancy Emergency', 
    icon: '🤰', 
    color: '#ff6b9d',
    description: 'Maternity emergency'
  }
];

function Dashboard({ onEmergencySelect }) {
  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>🚨 Emergency Response System</h1>
        <p className="subtitle">AI-Powered Hospital Optimization</p>
        <div className="status-badge">
          <span className="status-dot"></span>
          System Active
        </div>
      </div>

      <div className="emergency-grid">
        {emergencies.map((emergency) => (
          <div
            key={emergency.type}
            className="emergency-card"
            style={{ borderColor: emergency.color }}
            onClick={() => onEmergencySelect(emergency.type)}
          >
            <div className="emergency-icon" style={{ color: emergency.color }}>
              {emergency.icon}
            </div>
            <h3>{emergency.type}</h3>
            <p>{emergency.description}</p>
            <button 
              className="emergency-button"
              style={{ backgroundColor: emergency.color }}
            >
              Request Emergency
            </button>
          </div>
        ))}
      </div>

      <div className="dashboard-footer">
        <p>📍 Location tracking enabled • 🏥 Connected to 5 hospitals • 🚑 5 ambulances available</p>
      </div>
    </div>
  );
}

export default Dashboard;
