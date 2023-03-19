def validate(heightF, heightI, weight):
    heightValid = False
    weightValid = False
    try: 
        heightF = float(heightF) * 12
        heightI = float(heightI)

        if heightF >= 0 and heightI >= 0 and heightI < 12:
            height = heightF + heightI
            
            if height > 0:
                heightValid = True

    except ValueError:
        heightValid = False

    try: 
        weight = float(weight)
        if weight > 0:
            weightValid = True

    except ValueError:
        weightValid = False
    
    return heightValid, weightValid
    

def bmiCalculator(height, weight):
    height_metric = height * 0.025
    weight_metric = weight * 0.45
    if height_metric <= 0 or weight_metric <= 0:
        return 0.0

    return round(weight_metric / (height_metric * height_metric), 1)

def categorize(bmi):
    if bmi < .1:
        category = "Error"
    elif bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return category


