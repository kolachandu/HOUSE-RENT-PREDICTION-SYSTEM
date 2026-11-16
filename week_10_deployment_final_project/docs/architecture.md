# System Architecture - House Rent Prediction System

```
[Property CSV Records] ---> [Sanitization & Valuation Matrix] ---> [Rental Pricing Model]
                                                                        |
                                                                        v
[Tenant / Landlord UI] <---> [FastAPI Endpoints (/predict-rent)]
```
