def reduce_file_path(s):
    # print("for {0} count:{1}".format(arg,c))
    l = s.split("/")
    st = "/"
    l[0] = " "
    if l.count("") > 0:
        l.remove("")
    for x in range(1, len(l)):
        if l[x] == "" or l[x] == ".":
            l[x] = " "
        if l[x] == "..":
            l[x - 1] = " "
            l[x] = " "

    if l.count("") > 0:
        l.remove("")
    for x in range(2, len(l)):
        if l[x] != " ":
            st += "/{0}".format(l[x])
    print(st)


def main():
    reduce_file_path("/")
    reduce_file_path("/srv/../")
    reduce_file_path("/srv/www/htdocs/wtf/")
    reduce_file_path("/srv/www/htdocs/wtf")
    reduce_file_path("/srv/./././././")
    reduce_file_path("/etc//wtf/")
    reduce_file_path("/etc/../etc/../etc/../")
    reduce_file_path("//////////////")
    reduce_file_path("/../")


if __name__ == '__main__':
    main()
