from vectorizer import compare_texts

text1=raw_input("Enter String 1 : ")
text2=raw_input("Enter String 2 : ")
a=compare_texts(text1, text2)*100
print str(a)+"%"
