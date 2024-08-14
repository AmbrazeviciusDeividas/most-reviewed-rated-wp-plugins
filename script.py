import requests

def get_plugins(orderby, per_page=50):
    url = f"https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[orderby]={orderby}&request[per_page]={per_page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('plugins', [])
    else:
        print("Error fetching data from the API")
        return []

def sort_plugins(plugins, key):
    return sorted(plugins, key=lambda x: x.get(key, 0), reverse=True)

def print_plugins(plugins):
    for plugin in plugins:
        print(f"Name: {plugin['name']}")
        print(f"Slug: {plugin['slug']}")
        print(f"Downloads: {plugin.get('downloaded', 'N/A')}")
        print(f"Rating: {plugin.get('rating', 'N/A')}")
        print(f"Number of Ratings: {plugin.get('num_ratings', 'N/A')}")
        print(f"Description: {plugin.get('short_description', 'N/A')}")
        print("-" * 40)

def main():
    print("Choose an option:")
    print("1. Most Downloaded Plugins")
    print("2. Most Reviewed Plugins")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        plugins = get_plugins(orderby='downloads')
        sorted_plugins = sort_plugins(plugins, key='downloaded')
    elif choice == '2':
        plugins = get_plugins(orderby='rating')
        sorted_plugins = sort_plugins(plugins, key='num_ratings')
    else:
        print("Invalid choice")
        return

    print_plugins(sorted_plugins)

if __name__ == "__main__":
    main()

