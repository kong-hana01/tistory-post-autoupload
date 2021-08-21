import requests #, json, textwrap, 
from bs4 import BeautifulSoup

def size18(sentence):
    return f'<p data-ke-size="size18"><b>{sentence}</b></p>'

def size16(sentence):
    return f'<p data-ke-size="size16"><b>{sentence}</b></p>'
    
def create_table(contents):
    return f'<pre id="code_1626712772758" class="python" style="margin: 20px auto 0px; display: block; overflow: auto; padding: 20px; color: #383a42; background: #f8f8f8; font-size: 14px; font-family: \'SF Mono\', Menlo, Consolas, Monaco, monospace; border: 1px solid #ebebeb; line-height: 1.71; cursor: default; z-index: 1; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" data-ke-language="python" data-ke-type="codeblock">{contents}</pre>'

# with open(f"C:/Users/최진만/Project/algorithm/greedy/선긋기.py", "r", encoding="utf-8") as f:
#     data = f.readlines()
#     print(data[0][2:])
    
def post_upload(algorithm, problem):
    with open(f"C:/Users/최진만/Project/algorithm/{algorithm}/{problem}.py", "r", encoding="utf-8") as f:
        data = f.readlines()

    if 'https://www.acmicpc.net/problem/' not in data[0]:
        url = input('문제주소를 입력해주세요.')
    else:
        url = data[0][2:]

    request = requests.get(url)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    descript_ = soup.select('#problem_description > p')
    input_ = soup.select('#problem_input > p')
    sample_input = soup.select('#sample-input-1')
    sample_output = soup.select('#sample-output-1')

