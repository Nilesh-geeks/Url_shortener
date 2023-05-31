import requests

def shorten_url(full_link,link_name):

    API_KEY='760675b8e72e55d38de91ce52e5de2f3'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key':API_KEY , 'short': full_link,'name': link_name}
    request = requests.get(BASE_URL , params = payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title',title)
        print('Link :',short_link)
    except:
        status = data['url']['status']
        print('Error Status : ',status)

# shorten_url('https://www.google.com/search?q=apples&oq=apples&aqs=chrome..69i57.1151j0j1&sourceid=chrome&ie=UTF-8','abc_xc')

link = input("Enter the url : ")
name = input("Enter the name for Url : ")

shorten_url(link,name)