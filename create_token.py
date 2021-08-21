# import requests

# '''
# code
# https://www.tistory.com/oauth/authorize?client_id=678738155865039c00e009721d2807f9b&redirect_uri=http://localhost:3033/&response_type=code

# access_token
# https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={secret_key}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code
# '''

# blog = 'https://konghana01.tistory.com/'
# redirect_uri = 'http://localhost:3033/'
# client_id = '678738155865039c00e009721d287f9b'
# secret_key = '678738155865039c00e009721d287f9b4ed19b7f28774de94f9e202a7ce99307d234c8e7'
# print(f'https://www.tistory.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code')

# code = input('code:')
# print('access_token', f'https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={secret_key}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code', sep='\n')

# # token_url = f'https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={secret_key}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code'
# # r = requests.get(token_url)
# # print(r.text)
# # access_token = r.text
# access_token = '1d0e5b184a5830bd4fa5bbdc0c06e253_f156abb8ddd1562390af6d3cbc38fbb4'
