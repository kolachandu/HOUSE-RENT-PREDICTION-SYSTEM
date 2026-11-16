# HOUSE RENT PREDICTION SYSTEM - Week 10 - Deployment & Final Project

## Goal
Package, containerize, and finalize the complete project for academic submission and deployment.

## Final Deliverables Included
- Complete end-to-end dataset pipeline (raw & processed).
- Production-ready core business logic & analytical engine.
- FastAPI backend REST service with validated endpoints.
- Modern responsive HTML5/CSS3/JavaScript web dashboard.
- Automated test suite validating data structures, edge cases, and inference.
- Production containerization Dockerfile.
- Comprehensive Final Project Report & Architecture documentation.

## Step-by-Step Local Execution
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run data pipeline:
   ```bash
   python src/preprocessing/clean_data.py
   ```
3. Execute unit test suite:
   ```bash
   python -m unittest discover tests
   ```
4. Start the backend service:
   ```bash
   uvicorn src.api.main:app --reload
   ```
5. Open `frontend/index.html` in your web browser.
6. Test end-to-end features.

## Backend API Endpoints
```text
GET  http://127.0.0.1:8000/properties
POST http://127.0.0.1:8000/predict-rent
```

## Docker Container Deployment
```bash
docker build -f deployment/Dockerfile -t proj03-house-rent-prediction-system .
docker run -p 8000:8000 proj03-house-rent-prediction-system
```

## Student Submission Checklist
- [ ] Data preprocessing runs cleanly
- [ ] All unit tests pass (`python -m unittest discover tests`)
- [ ] FastAPI backend starts without errors
- [ ] Frontend dashboard submits and renders live API responses
- [ ] `docs/final_report.md` updated with student reflections

## Viva Voce Examination Questions & Answers
### Q1: Which factor exerts the highest weight on monthly rent?
**Answer:** Square footage and geographic city zone (Downtown commands 1.45x premium).

### Q2: How is the security deposit calculated?
**Answer:** Standard lease convention of 3 times the predicted monthly rent.

### Q3: Why is Mean Absolute Percentage Error (MAPE) used?
**Answer:** Because rent values range from INR 8,000 to INR 70,000; percentage error provides an intuitive normalized metric.

### Q4: How does floor height affect rent?
**Answer:** Higher floors in high-rise buildings often provide better views and less noise, adding an incremental floor bonus.

### Q5: What future extensions would you recommend?
**Answer:** Incorporating proximity to metro stations and building amenities (gym, swimming pool).

