f=open("refs.bib","r",encoding='utf-8')
#查看多少行
citations=[]
for line in f:
	begin=line.find('@')
	if begin == 0:
		begin_ = line.find('{')
		end = line.find(',')
		citations.append(line[begin_+1:end])

#print(citations)

repeat=[]

news_citations = []
for citation in citations:
	if citation not in news_citations:
		news_citations.append(citation)
	else:
		repeat.append(citation)

print(repeat)





