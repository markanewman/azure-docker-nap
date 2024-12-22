import pathlib
import time

f_in: pathlib.Path = pathlib.Path('/data/in.txt')
f_out: pathlib.Path = pathlib.Path('/data/out.txt')

print('--- azure-docker-nap ---')
print(f'File In: {f_in}')
print(f'File Out: {f_out}')
print(f'Read: {f_in.exists()}')
print(f'Nap ...')
time.sleep(5)
print(f'Wake')
print('Writing ...')
with open(f_out, mode = 'w', encoding = 'utf8') as fp:
    fp.write('')
print('Written')
