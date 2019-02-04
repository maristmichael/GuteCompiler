def main():
    f = open('dumb.txt', 'r')
    data = f.read()
    f.close()
    print(type(data))

    
if __name__ == '__main__':
    main()
    