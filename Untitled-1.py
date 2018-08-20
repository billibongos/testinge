taken = ['REGION_CLUSTER', 'MAINTENANCE_VENDOR', 'MANUFACTURER', 'WELL_GROUP', 'DAYS_SINCE_START', 'too_soon',
           'S15', 'S17', 'S13', 'S5', 'S16', 'S19', 'S18', 'S8', 'S15_mean', 'S15_median', 'S15_max', 'S15_min',
           'S17_mean', 'S17_median', 'S17_max', 'S17_min', 'S13_mean', 'S13_median', 'S13_max', 'S13_min', 'S5_mean',
           'S5_median', 'S5_max', 'S5_min', 'S16_mean', 'S16_median', 'S16_max', 'S16_min', 'S19_mean', 'S19_median',
           'S19_max', 'S19_min', 'S18_mean', 'S18_median', 'S18_max', 'S18_min', 'S8_mean', 'S8_median', 'S8_max',
           'S8_min', 'S5_chg', 'S8_chg', 'S13_chg', 'S15_chg', 'S16_chg', 'S17_chg', 'S18_chg', 'S19_chg']



initial = ['index', 'ID', 'DATE', 'REGION_CLUSTER', 'MAINTENANCE_VENDOR',
       'MANUFACTURER', 'WELL_GROUP', 'S15', 'S17', 'S13', 'S5', 'S16', 'S19',
       'S18', 'EQUIPMENT_FAILURE', 'S8', 'AGE_OF_EQUIPMENT',
       'DAYS_SINCE_START', 'too_soon', 'S15_mean', 'S15_median', 'S15_max',
       'S15_min', 'S17_mean', 'S17_median', 'S17_max', 'S17_min', 'S13_mean',
       'S13_median', 'S13_max', 'S13_min', 'S5_mean', 'S5_median', 'S5_max',
       'S5_min', 'S16_mean', 'S16_median', 'S16_max', 'S16_min', 'S19_mean',
       'S19_median', 'S19_max', 'S19_min', 'S18_mean', 'S18_median', 'S18_max',
       'S18_min', 'S8_mean', 'S8_median', 'S8_max', 'S8_min', 'S15_chg',
       'S17_chg', 'S13_chg', 'S5_chg', 'S16_chg', 'S19_chg', 'S18_chg',
       'S8_chg', 'FAILURE_DATE', 'FAILURE_TARGET']

b = set(initial)-set(taken)
print(b)

def summa(x=0):
    return x*2

var = summa

print(var)

print(var(2))

c = 8
b = 9

class Some():
    def __init__(self): 
        self.a = 5
    def do(self):
        self.a = self.a *10
        return self.a

b = Some()
b.do()

c = Some()
c.do()