from app import parse_food  # Assuming parse_food is defined in the app module


def test():
    example_response = """Absolutely! Congratulations on your happiness! 
        Here are some popular and delicious options for 
        delivery food menus that you can consider for your party:

        Pizza Party:

        Choose from a variety of pizzas with different 
        toppings to cater to everyone's preferences.
        Consider adding some sides like garlic bread, 
        chicken wings, or salads.

        Mexican Fiesta:

        Order a selection of tacos, burritos, and quesadillas.
        Include sides such as guacamole, salsa, and nachos with cheese.

        Asian Fusion:

        Sushi platters with a mix of rolls and sashimi.
        Add some Chinese favorites like spring rolls, 
        dumplings, and sweet and sour chicken.

        Mediterranean Feast:

        Gyros or kebabs with a variety of meats and veggies.
        Include hummus, tzatziki, and a selection of fresh salads.

        Burger Bash:

        Gourmet burgers with different toppings and sauces.
        Don't forget to add some fries or onion rings on the side.
        Enjoy your party!"""

    recommendations = parse_food(example_response)
    for sent in recommendations:
        first_char = sent[0].strip()
        if first_char.isdigit():
            assert int(first_char) in range(1, 6)


if __name__ == "__main__":
    test()
