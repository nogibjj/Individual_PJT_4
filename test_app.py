from app import parse_food

def test():
    example_resposne = """Absolutely! Congratulations on your happiness! Here are some popular and delicious options for delivery food menus that you can consider for your party:

Pizza Party:

Choose from a variety of pizzas with different toppings to cater to everyone's preferences.
Consider adding some sides like garlic bread, chicken wings, or salads.
Mexican Fiesta:

Order a selection of tacos, burritos, and quesadillas.
Include sides such as guacamole, salsa, and nachos with cheese.
Asian Fusion:

Sushi platters with a mix of rolls and sashimi.
Add some Chinese favorites like spring rolls, dumplings, and sweet and sour chicken.
Mediterranean Feast:

Gyros or kebabs with a variety of meats and veggies.
Include hummus, tzatziki, and a selection of fresh salads.
Burger Bash:

Gourmet burgers with different toppings and sauces.
Don't forget to add some fries or onion rings on the side.
Italian Indulgence:

Pasta dishes with a choice of sauces (marinara, Alfredo, pesto).
Consider ordering a variety of appetizers like bruschetta or stuffed mushrooms.
BBQ Bonanza:

Ribs, pulled pork, or brisket with barbecue sauce.
Include classic BBQ sides like coleslaw, baked beans, and cornbread.
Vegetarian Delight:

Veggie wraps or sandwiches with a variety of fillings.
Order vegetarian sushi rolls or a selection of meat-free appetizers.
Dessert Extravaganza:

Cupcakes, cookies, and brownies for a sweet treat.
Consider getting a variety of desserts to satisfy different tastes.
Healthy Options:

Salad bowls with a mix of fresh greens, proteins, and dressings.
Include options like grilled chicken or shrimp for added protein.
Remember to check with the chosen delivery service or restaurant for their menu options and to ensure they can accommodate any dietary restrictions or preferences among your guests. Enjoy your party!"""
    recommendation = parse_food(example_resposne) 
    for sent in recommendation:
        assert int(sent[0]) in range(1,6)

if __name__ == "__main__":
    test()