# ============================================================
# Customer fedback formatter
# Teaching: Built-in String Methods & String Formating
# =============================================================

raw_name = input("Enter customer name: ")
raw_feedback = input("Enter feedback message: ")
rating = input("Enter rating (1 to 5): ")

clean_name = raw_name.strip()
clean_feedback = raw_feedback.strip()

formatted_name = clean_name.title()

formatted_feedback = clean_feedback.capitalize()

formatted_feedback = formatted_feedback.replace("u","you").replace("r","are")
                    

exclamation_count = formatted_feedback.count("!")

if int(rating) >= 4:
    category = "POSITIVE".upper()
else:
    category = "NEEDS REVIEW".upper()

print("\n" + "=" * 45)
print(f"{'PROFESSIONAL FEEDBACK REPORT': ^45}")
print("=" * 45)

print(f"Customer Name : {formatted_name}")
print(f"Rating        : {rating} / 5 Stard")
print(f"Category      : [{category}]")
print(f"Excitement    : {exclamation_count} exclamation mark(s)")
print("-" * 45)
print("Formatted Massage:")
print(f'"{formatted_feedback}"')
print("=" * 45)


