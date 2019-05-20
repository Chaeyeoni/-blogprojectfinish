from django.shortcuts import render

def wordhome(request):
    return render(request, 'wordhome.html')

def wordabout(request):
    return render(requet, 'wordabout.html')

def wordresult(request):
    text = request.GET['fulltext']
    #원문 글자체를 가지고 와라는 뜻을 text에 담아줌
    words = text.split()
    #split함수는 string을 공백을 기준으로 단어를 리스트화 시켜줌
    # 총 단어 수를 변환 시키는 것은 len
    word_dic = {}

    for word in words:
        if word in word_dic:
            #increase
            word_dic[word]+=1
        else:
            #add to dictionary
            word_dic[word]=1
    return render(request,'wordresult.html', {'full': text, 'total' : len(words), 'dictionary': word_dic.items()})
# Create your views here.
