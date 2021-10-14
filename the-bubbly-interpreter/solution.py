# credit to Unnamed

get = lambda x: x if callable(x) else lambda s, c: c(s, s[x] if isinstance(x, str) else x)
start = lambda x: x({}, None)
return_ = lambda s, c: lambda x: get(x)(s, lambda _s, x: x)
let = lambda s, c: lambda x: lambda y: get(y)(s, lambda s, y: lambda z: z({**s, x: y}, None))
add = lambda s, c: lambda x: get(x)(s, lambda s, x: lambda y: get(y)(s, lambda s, y: c(s, x + y)))
sub = lambda s, c: lambda x: get(x)(s, lambda s, x: lambda y: get(y)(s, lambda s, y: c(s, x - y)))
mul = lambda s, c: lambda x: get(x)(s, lambda s, x: lambda y: get(y)(s, lambda s, y: c(s, x * y)))
div = lambda s, c: lambda x: get(x)(s, lambda s, x: lambda y: get(y)(s, lambda s, y: c(s, x // y)))
