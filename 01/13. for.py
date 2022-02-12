for alpha in 'ChaCha':
    print(alpha)

page=10
for x in range (0,10,1):
    page=page+10
    print(('https://www.indeed.com/jobs?q=python&start='+str(page)))

