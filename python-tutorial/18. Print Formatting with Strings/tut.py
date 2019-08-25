val="Hello Jack {}"
print(val.format('inserted'))
val="ku {} {} {}"
print(val.format('ku', 'ku', 'P'))
val="ku {2} {0} {1}"
print(val.format('ku', 'ki', 'P'))
val="ku {a} {b} {c} {a}"
print(val.format(a='ku', c='ki', b='P'))

res=100/555
print(res)
val="ku {a}"
print(val.format(a=res))

val="ku {a:10.2f}"
print(val.format(a=res))
val="lilo"
name="kuku"
print(f"val{name}")
