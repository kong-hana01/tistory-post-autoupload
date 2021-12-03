import requests, json #, textwrap, 
from bs4 import BeautifulSoup

def size18(sentence):
    return f'<p data-ke-size="size18"><b>{sentence}</b></p>'

def size16(sentence):
    return f'<p data-ke-size="size16">{sentence}</p>'
    
def create_table(contents):
    return f'<pre id="code_1626712772758" class="python" style="margin: 20px auto 0px; display: block; overflow: auto; padding: 20px; color: #383a42; background: #f8f8f8; font-size: 14px; font-family: \'SF Mono\', Menlo, Consolas, Monaco, monospace; border: 1px solid #ebebeb; line-height: 1.71; cursor: default; z-index: 1; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" data-ke-language="python" data-ke-type="codeblock">{contents}</pre>'

def create_code(code):
    return f'<pre id="code_1626712944698" class="python" style="margin: 20px auto 0px; display: block; overflow: auto; padding: 20px; color: #383a42; background: #f8f8f8; font-size: 14px; font-family: \'SF Mono\', Menlo, Consolas, Monaco, monospace; border: 1px solid #ebebeb; line-height: 1.71; cursor: default; z-index: 1; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" data-ke-language="python" data-ke-type="codeblock"><code>{code}</code></pre>'

def write1(soup):
    string = ''
    for x in soup:
        string = string + x.text + '<br>'
    return size18(string)

def write2(soup):
    string = ''
    for x in soup:
        string = string + x.text + '<br>'
    return size16(string)

def post_upload(algorithm, problem, token, flag):

    # 파이썬 파일 불러오기
    with open(f"C:/Users/최진만/Project/algorithm/{algorithm}/{problem}.py", "r", encoding="utf-8") as f:
        data = f.readlines()
    
    # 카테고리 아이디 추출
    with open(f"C:/Users/최진만/Project/tistory/tistory_category.json", "r", encoding="utf-8") as json_file:
        c = json.load(json_file)
    category = {}
    for i in range(len(c['categories'])):
        category[c['categories'][i]['name']] = c['categories'][i]['id']

    # 백준 사이트 크롤링
    if 'https://www.acmicpc.net/problem/' not in data[0]:
        url = input('문제주소를 입력해주세요.')
    else:
        url = data[0][2:-1]

    request = requests.get(url)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    # descript_ = write2(soup.select('#problem_description > p'))
    # input_ = write2(soup.select('#problem_input > p'))
    # output_ = write2(soup.select('#problem_output > p'))
    # sample_input_ = create_table(soup.select('#sample-input-1')[0].text)
    # sample_output_ = create_table(soup.select('#sample-output-1')[0].text)
    problem_ = soup.select('#problem-body')[0]
    code_ = create_code(''.join(data))
    
    
    # 코드 정보 재구조화
    i = 1
    approach = ''
    while i < len(data) and '#' in data[i]:
        if '접근' in data[i]:
            i += 1
            continue
        approach += '-' + data[i][1:] + '<br>'
        i += 1
    approach = size16(approach)


    # content = size18('문제') + url + '<br>' + size18('문제 정의') + descript_ + '<br>' + size18('입력') + input_ + '<br>' + size18('출력') +  output_ + '<br>' + \
    #     size18('예제 입력 1') + sample_input_ + '<br>' + size18('예제 출력 1') + sample_output_ + '<br>' + size18('접근 방법') + approach + size18('코드') + code_
    content = str(problem_) + '\n' + size18('접근 방법') + approach + size18('코드') + code_
    problem_number = url.split('/')[-1]
    option = ''
    for x in flag:
        if x == '0':
            option = option + ", " + '백준 브론즈문제'
        elif x == '1':
            option = option + ", " + '백준 실버문제'
        elif x == '2':
            option = option + ", " + '백준 골드문제'
        elif x == '3':
            option = option + ", " + '백준 플레티넘문제'
        elif x == '4':
            option = option + ", " + '삼성 SW 기출문제'

    title = f'백준 온라인 저지, {algorithm} / {problem_number}번: {problem} (파이썬 / {option})'
    blog_name = 'konghana01'
    visibility = 3 # 0: 비공개 - 기본값, 1: 보호, 3: 발행
    tag = f'백준 알고리즘, 파이썬 코딩 테스트, {algorithm}, {problem}, 백준 온라인 저지, 파이썬, 코딩 공부, {option}'
    
    # 글 올리기 전 점검
    print(content)
    if input('내용을 수정하고 싶으면 "r"을 누르세요.') in ['r', 'ㄱ']:
        return
    write = {'access_token': token['access_token'], 'output': 'json', 'blogName': blog_name, 
    'title': title, 'content': content, 'visibility': visibility, 'category': category[algorithm], 'tag': tag}
    write_url = 'https://www.tistory.com/apis/post/write'
    r = requests.post(write_url, data=write)
    print(r.text)

def category_search(token):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    blog_name = 'konghana01'
    params = {'access_token': token['access_token'], 'output': 'json', 'blogName': blog_name}
    url = 'https://www.tistory.com/apis/category/list'
    r = requests.get(url, params=params, headers=header)
    
    if r.status_code == 200:
        print('카테고리 조회 성공')
        r_json = r.json()
        with open("tistory/tistory_category.json", "w") as fp:
            json.dump(r_json['tistory']['item'], fp)

if __name__ == '__main__':
    with open('C:/Users/최진만/Project/tistory/tistory_token.json', "r") as json_file:
        token = json.load(json_file)

    # category_search(token)
    algorithm = input('알고리즘을 입력하세요.')
    problem = input('문제 이름을 입력하세요.')
    flag = input('옵션을 입력하세요.(옵션별 공백 기준) \n브론즈문제: 0, 실버문제: 1, 골드문제: 2, 플레티넘문제: 3, 삼성SW기출문제: 4\n').split()
    post_upload(algorithm, problem, token,flag)
