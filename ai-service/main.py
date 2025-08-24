"""
ZİRAVE AI Service - Agricultural Intelligence Platform
FastAPI service for plant diagnostics and agricultural recommendations
"""

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import os
from datetime import datetime
import json

# Initialize FastAPI app
app = FastAPI(
    title="ZİRAVE AI Service",
    description="Agricultural Intelligence Platform - Plant Diagnostics and Recommendations",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class DiagnosisRequest(BaseModel):
    plant_type: Optional[str] = None
    symptoms: Optional[List[str]] = None
    location: Optional[str] = None
    season: Optional[str] = None

class DiagnosisResponse(BaseModel):
    diagnosis_id: str
    plant_type: str
    detected_issues: List[Dict[str, Any]]
    recommendations: List[Dict[str, Any]]
    confidence: float
    timestamp: str

class HealthResponse(BaseModel):
    status: str
    message: str
    version: str
    timestamp: str

# Mock data for development
MOCK_PLANT_DISEASES = {
    "domates": {
        "common_diseases": [
            {
                "name": "Alternaria Yaprak Lekesi",
                "symptoms": ["kahverengi lekeler", "yaprak sararması", "yaprak dökülmesi"],
                "treatment": "Fungisit uygulaması ve sulama düzeni",
                "confidence": 0.85
            },
            {
                "name": "Fusarium Solgunluğu",
                "symptoms": ["yaprak sararması", "gövde çürümesi", "bitki ölümü"],
                "treatment": "Toprak dezenfeksiyonu ve dayanıklı çeşit kullanımı",
                "confidence": 0.78
            }
        ]
    },
    "salatalik": {
        "common_diseases": [
            {
                "name": "Külleme Hastalığı",
                "symptoms": ["beyaz toz tabaka", "yaprak deformasyonu"],
                "treatment": "Havalandırma artırımı ve fungisit",
                "confidence": 0.92
            }
        ]
    }
}

MOCK_RECOMMENDATIONS = [
    {
        "type": "watering",
        "title": "Sulama Önerisi",
        "description": "Günde 2-3 kez, sabah ve akşam saatlerinde sulayın",
        "priority": "high"
    },
    {
        "type": "fertilizer",
        "title": "Gübre Önerisi", 
        "description": "Azot oranı yüksek gübre kullanın",
        "priority": "medium"
    },
    {
        "type": "pest_control",
        "title": "Zararlı Kontrolü",
        "description": "Organik insektisit uygulaması yapın",
        "priority": "low"
    }
]

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="ZİRAVE AI Service is running successfully!",
        version="1.0.0",
        timestamp=datetime.now().isoformat()
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check"""
    return HealthResponse(
        status="healthy",
        message="All systems operational",
        version="1.0.0",
        timestamp=datetime.now().isoformat()
    )

@app.post("/diagnose", response_model=DiagnosisResponse)
async def diagnose_plant(request: DiagnosisRequest):
    """
    Diagnose plant diseases and provide recommendations
    This is a mock implementation - will be replaced with actual AI models
    """
    try:
        # Generate mock diagnosis ID
        diagnosis_id = f"diag_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Determine plant type
        plant_type = request.plant_type or "domates"  # Default to tomato
        plant_key = plant_type.lower().replace(" ", "")
        
        # Get mock diseases for the plant type
        plant_diseases = MOCK_PLANT_DISEASES.get(plant_key, MOCK_PLANT_DISEASES["domates"])
        
        # Select a random disease (in real implementation, this would be AI-based)
        detected_issues = plant_diseases["common_diseases"][:1]  # Take first disease
        
        # Generate recommendations
        recommendations = MOCK_RECOMMENDATIONS
        
        return DiagnosisResponse(
            diagnosis_id=diagnosis_id,
            plant_type=plant_type,
            detected_issues=detected_issues,
            recommendations=recommendations,
            confidence=0.87,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Diagnosis failed: {str(e)}")

@app.post("/diagnose/image")
async def diagnose_from_image(
    file: UploadFile = File(...),
    plant_type: Optional[str] = None
):
    """
    Diagnose plant diseases from uploaded image
    This is a placeholder - will implement actual image processing
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # In real implementation, we would:
        # 1. Process the image with AI model
        # 2. Extract features and detect diseases
        # 3. Generate confidence scores
        
        # For now, return mock response
        diagnosis_id = f"img_diag_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        return {
            "diagnosis_id": diagnosis_id,
            "plant_type": plant_type or "Bilinmeyen Bitki",
            "detected_issues": [
                {
                    "name": "Yaprak Lekesi Hastalığı",
                    "symptoms": ["kahverengi lekeler", "yaprak sararması"],
                    "treatment": "Fungisit uygulaması önerilir",
                    "confidence": 0.82
                }
            ],
            "recommendations": MOCK_RECOMMENDATIONS,
            "confidence": 0.82,
            "timestamp": datetime.now().isoformat(),
            "image_processed": True,
            "image_size": f"{file.size} bytes" if file.size else "unknown"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image diagnosis failed: {str(e)}")

@app.get("/plants/diseases")
async def get_plant_diseases():
    """Get list of known plant diseases"""
    return {
        "diseases": MOCK_PLANT_DISEASES,
        "total_plants": len(MOCK_PLANT_DISEASES),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/recommendations/types")
async def get_recommendation_types():
    """Get available recommendation types"""
    return {
        "types": ["watering", "fertilizer", "pest_control", "pruning", "harvesting"],
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    # Get port from environment or default to 8000
    port = int(os.getenv("PORT", 8000))
    
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,  # Enable auto-reload in development
        log_level="info"
    )