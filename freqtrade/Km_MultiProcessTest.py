import _thread
from multiprocessing.pool import AsyncResult
from RunBotForSingleUser import RunSingleBot 
from main import main
import sys
import asyncio

from multiprocessing import Process

import RunBotForSingleUser as SingleBot


#sys.argv = ['freqtrade', 'trade','-c',r'F:\Projects\Python\FreqTrade\freqtrade\user_data\configs\config.json', '--strategy', 'AverageStrategy']
#_thread .start_new_thread( main, () )
#sys.argv = ['freqtrade', 'trade','-c',r'F:\Projects\Python\FreqTrade\freqtrade\user_data\configs\config1.json','--strategy', 'AverageStrategy']
#_thread .start_new_thread( main, () )

# if __name__ == '__main__':  

from multiprocessing import Pool

if __name__ == '__main__':  
  pool = Pool(processes=10)              # start 4 worker processes    
  

  for x in range(10): 
    result1 = pool.apply_async(SingleBot.RunSingleBot,args = (r'F:\Projects\Python\FreqTrade\freqtrade\user_data\configs\config.json','AverageStrategy' ), callback = log_result)
  

  pool.close()
  pool.join()


