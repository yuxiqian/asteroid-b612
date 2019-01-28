#!/Applications/Julia-1.1.app/Contents/Resources/julia/bin/julia
quotes = ["请画一匹马。",
        "请画一只骆驼。",
        "请画一只鸡。",
        "请画一条狗。",
        "请画一只羊。",
        "请画一只鹅。",
        "请画一头牛。",
        "请画一只象。",
        "请画一NoneType。",
        "请画一条蛇。",
        "请画一顶帽子。"]

val_a = 3 + 4im
val_b = 3 - 4im


while 1 > 0
    println(quotes[Int32(sqrt(val_a * val_b))])
    readline(stdin)
end