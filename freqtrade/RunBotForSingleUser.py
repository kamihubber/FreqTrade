import asyncio
from main import main
import sys


def RunSingleBot(configpath,strategyname) :
  sys.argv = ['freqtrade', 'trade','-c',configpath,'--strategy',strategyname]
  print("i am running single with config" + configpath)
  main()

def RunSingleBot2(configpath,strategyname,loop) :
  asyncio.set_event_loop(loop)
  task = loop.create_task(RunSingleBot(configpath,strategyname))
  loop.run_until_complete(task)
  

# def RunSingleBot() :  
#   print("i am running single")
#   print(sys.argv[1])
  #main()

def printsmt(param) :
  print("hello!!");  
  #print(param)  