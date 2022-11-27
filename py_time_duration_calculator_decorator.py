

def deco_time_calculator(func_to_decorate):
  def func_wrapped(*args, **kwargs):
    from datetime import datetime
    time_start = datetime.now()
    func_to_decorate(*args, **kwargs)
    time_end = datetime.now()
    time_diff = time_end-time_start
    print(f"Metrics: {time_diff}")
  return func_wrapped


#sample function
def get_sum(till_num):
    total=0
    for i in range(till_num): total=total+i
    print("Total: ", total)

# let's decorate the function with our decorator
km = deco_time_calculator(get_sum)

km(100000000)

