from re import T


text_test = 'hello world'
text_test_strip ='   he he   hee hhe  '


print (text_test.upper())
print("eeee".upper())
print("HASDLF".lower())

print(text_test_strip.strip())

print(text_test_strip.replace('hee', 'nice'))

print(text_test.split(","))



age = 36
year = 1999
ip= '192.168.1.2'
txt = 'my name is hai, i am {}, and was born in {} , local address is {}'

print(txt.format(age,year,ip))
