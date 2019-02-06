def main():
    f = open('dumb.txt', 'r')
    data = f.read()
    f.close()
    print(data)

    
if __name__ == '__main__':
    main()
    