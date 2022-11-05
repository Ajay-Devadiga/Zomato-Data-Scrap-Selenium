import ZomatoParserModule


restaurant_list = ZomatoParserModule.getRestaurantList("411021")
for restaurant in restaurant_list:
    url = f"https://www.zomato.com/{restaurant['url']}"
    print(url)
    print(type(restaurant))
    ZomatoParserModule.navigateRestaurantPage(url)
    print("#######################################")