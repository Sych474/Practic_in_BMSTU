import time 

M = 5
time_val = 0
start = 1
print('Время приведено в милисекундах (0.001 с)')
print('Количество запусков =',M)
for i in range(M):
	
	start_time = time.time()
	import lib
	F = lib.get_lens(int(start))
	time_val +=(time.time()-start_time)
	print((time.time()-start_time)*1000)

print('Среднее время работы Python+Cython:', '{:14.2f}'.format(time_val/M*1000),'мс.')
