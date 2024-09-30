import requests
from bs4 import BeautifulSoup
import asyncio
from util_dc_bot import send_message

OUR_PROJECT_NAME = 'Lazy Diffusion - 予你閒畫'

url = "https://genaistars.org.tw/vote"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

data_list = []

vote_items = soup.find_all('div', class_='vote_item')

for item in vote_items:
    title = item.find('a', class_='info_title').text.strip()
    count = int(item.find('span').text.strip())
    
    data_list.append({'title': title, 'count': count})

sorted_data = sorted(data_list, key=lambda x: x['count'], reverse=True)

title_width = 70
count_width = 10

print(f"{'Rank':<8} {'Count':<{count_width}} {'Title':<{title_width}}")

for i, data in enumerate(sorted_data):
    if data['title'] == 'Lazy Diffusion - 予你閒畫':

        print(f"{i+1:<8} {data['count']:<{count_width}} 🌟{data['title']:<{title_width}}")
    else:
        print(f"{i+1:<8} {data['count']:<{count_width}} {data['title']:<{title_width}}")


def rank_msg_generator():
    return_msg = ""
    our_rank = [i+1 for i, data in enumerate(sorted_data) if data['title'] == OUR_PROJECT_NAME][0]

    def gen_msg_with_rank(rank):
        return f"Rank {rank}: {sorted_data[rank-1]['title']} - {sorted_data[rank-1]['count']} votes\n"

    # previous position
    return_msg += gen_msg_with_rank(our_rank-1)

    # our position
    return_msg += gen_msg_with_rank(our_rank)

    # next position
    return_msg += gen_msg_with_rank(our_rank+1)

    return_msg += "-" * 70 + "\n"

    # 10th position
    return_msg += gen_msg_with_rank(10)

    return return_msg




if __name__ == "__main__":
    # print(rank_msg_generator())
    asyncio.run(send_message(rank_msg_generator()))
    
# print("-" * 100)
# rank_mes = "Our Rank:", [i+1 for i, data in enumerate(sorted_data) if data['title'] == OUR_PROJECT_NAME][0]
# print(rank_mes)




