import time
import datetime
import selectorlib
#%% Run time code here
now = datetime.datetime.now()
print(now)
timestamp = datetime.datetime.timestamp(now)
print(timestamp)
utc = datetime.datetime.utcnow()
timegm = time.time()

print(dir(selectorlib.Extractor))
extractormethods = dir(selectorlib.Extractor)
#%%
print("YOU CAN'T SEE ME")
print(help(selectorlib.Extractor.from_yaml_string()))