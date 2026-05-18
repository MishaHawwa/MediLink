import React, { useState, useEffect } from 'react';
import './LoadingScreen.css';

const loadingSteps = [
  { text: '📍 Analyzing your location...', duration: 1000 },
  { text: '🏥 Scanning nearby hospitals...', duration: 1000 },
  { text: '🔍 Checking ICU availability...', duration: 800 },
  { text: '🚑 Assigning nearest ambulance...', duration: 700 },
  { text: '🤖 AI optimizing route...', duration: 500 }
];

function LoadingScreen({ emergencyType }) {
  const [currentStep, setCurrentStep] = useState(0);

  useEffect(() => {
    if (currentStep < loadingSteps.length) {
      const timer = setTimeout(() => {
        setCurrentStep(currentStep + 1);
      }, loadingSteps[currentStep].duration);
      return () => clearTimeout(timer);
    }
  }, [currentStep]);

  return (
    <div className="loading-screen">
      <div className="loading-container">
        <div className="emergency-badge">
          <span className="pulse-dot"></span>
          {emergencyType}
        </div>
        
        <div className="loading-spinner">
          <div className="spinner"></div>
        </div>

        <div className="loading-steps">
          {loadingSteps.map((step, index) => (
            <div 
              key={index}
              className={`loading-step ${index <= currentStep ? 'active' : ''} ${index < currentStep ? 'completed' : ''}`}
            >
              <div className="step-icon">
                {index < currentStep ? '✓' : '○'}
              </div>
              <div className="step-text">{step.text}</div>
            </div>
          ))}
        </div>

        <div className="loading-message">
          <p>Please wait while we find the best hospital for you...</p>
        </div>
      </div>
    </div>
  );
}

export default LoadingScreen;
