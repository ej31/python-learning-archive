with open("myfile.txt", "r") as _file:
    for line in _file:
        if "Hello" in line:
            print("Hello 발견했습니다..!")
            # do something... start
            # save to Mysql or SqLite
            # do something... end
