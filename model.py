def dessert_choice_message(user_choice):
    if user_choice == "Cheesecake":
        return "Link to an easy recipe for cheesecake "
    elif user_choice == "Donut":
        return "Link to an easy recipe for donuts "
    elif user_choice == "Caramel Apple":
        return "Link to an easy recipe for caramel apples "

def link_dessert(user_choice):
    if user_choice == "Cheesecake":
        return "https://www.kingarthurbaking.com/recipes/easy-cheesecake-recipe"
    elif user_choice == "Donut":
        return "https://www.cookingclassy.com/15-minute-donuts-from-scratch/"
    elif user_choice == "Caramel Apple":
        return "https://foodschmooze.org/recipe/candy-apples/"

def title(user_choice):
    if user_choice == "Cheesecake":
        return "Cheesecake Recipe"
    elif user_choice == "Donut":
        return "Donut Recipe"
    elif user_choice == "Caramel Apple":
        return "Caramel Apple Recipe"

def picture(user_choice):
    if user_choice == "Cheesecake":
        return "https://sugarspunrun.com/wp-content/uploads/2019/01/Best-Cheesecake-Recipe-2-1-of-1-4.jpg"
    elif user_choice == "Donut":
        return "https://tornadoughalli.com/wp-content/uploads/2020/03/CHOCOLATE-GLAZED-DONUTS-12.jpg"
    elif user_choice == "Caramel Apple":
        return "https://foodschmooze.org/wp-content/uploads/2017/08/candy-apples_recipe_credit-Kylie-Tefft-300x300.jpg"



    