signal = input("Enter the traffic signal color (Red, Yellow, Green): ").lower()


if signal == "red":
    print("🔴 STOP! ")

elif signal == "yellow":
    print("🟡 READY! ")

elif signal == "green":
    print("🟢 GO! ")

else:
    print("❌ Invalid signal color! Please enter Red, Yellow, or Green.")