document.getElementById("calcBtn").addEventListener("click", async () => {
  const payload = {
    bhk: parseInt(document.getElementById("bhk").value),
    area_sqft: parseFloat(document.getElementById("area").value),
    city_zone: document.getElementById("zone").value,
    furnishing: document.getElementById("furnishing").value,
    floor_no: parseInt(document.getElementById("floor").value)
  };

  try {
    const res = await fetch("http://127.0.0.1:8000/predict-rent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error("API call failed");
    const data = await res.json();

    document.getElementById("resRent").textContent = data.formatted_rent;
    document.getElementById("resDeposit").textContent = data.estimated_deposit;
    document.getElementById("resZone").textContent = data.zone_tier;
    document.getElementById("zoneBadge").textContent = data.zone_tier.toUpperCase();
  } catch (err) {
    alert("FastAPI backend not running. Start with: uvicorn src.api.main:app --reload");
  }
});
