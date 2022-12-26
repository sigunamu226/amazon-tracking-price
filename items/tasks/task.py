from apscheduler.schedulers.background import BackgroundScheduler
from items.models import CacheItems, Item
from items.service import periodicUpdate

def periodicExecution():# 任意の関数名
    # ここに定期実行したい処理を記述する
    items = Item.objects.all()
    for item in items:
        nowPrice = periodicUpdate(item.url)
        if(item.now_price != nowPrice):
            CacheItems(item=item, old_price=item.now_price).save()
            oldItem = CacheItems.objects.filter(item=item).earliest("created_at")
            fluctuating_value = int(nowPrice) - int(oldItem.old_price)
            item.fluctuating_value = str(fluctuating_value)
            item.now_price = nowPrice
            item.save()
    
        
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodicExecution, 'interval', hours=1)# 1時間おきに実行
    scheduler.start()

  
# 5分おきに実行
# scheduler.add_job(periodic_execution, 'interval', minutes=5)

# 1時間5秒おきに実行
# scheduler.add_job(periodic_execution, 'interval', hours=1, seconds=5)

# 1日おきに実行
# scheduler.add_job(periodic_execution, 'interval', days=1)

# 1週間おきに実行
# scheduler.add_job(periodic_execution, 'interval', weeks=1)

# 2022年4月1日19時〜20時の間、1分おきに実行
# scheduler.add_job(periodic_execution, 'interval', minutes=1,
    # start_date="2022-04-01 19:00:00",
    # end_date="2022-04-01 20:00:00")

# 毎時20分に実行
# scheduler.add_job(periodic_execution, 'cron', minute=20)

# 月曜から金曜の間、8時に実行
# scheduler.add_job(periodic_execution, 'cron', hour=8, day_of_week='mon-fri')