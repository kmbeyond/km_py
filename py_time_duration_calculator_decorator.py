

def deco_time_calculator(func_to_decorate):
  def func_wrapped(*args, **kwargs):
    from datetime import datetime
    time_start = datetime.now()
    func_to_decorate(*args, **kwargs)
    time_end = datetime.now()
    time_diff = time_end-time_start
    print(f"Duration: {time_diff}")
  return func_wrapped


#sample function
@deco_time_calculator
def get_sum(till_num):
    total=0
    for i in range(till_num): total=total+i
    print("Total: ", total)

get_sum(100000000)


#decorate the function with our decorator (if not using syntactic sugar)
#km = deco_time_calculator(get_sum)
#km(100000000)

