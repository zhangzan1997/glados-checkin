import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]
# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]
#'SCU134959T91379aa989feb3f71eb5cff3f4ad44175fd5a2f6d1f46'
# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]
#'_ga=GA1.2.1814369912.1607835534; _gid=GA1.2.689969317.1607835534; koa:sess=eyJ1c2VySWQiOjQ3NDU0LCJfZXhwaXJlIjoxNjMzNzU1NjM1MzUzLCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=C7sdjK-t0k3vo_kL2u2W4jEzxh8'



def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
    
