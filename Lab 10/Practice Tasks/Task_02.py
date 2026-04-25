from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
emails = [
    "Win money now",
    "Hello friend how are you",
    "Claim your prize now",
    "Meeting at 5pm",
    "Earn dollars fast"
]

labels = [1, 0, 1, 0, 1]  # 1=spam, 0=not spam
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(emails)
x_train,x_test,y_train,y_test=train_test_split(x,labels,test_size=0.3)
model=SVC(kernel='linear')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("==============================================================")
print("Accuracy:", accuracy_score(y_test, y_pred))
new_email = ["Win a free iPhone"]
new_email_vec = vectorizer.transform(new_email)
print("Spam or Not:", model.predict(new_email_vec))
print("===============================================================")
