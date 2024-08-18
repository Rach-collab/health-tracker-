def input_calories():
    intake = 0
    while True:
        food = input("Enter food item (or 'done' to finish): ")
        if food.lower() == 'done':
            break
        calories = int(input(f"Enter calories for {food}: "))
        intake += calories
    return intake

def input_activities():
    burned = 0
    while True:
        activity = input("Enter activity (or 'done' to finish): ")
        if activity.lower() == 'done':
            break
        duration = int(input(f"Enter duration (in minutes) for {activity}: "))
        # Example burn rate
        burned += duration * 10
    return burned

def calculate_net_calories(intake, burned):
    return intake - burned

def give_feedback(net_calories):
    if net_calories > 0:
        print(f"You have a net calorie intake of {net_calories} calories. This suggests a calorie surplus, which may lead to weight gain.")
    elif net_calories < 0:
        print(f"You have a net calorie deficit of {-net_calories} calories. This suggests a calorie deficit, which may lead to weight loss.")
    else:
        print("You have balanced your calorie intake and burn. You are maintaining your weight.")

def main():
    intake = input_calories()
    burned = input_activities()
    net_calories = calculate_net_calories(intake, burned)
    give_feedback(net_calories)

if __name__ == "__main__":
    main()
