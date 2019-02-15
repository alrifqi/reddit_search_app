# Import flask deps
from app import app
from flask import Blueprint, request, render_template, flash, g, session, \
        redirect, url_for, json
import praw

show_data = 9
# Set routing and accepted methods
@app.route('/test')
def test():
    return render_template('mod_1/test.html')


@app.route('/reddit/postsearch', methods=['POST', 'GET'])
def reddit_search():
    reddit = praw.Reddit(client_id='Ernv92ALXMZHgg',
                         client_secret='hvN9Fed5-pVmFbAH8_aTy5OSB_M',
                         password='',
                         user_agent='testscript by /u/fakebot3',
                         username='rarex88')
    all = reddit.subreddit("all")
    datas = []
    subreddit = []
    totaldata = 0
    keyword = json.loads(request.data)
    for i in all.search(keyword['keyword'], sort='new', limit=10):
        data = {}
        totaldata += 1
        data['title'] = i.title
        data['subreddit_name_prefixed'] = i.subreddit_name_prefixed
        data['post_link'] = i.url
        data['reddit_link'] = 'https://www.reddit.com'+i.permalink
        if i.subreddit_name_prefixed not in subreddit:
            subreddit.append(i.subreddit_name_prefixed)
        datas.append(data)
    pagination = totaldata / show_data
    if pagination > 0:
        pagination += 1

    respdatas =  []
    count = 0

    if 'page' not in keyword:
        for number in range(0,9) :
            if count > 9:
                break
            respdatas.append(datas[number])
            count += 1
    else:
        currentPage = (int(keyword['page']))*show_data-1
        prevPage = (int(keyword['page'])-1)*show_data-1


        for number in range(prevPage, currentPage):
            if count > 9 or (count+prevPage)>totaldata-1:
                break
            respdatas.append(datas[number])
            count += 1


    resp = {"post":respdatas, "subreddit":subreddit, "keyword":keyword, "pagination": pagination }

    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/reddit/subreddit', methods=['GET','POST'])
def reddit_subreddit():
    subreddit_keys = json.loads(request.data)
    datas = []
    subreddit = []
    reddit = praw.Reddit(client_id='Ernv92ALXMZHgg',
                         client_secret='hvN9Fed5-pVmFbAH8_aTy5OSB_M',
                         password='Alrifqi1988_',
                         user_agent='testscript by /u/fakebot3',
                         username='rarex88')
    print subreddit_keys['subreddit_key'].replace('r/','')
    for i in reddit.subreddit(subreddit_keys['subreddit_key'].replace('r/','')).hot(limit=25):
        data = {}
        data['title'] = i.title
        data['subreddit_name_prefixed'] = i.subreddit_name_prefixed
        data['post_link'] = i.url
        data['reddit_link'] = 'https://www.reddit.com' + i.permalink
        if i.subreddit_name_prefixed not in subreddit:
            subreddit.append(i.subreddit_name_prefixed)
        datas.append(data)
        resp = {"post": datas, "subreddit": subreddit, "keyword": ''}

        response = app.response_class(
            response=json.dumps(resp),
            status=200,
            mimetype='application/json'
        )
        return response
