# # from django.shortcuts import render

# # def home(request):
# #     return render(request, "index.html")

# import requests
# from django.shortcuts import render

# def home(request):
#     result = None

#     if request.method == "POST":
#         engine_size = request.POST.get("engine_size")
#         cylinders = request.POST.get("cylinders")
#         fuel = request.POST.get("fuel_consumption_comb")

#         response = requests.post(
#             "http://127.0.0.1:8000/predict",
#             json={
#                 "engine_size": float(engine_size),
#                 "cylinders": int(cylinders),
#                 "fuel_consumption_comb": float(fuel)
#             }
#         )

  

#         if response.status_code == 200:
#             result = response.json().get("CO2_Emission_Prediction")

#     return render(request, "index.html", {"result": result})



import requests
from django.shortcuts import render

def home(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            engine_size = float(request.POST.get("engine_size"))
            cylinders = int(request.POST.get("cylinders"))
            fuel = float(request.POST.get("fuel_consumption_comb"))
            response = requests.post(
                "http://127.0.0.1:8001/predict",
                json={
                    "engine_size": engine_size,
                    "cylinders": cylinders,
                    "fuel_consumption_comb": fuel
                },
                timeout=5
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)

            if response.status_code == 200:
                result = response.json().get("CO2_Emission_Prediction")
            else:
                error = "API Error"

        except Exception as e:
            print("ERROR:", e)
            error = str(e)

    return render(request, "index.html", {"result": result, "error": error})